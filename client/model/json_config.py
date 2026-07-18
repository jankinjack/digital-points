import copy
from functools import reduce
import operator
from typing import Any, Optional, Self
from pathlib import Path
from contextlib import suppress
import collections

import orjson

from PySide6.QtCore import Slot, QObject

import __main__


# Default application configuration.
DEFAULT_CONFIG = {
    'language': 1,
    'elf-file': {
        'path': '',
        'mtime': 0.0,
    },
    'save-selection': True,
    'selected-lines': [],
    'last-dir': '',
    'interface': {
        'type': 'serial',
        'serial': {
            'baudrate': 115200,
            'bytesize': 8,
            'parity': 'None',
            'stopbits': 1.0,
            'port': '',
        },
        'can': {
            'bus_type': 'robotell',
            'bitrate': 500000,
            'baudrate': 115200,
            'id': 1,
            'port': '',
            'extended_id': False,
        }
    },
    'node address': 0,
    'mode': 'Real-Time Mode',
    'sampling frequency': 0,
    'sample count': 1,
    'rtm': {
        'dump_size_mb': 0,
    },
    'trigger': {
        'selected-line': {
            'name': '',
            'index': None,
        },
        'edge': 'Leading Edge',
        'one_shot_mode': False,
        'level': 0.0,
        'pre_trigger': 0,
        'post_trigger': 100,
        'samples number': 0,
        'count': 1,
        'settling time': 0.0,
    },
    'math': {
        'k_corr': '0',
        'phi_corr': '0',
        'f_s': '100e3',
        'f_c': '1000',
        'phi_m': '60',
    },
    'fra': {
        'frequency min': '100',
        'frequency max': '50000',
        'frequency count': '20',
        'amplitude': '0.1',
        'repeat': '1',
        'average type': 'Vector Averaging',
        'excitation type': 'Single-Sine Excitation',
    },
    'measurement': {
        'delta': True,
        'min': True,
        'max': True,
        'rms': False,
        'mean': False,
        'crest factor': False,
    }
}


class JSON_Config(QObject):
    """
    Singleton class for managing the application's JSON configuration file.
    Provides methods to safely read, write,
    and update nested configuration parameters.
    """

    __slots__ = (
        '_file_path',
        '_enable',
        '_config',
        '_is_initialized',
        )
    __instance = None

    def __new__(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self) -> None:
        # Prevent re-initialization of the Singleton instance, which would 
        # otherwise wipe out loaded user settings and reset '_enable' to False.
        if getattr(self, '_is_initialized', False):
            return

        super().__init__()

        self._file_path = __main__.FULL_PATH / 'config.json'
        self._enable = False

        # Deepcopy prevents accidental mutation of the global DEFAULT_CONFIG.
        self._config = copy.deepcopy(DEFAULT_CONFIG)
        self._is_initialized = True

    @property
    def enable(self) -> bool:
        return self._enable

    @enable.setter
    def enable(self, enable: bool) -> None:
        self._enable = enable

    @staticmethod
    def _get_by_path(root: dict, keys: tuple[str, ...]) -> Any:
        """ Access a nested object in root by a sequence of keys. """

        return reduce(operator.getitem, keys, root)

    @staticmethod
    def _set_by_path(root: dict, keys: tuple[str, ...], value: Any) -> None:
        """ Set a value in a nested object in root by a sequence of keys. """

        # If keys[:-1] is empty, it means the target key is at the root level.
        parent_dict = reduce(operator.getitem, keys[:-1], root) if keys[:-1] else root
        parent_dict[keys[-1]] = value

    @staticmethod
    def _deep_update(dest: dict, src: dict) -> dict:
        """
        Recursively update a nested dictionary.
        Only updates keys that already exist in the destination dictionary
        to prevent garbage data from corrupted config files.
        """

        for k, v in src.items():
            if k in dest:
                if isinstance(v, dict) and isinstance(dest[k], dict):
                    JSON_Config._deep_update(dest[k], v)
                else:
                    dest[k] = v
        return dest

    @Slot(str)
    @Slot(int)
    @Slot(float)
    @Slot(bool)
    def set_parameter(
            self,
            keys: tuple[str, ...],
            value: Optional[str | int | float | bool],
            ) -> None:
        """ Update a configuration parameter and save it to the file. """

        if not self._enable:
            return

        self._set_by_path(self._config, keys, value)
        self.save_config(self._file_path)

    def get_parameter(self, keys: tuple[str, ...]) -> Any:
        """ Retrieve a specific configuration parameter. """

        return self._get_by_path(self._config, keys)

    def get_config(self, load_file: bool = False) -> dict:
        """ Return the current configuration dictionary. """

        if load_file:
            self.load_config(self._file_path)

        return self._config

    def load_config(self, file_path: Path) -> None:
        """ Load data from the config file. """

        with (suppress(FileNotFoundError, orjson.JSONDecodeError, OSError),
                Path(file_path).open('r', encoding='utf-8') as read_file):
            data = read_file.read()

            if not data:
                return

            loaded_config = orjson.loads(data)
            self._deep_update(self._config, loaded_config)

    def save_config(self, file_path: Path) -> None:
        """ Serialize and save the current configuration to a JSON file. """

        if not self._enable:
            return

        with (suppress(OSError),
                Path(file_path).open('w', encoding='utf-8') as write_file):

            # Use OPT_INDENT_2 to make the saved JSON file human-readable.
            data = orjson.dumps(self._config, option=orjson.OPT_INDENT_2)
            write_file.write(data.decode('utf-8'))
