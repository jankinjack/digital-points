
from typing import TYPE_CHECKING
import pickle

import numpy as np

import zmq

if TYPE_CHECKING:
    from model.graph_view import GraphView


class IPC():
    """
    Inter-Process Communication manager using ZeroMQ.

    Automatically binds to an available port for publishing data
    and connects to other instances' ports for subscribing, effectively
    creating a peer-to-peer mesh network for data synchronization.
    """

    __slots__ = (
        '_context',
        '_start_port',
        '_instance',
        '_pub',
        '_subs',
        )

    def __init__(self, max_instances: int = 10) -> None:
        # Initialize ZeroMQ context with 2 IO threads for better concurrency.
        self._context = zmq.Context(io_threads=2)

        self._start_port = 48900
        self._instance = -1
        self._subs = []

        # Setup publisher (PUSH) socket.
        self._pub = self._context.socket(zmq.PUSH)
        self._pub.setsockopt(zmq.SNDHWM, 100000)
        self._pub.setsockopt(zmq.LINGER, 0)
        self._pub.setsockopt(zmq.SNDBUF, 4 * 1024 * 1024)

        for instance in range(max_instances):
            port = self._start_port + instance
            address = f'tcp://127.0.0.1:{port}'

            try:
                # Try to bind the publisher
                # if we haven't found an available port yet
                if self._instance == -1:
                    self._pub.bind(address)
                    self._instance = instance
                else:
                    raise zmq.error.ZMQError
            except zmq.error.ZMQError:
                # Create a subscriber (PULL) for this port
                # (either it's used by another process,
                # or we already bound our own publisher)
                sub = self._context.socket(zmq.PULL)
                sub.connect(address)
                sub.setsockopt(zmq.RCVHWM, 100000)
                sub.setsockopt(zmq.RCVBUF, 4 * 1024 * 1024)
                self._subs.append(sub)

    @property
    def instance(self) -> int:
        """ Returns the current instance ID. """
        return self._instance

    @property
    def port(self) -> int:
        """ Returns the port number assigned to this instance. """
        return self._start_port + self._instance

    def send_data(self, graph_view: 'GraphView') -> None:
        """
        Serializes and sends graph data to all connected subscribers.
        Uses a multi-part message: metadata followed by binary numpy arrays.
        """

        batch_meta = []
        arrays = []

        for i, axis in enumerate(graph_view.axes):
            if not axis.lines:
                continue

            x_data = axis.lines[0].x_data

            # Skip if x_data is missing or empty.
            if x_data is None or len(x_data) == 0:
                continue

            # Filter out internal IPC lines.
            filtered_lines = [
                line for line in axis.lines if not line.name().startswith('ipc')
                ]

            if not filtered_lines:
                continue

            # Stack arrays efficiently using np.vstack.
            # This also safely promotes dtype
            # if x_dataand y_data have different types.
            y_arrays = [line.y_data for line in filtered_lines]

            try:
                array = np.vstack((x_data, *y_arrays))
            except Exception:
                continue

            meta = {
                'instance': self._instance,
                'axis': i,
                'names': [line.name() for line in filtered_lines],
                'shape': array.shape,
                'dtype': str(array.dtype),
            }

            batch_meta.append(meta)
            arrays.append(array)

        if not batch_meta:
            return

        try:
            # Send metadata as the first part of the message.
            self._pub.send(
                pickle.dumps(batch_meta), flags=zmq.NOBLOCK | zmq.SNDMORE
                )

            # Send numpy arrays as subsequent parts without copying memory.
            for array in arrays:
                self._pub.send(array, copy=False, flags=zmq.NOBLOCK)
        except Exception:
            pass

    def receive_data(self) -> list[tuple[int, int, list[str], np.ndarray]]:
        """
        Receives and deserializes data from all connected subscribers.
        Returns a list of tuples containing:
            (instance_id, axis_index, line_names, data_array).
        """

        data = []

        for sub in self._subs:
            try:
                # Receive metadata part.
                meta_bytes = sub.recv(flags=zmq.NOBLOCK)
                batch_meta = pickle.loads(meta_bytes)

                # Receive corresponding data arrays.
                for meta in batch_meta:
                    raw = sub.recv(flags=zmq.NOBLOCK, copy=False)

                    try:
                        array = np.frombuffer(
                            raw, dtype=meta['dtype']
                        ).reshape(meta['shape'])

                        data.append((
                            meta['instance'],
                            meta['axis'],
                            meta['names'],
                            array,
                            ))
                    except (ValueError, TypeError):
                        pass
            except Exception:
                continue

        return data

    def close(self) -> None:
        """ Closes all sockets and terminates the context. """

        if self._pub:
            self._pub.close()
        for sub in self._subs:
            sub.close()
        self._context.term()

    def __enter__(self) -> 'IPC':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
