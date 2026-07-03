from typing import Callable

import numpy as np


class FrameRateTracker:
    def __init__(
            self,
            window_size: int = 100,
            progress_func: Callable = lambda _: False
            ) -> None:

        self._window_size = window_size
        self._array = np.zeros(window_size)
        self._pointer = 0
        self._sum = 0.0
        self._progress_func = progress_func

    def __call__(self, new_frame_rate: float) -> None:
        """ Handler of frame_rate_changed. """

        self._sum = self._sum - self._array[self._pointer] + new_frame_rate
        self._array[self._pointer] = new_frame_rate
        self._pointer = (self._pointer + 1) % self._window_size

        frame_rate = self._sum / self._window_size

        self._progress_func(f'{frame_rate:.1f} fps')
