
from typing import TYPE_CHECKING, Callable

from controller.signals_.signals_main import init_signals_main
from controller.signals_.signals_scope import init_signals_scope
from controller.signals_.signals_settings import init_signals_settings
from controller.signals_.signals_com_settings import init_signals_com_settings
from controller.signals_.signals_select_variables import init_signals_select_variables
from controller.signals_.signals_fra_settings import init_signals_fra_settings
from controller.signals_.signals_math import init_signals_math
from controller.signals_.signals_numbers import init_signals_numbers
from controller.signals_.signals_help import init_signals_help
from controller.signals_.signals_import_csv import init_signals_import_csv

if TYPE_CHECKING:
    from digital_points import DigitalPoints

# A centralized registry of all signal initialization functions.
# Adding a new window/module only requires appending
# its initializer to this tuple.
SIGNAL_INITIALIZERS: tuple[Callable[['DigitalPoints'], None], ...] = (
    init_signals_main,
    init_signals_scope,
    init_signals_settings,
    init_signals_com_settings,
    init_signals_select_variables,
    init_signals_fra_settings,
    init_signals_math,
    init_signals_numbers,
    init_signals_help,
    init_signals_import_csv,
)


def init_signals(dp: 'DigitalPoints') -> None:
    """
    Initialize and connect all Qt signals
    and slots across the application's UI modules.

    Args:
        dp: The main DigitalPoints application instance.
    """

    for initializer in SIGNAL_INITIALIZERS:
        initializer(dp)
