
from typing import TYPE_CHECKING
from enum import IntEnum

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

from controller.common import add_drag_handlers, select_variable_in_table

if TYPE_CHECKING:
    from digital_points import DigitalPoints

class Page(IntEnum):
    """ Enumeration of available pages in the main stacked widget. """
    SCOPE = 1
    SETTINGS = 2
    FRA = 3
    LOG = 4
    MATH = 5


# The order in which pages are cycled when pressing 'Tab'
AVAILABLE_PAGES = (
    Page.SCOPE,
    Page.FRA,
    Page.MATH,
    Page.LOG,
    Page.SETTINGS,
)

FORBIDDEN_PAGES = set()


def init_signals_main(dp: 'DigitalPoints') -> None:
    """ Initialize and connect all Qt signals related to the main window. """

    dp.interface.update_scope_data.connect(dp.main.graph_scope.set_data)
    dp.interface.update_fra_data.connect(dp.main.graph_fra.set_data)

    # Automatically switch to FRA page when measurements finish.
    dp.interface.fra_finished.connect(
        lambda: dp.main.ui.pushButtonOpenScopeFRA.toggled.emit(True)
        )

    # Connect interface and trigger config signals to the JSON config manager
    for signal_type in (str, int, float, bool):
        dp.interface.set_config_parameter[tuple, signal_type].connect(
            dp.config.set_parameter
            )
        dp.interface.trigger.set_config_parameter[tuple, signal_type].connect(
            dp.config.set_parameter
            )

    dp.interface.trigger.set_sampling_frequency.connect(
        dp.fra_settings.ui.lineEditFmin.editingFinished
        )
    dp.interface.trigger.set_pre_trigger.connect(
        dp.main.ui.labelPreTriggerTime.setText
        )
    dp.interface.trigger.set_post_trigger.connect(
        dp.main.ui.labelPostTriggerTime.setText
        )
    dp.interface.trigger.update_f_min_max.connect(
        dp.fra_settings.ui.lineEditFmin.editingFinished
        )
    dp.interface.node_status_changed.connect(
        lambda state: dp.status_tracker.node_status('Linked' if state else 'Unlinked')
        )

    # Recalculate FRA limits when node connects.
    dp.interface.node_status_changed.connect(
        lambda state: dp.fra_settings.ui.lineEditFmin.editingFinished.emit() if state else None
        )

    def __on_change_number_of_lines(new_number: int) -> None:
        dp.interface.trigger.number_of_variables = new_number

    dp.main.graph_scope.number_lines_changed.connect(
        __on_change_number_of_lines
        )

    def __on_connect_toggled(checked: bool) -> None:
        """ Handle the main 'Connect/Disconnect' button. """

        if checked:
            signal = dp.fra_settings.graph_fra_excitation.lines[0].y_data

            # Force FRA configuration if trying to start Multi-Sine FRA
            # without an excitation signal.
            if (dp.interface.mode == 'FRA Mode'
                    and dp.interface.trigger.fra_excitation_type == 'Multi-Sine Excitation'
                    and (signal is None or len(signal) == 0)
                    and len(dp.main.graph_scope.axes[0].lines) == 1
                    and len(dp.main.graph_scope.axes[1].lines) == 1):
                dp.main.ui.pushButtonConfigureFRA.click()
                return

            dp.interface.connect_to_node(dp.main.graph_scope.share_objects)
        else:
            dp.interface.disconnect_from_node()

    dp.main.ui.pushButtonConnect.toggled.connect(__on_connect_toggled)

    def __on_page_changed(index: int) -> None:
        """ Handle page changes in the stackedWidget. """

        if dp.main.ui.stackedWidget.currentIndex() == index:
            return

        buttons = (
            dp.main.ui.pushButtonOpenScope,
            dp.main.ui.pushButtonOpenSettings,
            dp.main.ui.pushButtonOpenScopeFRA,
            dp.main.ui.pushButtonOpenLog,
            dp.main.ui.pushButtonOpenMath,
            )

        # Update button states: target button is checked
        # and disabled, others are enabled.
        for i, btn in enumerate(buttons):
            is_target = (i == index - 1)
            btn.setDisabled(is_target)
            btn.setChecked(is_target)

        if index == Page.SETTINGS:
            dp.main.ui.lineEditSearchVariable.setFocus()

        # Update the keyboard navigation tracker.
        if index in AVAILABLE_PAGES:
            dp.main._current_page_index = AVAILABLE_PAGES.index(index)

        dp.main.ui.stackedWidget.setCurrentIndex(index)

    # Connect page toggle buttons dynamically.
    page_buttons = (
        (dp.main.ui.pushButtonOpenScope, Page.SCOPE),
        (dp.main.ui.pushButtonOpenSettings, Page.SETTINGS),
        (dp.main.ui.pushButtonOpenScopeFRA, Page.FRA),
        (dp.main.ui.pushButtonOpenLog, Page.LOG),
        (dp.main.ui.pushButtonOpenMath, Page.MATH),
        )

    for btn, page_idx in page_buttons:
        btn.toggled.connect(
            lambda checked, idx=page_idx: __on_page_changed(idx) if checked else None
        )

    dp.main.ui.lineEditSearchVariable.textChanged.connect(
        lambda text: select_variable_in_table(
            dp.main.ui.tableWidgetVariables,
            text
            )
        )

    dp.main._current_page_index = 0

    def __on_tab_pressed() -> None:
        """ Handle 'Tab' key press to cycle through available pages. """

        dp.main._current_page_index = (dp.main._current_page_index + 1) % len(AVAILABLE_PAGES)
        target_page = AVAILABLE_PAGES[dp.main._current_page_index]

        if target_page not in FORBIDDEN_PAGES:
            __on_page_changed(target_page)
        else:
            __on_tab_pressed()  # Recursively skip forbidden pages

    dp.main.shortcut_tab.activated.connect(__on_tab_pressed)

    def __on_ctrl_tab_pressed() -> None:
        """ Handle 'Ctrl+Tab' to cycle through available COM ports. """

        combo = dp.com_settings.ui.comboBoxSerialPorts
        count = combo.count()

        if count <= 1:
            return

        index = (combo.currentIndex() + 1) % count

        # Skip index 0 if it represents '-- NONE --' or similar placeholder.
        if index == 0 and count > 1:
            index = 1

        combo.setCurrentIndex(index)

    dp.main.shortcut_ctrl_tab.activated.connect(__on_ctrl_tab_pressed)

    def __on_ctrl_space_pressed() -> None:
        """ Handle 'Ctrl+Space' to toggle the connection state. """

        dp.main.ui.pushButtonConnect.toggled.emit(
            not dp.main.ui.pushButtonConnect.isChecked()
            )

    dp.main.shortcut_ctrl_space.activated.connect(__on_ctrl_space_pressed)

    # Main app exit.
    dp.main.ui.pushButtonCloseApp.clicked.connect(dp.exit)

    # Dynamically connect close buttons
    # and Esc shortcuts for all secondary windows.
    windows_to_close = (
        dp.com_settings,
        dp.fra_settings,
        dp.variable_sel,
        dp.import_csv,
        dp.help,
        )

    for win in windows_to_close:
        win.ui.pushButtonCloseApp.clicked.connect(win.close)
        if hasattr(win, 'shortcut_esc'):
            win.shortcut_esc.activated.connect(win.close)

    dp.main.ui.pushButtonMinimizeApp.clicked.connect(dp.main.showMinimized)

    def _toggle_maximize(window: QWidget) -> None:
        """ Toggle between maximized and normal window states. """

        btn = window.ui.pushButtonMaximizeApp
        current_mode = getattr(btn, 'mode', 'Maximize')

        if current_mode == 'Maximize':
            window.showMaximized()
            icon_path = ':/icons/icons/icon_restore.png'
            btn.mode = 'Restore'
        else:
            window.showNormal()
            icon_path = ':/icons/icons/icon_maximize.png'
            btn.mode = 'Maximize'

        icon = QIcon()
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        btn.setIcon(icon)
        btn.setIconSize(QSize(28, 28))

    dp.main.ui.pushButtonMaximizeApp.mode = 'Maximize'
    dp.main.ui.pushButtonMaximizeApp.clicked.connect(
        lambda: _toggle_maximize(dp.main)
        )

    add_drag_handlers(dp.main)

    dp.main.ui.pushButtonHelp.clicked.connect(dp.help.show)
    dp.variable_sel.ui.pushButtonHelp.clicked.connect(dp.help.show)
