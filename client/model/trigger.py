
from typing import Any, Optional

from PySide6.QtCore import QObject, Signal

import numpy as np

from model.line import VAR_TYPE_CODE


# Mapping of trigger edge names to their internal integer codes.
TRIGGER_EDGES = {
    'Leading Edge': 0,
    'Trailing Edge': 1,
    'Alter Edge': 2,
    }
TRIGGER_EDGES_REVERSE = {v: k for k, v in TRIGGER_EDGES.items()}


class Trigger(QObject):
    """
    Central configuration hub for oscilloscope triggers and FRA settings.
    Acts as a model that emits Qt signals to update the UI
    and save configurations.
    """

    __slots__ = (
        '_enable_save_config',
        '_type',
        '_type_str',
        '_address',
        '_one_shot_mode',
        '_stage',
        '_pre_trigger',
        '_post_trigger',
        '_max_number_samples',
        '_number_samples',
        '_tx_number_samples',
        '_count',
        '_sample_count',
        '_level',
        '_edge',
        '_settling_time',
        '_settling_samples',
        '_sampling_frequency',
        '_number_of_variables',
        '_fra_frequencies',
        '_fra_n_list',
        '_fra_dividers',
        '_fra_amplitudes',
        '_fra_progress',
        '_fra_repeat',
        '_fra_average_type',
        '_fra_excitation_type',
        '_fra_harmonics',
        )

    set_config_parameter = Signal(
        (tuple, str),
        (tuple, int),
        (tuple, float),
        (tuple, bool),
        )
    set_sampling_frequency = Signal(str)
    set_pre_trigger = Signal(str)
    set_post_trigger = Signal(str)
    update_f_min_max = Signal()
    recompute_pre_post_triggers = Signal()
    stage_changed = Signal()
    fra_progress_changed = Signal()

    def __init__(self, enable_save_config: bool = True) -> None:
        super().__init__()

        self._enable_save_config = enable_save_config

        self._type = VAR_TYPE_CODE['immediate_t']
        self._type_str = 'immediate_t'
        self._address = 0

        self._one_shot_mode = False
        self._stage = '-'

        self._pre_trigger = 0
        self._post_trigger = 0
        self._max_number_samples = 1
        self._number_samples = 1
        self._tx_number_samples = 1
        self._count = 0
        self._sample_count = 0
        self._level = 0.0
        self._edge = TRIGGER_EDGES['Leading Edge']
        self._settling_time = 0
        self._settling_samples = 0
        self._sampling_frequency = 1
        self._number_of_variables = 0

        self._fra_frequencies = np.array([], dtype=np.float64)
        self._fra_n_list = np.array([], dtype=np.uint64)
        self._fra_dividers = np.array([], dtype=np.uint64)
        self._fra_amplitudes = np.array([], dtype=np.float64)
        self._fra_progress = (0, 0)
        self._fra_repeat = 1
        self._fra_average_type = 'Vector Averaging'
        self._fra_excitation_type = 'Single-Sine Excitation'
        self._fra_harmonics = np.array([], dtype=np.uint64)

        self.clear()

    @property
    def type_(self) -> int:
        return self._type

    @property
    def type_str(self) -> str:
        return self._type_str

    @type_.setter
    def type_(self, new_type: str) -> None:
        self._type = VAR_TYPE_CODE.get(new_type, VAR_TYPE_CODE['uint32_t'])
        self._type_str = new_type

    @property
    def address(self) -> int:
        return self._address

    @address.setter
    def address(self, new_address: int) -> None:
        self._address = new_address

    @property
    def one_shot_mode(self) -> bool:
        return self._one_shot_mode

    @one_shot_mode.setter
    def one_shot_mode(self, new_one_shot_mode: bool | int) -> None:
        self._one_shot_mode = bool(new_one_shot_mode)
        self._save_config(('trigger', 'one_shot_mode'), self._one_shot_mode)

    @property
    def stage(self) -> str:
        return self._stage

    @stage.setter
    def stage(self, new_stage: str) -> None:
        self._stage = new_stage
        self.stage_changed.emit()

    @property
    def pre_trigger(self) -> int:
        return self._pre_trigger

    @pre_trigger.setter
    def pre_trigger(
            self,
            new_pre_trigger: int,
            ) -> None:

        if self._pre_trigger != new_pre_trigger:
            self._pre_trigger = new_pre_trigger

            self._compute_pre_post_trigger_time()
            self._compute_number_samples()

            self.recompute_pre_post_triggers.emit()

            self._save_config(('trigger', 'pre_trigger'), new_pre_trigger)

    @property
    def post_trigger(self) -> int:
        return self._post_trigger

    @post_trigger.setter
    def post_trigger(
            self,
            new_post_trigger: int,
            ) -> None:

        if self._post_trigger != new_post_trigger:
            self._post_trigger = new_post_trigger

            self._compute_pre_post_trigger_time()
            self._compute_number_samples()

            self.recompute_pre_post_triggers.emit()

            self._save_config(('trigger', 'post_trigger'), new_post_trigger)

    @property
    def max_number_samples(self) -> int:
        return self._max_number_samples

    @max_number_samples.setter
    def max_number_samples(
            self,
            new_number_samples: int,
            ) -> None:

        if self._max_number_samples != new_number_samples:
            self._max_number_samples = new_number_samples

            self.recompute_pre_post_triggers.emit()

            self._save_config(
                ('trigger', 'samples number'),
                new_number_samples
                )

    @property
    def number_samples(self) -> int:
        return self._number_samples

    @property
    def number_of_variables(self) -> int:
        return self._number_of_variables

    @number_of_variables.setter
    def number_of_variables(self, new_number_of_variables: int) -> None:
        self._number_of_variables = new_number_of_variables
        self._compute_number_samples()
        self.recompute_pre_post_triggers.emit()

    @property
    def tx_number_samples(self) -> Optional[int]:
        return self._tx_number_samples

    @tx_number_samples.setter
    def tx_number_samples(
            self,
            new_tx_number_samples: Optional[int]
            ) -> None:
        self._tx_number_samples = new_tx_number_samples

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, new_count: int) -> None:

        if self._count != new_count:
            self._count = new_count
            self._save_config(('trigger', 'count'), new_count)

    @property
    def sample_count(self) -> int:
        return self._sample_count

    @sample_count.setter
    def sample_count(self, new_sample_count: int) -> None:

        if self._sample_count != new_sample_count:
            self._sample_count = new_sample_count
            self._save_config(('sample count',), new_sample_count)

    @property
    def level(self) -> int | float:
        return self._level

    @level.setter
    def level(self, new_level: int | float) -> None:

        if self._type in (
                VAR_TYPE_CODE['float32_t'],
                VAR_TYPE_CODE['float64_t']):
            self._level = float(new_level)
        else:
            self._level = int(new_level)

        self._save_config(('trigger', 'level'), self._level)

    @property
    def edge(self) -> int:
        return self._edge

    @edge.setter
    def edge(self, new_edge: str) -> None:

        self._edge = TRIGGER_EDGES.get(new_edge, TRIGGER_EDGES['Leading Edge'])
        self._save_config(('trigger', 'edge'), new_edge)

    @property
    def edge_name(self) -> str:
        return TRIGGER_EDGES_REVERSE[self._edge]

    @property
    def settling_time(self) -> int | float:
        return self._settling_time

    @settling_time.setter
    def settling_time(self, new_settling_time: int | float) -> None:

        if self._settling_time != new_settling_time:
            self._settling_time = new_settling_time

            self._update_settling_samples()

            self._save_config(('trigger', 'settling time'), new_settling_time)

    @property
    def settling_samples(self) -> int:
        return self._settling_samples

    @property
    def sampling_frequency(self) -> int | float:
        return self._sampling_frequency

    @sampling_frequency.setter
    def sampling_frequency(self, new_sampling_frequency: int | float) -> None:

        if self._sampling_frequency != new_sampling_frequency:
            self._sampling_frequency = new_sampling_frequency

            self.set_sampling_frequency.emit(
                str(new_sampling_frequency) if new_sampling_frequency else '-'
                )

            self._update_settling_samples()
            self._compute_pre_post_trigger_time()

            self._save_config(('sampling frequency',), new_sampling_frequency)

    @property
    def fra_progress(self) -> tuple[float, int]:
        return self._fra_progress

    @fra_progress.setter
    def fra_progress(self, new_fra_progress: tuple[float, int]) -> None:
        self._fra_progress = new_fra_progress
        self.fra_progress_changed.emit()

    @property
    def fra_frequencies(self) -> np.ndarray:
        return self._fra_frequencies

    @fra_frequencies.setter
    def fra_frequencies(
            self,
            new_fra_frequencies: np.ndarray,
            ) -> None:

        old_len = len(self._fra_frequencies)
        new_len = len(new_fra_frequencies)

        if new_len <= old_len:
            self._fra_amplitudes = self._fra_amplitudes[:new_len].astype(
                np.float64
                )
        else:
            fill_value = self._fra_amplitudes[-1] if old_len > 0 else 1.0
            ext_array = np.full(
                new_len - old_len, fill_value, dtype=np.float64
                )
            self._fra_amplitudes = np.concatenate(
                (self._fra_amplitudes, ext_array)
                )

        self._fra_frequencies = new_fra_frequencies

    @property
    def fra_n_list(self) -> np.ndarray:
        return self._fra_n_list

    @fra_n_list.setter
    def fra_n_list(
            self,
            new_n_list: np.ndarray
            ) -> None:
        self._fra_n_list = new_n_list

    @property
    def fra_dividers(self) -> np.ndarray:
        return self._fra_dividers

    @fra_dividers.setter
    def fra_dividers(
            self,
            new_dividers: np.ndarray
            ) -> None:
        self._fra_dividers = new_dividers

    @property
    def fra_amplitudes(self) -> np.ndarray:
        return self._fra_amplitudes

    @fra_amplitudes.setter
    def fra_amplitudes(
            self,
            new_amplitudes: np.ndarray
            ) -> None:
        self._fra_amplitudes = new_amplitudes

    @property
    def fra_repeat(self) -> int:
        return self._fra_repeat

    @fra_repeat.setter
    def fra_repeat(self, new_repeat: int) -> None:
        self._fra_repeat = new_repeat

    @property
    def fra_average_type(self) -> str:
        return self._fra_average_type

    @fra_average_type.setter
    def fra_average_type(self, new_average_type: str) -> None:
        self._fra_average_type = new_average_type

    @property
    def fra_excitation_type(self) -> str:
        return self._fra_excitation_type

    @fra_excitation_type.setter
    def fra_excitation_type(self, new_excitation_type: str) -> None:
        self._fra_excitation_type = new_excitation_type

    @property
    def fra_harmonics(self) -> np.ndarray:
        return self._fra_harmonics

    @fra_harmonics.setter
    def fra_harmonics(self, new_fra_harmonics: np.ndarray) -> None:
        self._fra_harmonics = new_fra_harmonics

    def clear(self) -> None:
        """ Reset trigger parameters to their default state. """

        self.type_ = 'immediate_t'
        self._address = 0

    def _save_config(self, key: str | tuple[str, ...], value: Any) -> None:
        """
        Safely emit the configuration saving signal based on the value's type.
        Centralizes the repetitive saving logic used across all setters.
        """

        if not self._enable_save_config:
            return

        # Ensure key is always a tuple for the signal signature
        signal_key = (key,) if isinstance(key, str) else key

        if isinstance(value, bool):
            self.set_config_parameter[tuple, bool].emit(signal_key, value)
        elif isinstance(value, int):
            self.set_config_parameter[tuple, int].emit(signal_key, value)
        elif isinstance(value, float):
            self.set_config_parameter[tuple, float].emit(signal_key, value)
        elif isinstance(value, str):
            self.set_config_parameter[tuple, str].emit(signal_key, value)

    def _compute_number_samples(self) -> None:
        """
        Recalculate the total number of samples
        based on variables and trigger window.
        """

        if self._number_of_variables > 0:
            new_number_samples = int(
                (self._pre_trigger + self._post_trigger)
                * self._number_of_variables,
                )
        else:
            new_number_samples = 0

        if self._number_samples != new_number_samples:
            self._number_samples = new_number_samples
            self.update_f_min_max.emit()

    def _update_settling_samples(self) -> None:
        """ Convert settling time (seconds) into discrete samples. """

        self._settling_samples = int(
            self._settling_time * self._sampling_frequency
            )

    def _compute_pre_post_trigger_time(self) -> None:
        """
        Recompute and emit the physical time durations
        for pre- and post-trigger.
        """

        if (self._sampling_frequency is not None
                and self._pre_trigger is not None
                and self._post_trigger is not None):

            pre_trigger_time = self._pre_trigger / self._sampling_frequency
            post_trigger_time = self._post_trigger / self._sampling_frequency

            self.set_pre_trigger.emit(
                f'~{pre_trigger_time:.4e} s'.replace('.', ',')
                )
            self.set_post_trigger.emit(
                f'~{post_trigger_time:.4e} s'.replace('.', ',')
                )

    def is_ready(self) -> bool:
        """ Check if the trigger configuration is valid and ready to arm. """

        if self._type_str == 'immediate_t':
            return True

        is_valid_trigger = (
            (self._type_str == 'fra_t' or self._address > 0) and
            (self._pre_trigger + self._post_trigger) > 0 and
            self._max_number_samples > 0 and
            self._count > 0
        )
        return is_valid_trigger
