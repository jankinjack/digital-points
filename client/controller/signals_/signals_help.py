
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from digital_points import DigitalPoints

from controller.common import add_drag_handlers

def init_signals_help(dp: 'DigitalPoints') -> None:
    """ Init signal related to help. """

    add_drag_handlers(dp.help)

    def __on_about_to_quit() -> None:
        dp.interface.interface.disconnect_from_port()

    # Disconnect from interface before quit.
    dp.aboutToQuit.connect(__on_about_to_quit)
