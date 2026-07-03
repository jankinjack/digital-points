
import math

import serial

from PySide6.QtWidgets import (
    QWidget, QMainWindow, QHeaderView, QMenu, QWidgetAction, QSizeGrip,
    QSizePolicy, QComboBox, QLineEdit, QGraphicsDropShadowEffect,
    QGraphicsView, QTableWidget,
)
from PySide6.QtCore import Qt, QTimer, QTranslator, QRegularExpression, QSize
from PySide6.QtGui import QRegularExpressionValidator, QKeySequence, QShortcut

import view.ui_form_main
import view.ui_form_com_settings
import view.ui_form_select_variables
import view.popups.ui_form_popup_table_variables
import view.ui_form_splash_screen
import view.ui_form_array_index_table_selected_variables
import view.ui_form_fra_settings
import view.ui_form_import_csv

import view.popups.ui_form_popup_scope
import view.popups.ui_form_popup_fra_scope
import view.popups.ui_form_popup_math_scope
import view.popups.ui_form_popup_fft_range
import view.popups.ui_form_popup_table_selected_variables
import view.popups.ui_form_popup_scope_cursor

import view.dialogs.ui_form_help

import info
from model.graph_view import GraphView


# Constants ans styles.


SHADOW_COLOR = '#8e8e93'

COMBO_BOX_STYLE = """
    QComboBox {
        background-color: white;
        border-radius: 0px;
        border: 0px solid grey;
        padding-left: 10px;
        height: 20px;
    }
    QComboBox:hover { border: 0px solid #7284b9; }
    QComboBox:disabled { border: 0px solid #7d7d7d; color: #7d7d7d; }
    QComboBox::drop-down {
        background-color: white;
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 28px; 
        border-left: 1px solid #D6CFC7;
        border-top-right-radius: 3px;
        background-image: url(:/icons/icons/icon_arrow_bottom.png);
        border-bottom-right-radius: 3px;
        background-position: center;
        background-repeat: no-repeat;
    }
    QComboBox::drop-down:disabled { background-color: #aaaaaa; border-left-color: #aaaaaa; }
    QComboBox::drop-down:hover { background-color: #d1eeff; }
    QComboBox::drop-down:on { background-image: url(:/icons/icons/icon_arrow_top.png); }
    QComboBox QAbstractItemView {
        background-color: white;
        selection-background-color: #adc9ff;
        selection-color: #212121;
        height: 20px;
        outline: 0;
    }
"""

LINE_EDIT_STYLE = """
    QLineEdit {
        color: black;
        background-color: white;
        border: 0px;
        padding-left: 3px;
    }
"""


# Helper functions.


def _apply_shadows(widgets: list[QWidget]) -> list[QGraphicsDropShadowEffect]:
    """ Apply a standard drop shadow effect to a list of widgets. """

    shadows = []

    for widget in widgets:
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(7)
        shadow.setColor(SHADOW_COLOR)
        shadow.setOffset(1)
        widget.setGraphicsEffect(shadow)
        shadows.append(shadow)

    return shadows


def _disable_wheel_events(widgets: list[QWidget]) -> None:
    """
    Disable mouse wheel events for a list of widgets
    to prevent accidental value changes.
    """

    for widget in widgets:
        widget.wheelEvent = lambda e: e.ignore()


def _resize_table_columns(
        table_widget: QTableWidget,
        column_count: int
        ) -> None:
    """
    Resize specified number of columns in a table
    to fit their contents.
    """

    header = table_widget.horizontalHeader()
    for i in range(column_count):
        header.setSectionResizeMode(i, QHeaderView.ResizeToContents)


# Base classes.


class BaseFramelessWindow(QMainWindow):
    """
    Base class providing common functionality
    for all frameless application windows.
    """

    def _setup_frameless(self, window_flag: Qt.WindowType = Qt.Window) -> None:
        """Configure window flags for a frameless modal appearance."""

        self.setWindowFlags(self.windowFlags() | window_flag | Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)

    def _add_size_grip(self, layout) -> None:
        """ Add a size grip to the specified layout for window resizing. """

        self.qsize_grip = QSizeGrip(self)
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.qsize_grip.sizePolicy().hasHeightForWidth())
        self.qsize_grip.setSizePolicy(size_policy)

        layout.addWidget(self.qsize_grip)

    def _add_esc_shortcut(self) -> None:
        """ Add a shortcut to close the window with the Esc key. """

        self.shortcut_esc = QShortcut(QKeySequence('Esc'), self)


class UiPopup(QMenu):
    """ Custom popup menu class for embedding widgets. """

    def __init__(self, ui_form: 'Ui_Form', parent=None) -> None:
        super().__init__(parent)

        self.main_widget = QWidget()
        self.ui_form = ui_form

        self._load_ui()

    def _load_ui(self) -> None:
        """ Initialize and configure the popup UI. """

        self.setWindowFlags(self.windowFlags() | Qt.Popup | Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)

        self.ui = self.ui_form.Ui_Form()
        self.ui.setupUi(self.main_widget)

        self.main_action = QWidgetAction(self)
        self.main_action.setDefaultWidget(self.main_widget)
        self.addAction(self.main_action)


class UiSplashScreen(QMainWindow):
    """ Splash screen window displayed during application startup. """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._load_ui()

    def _load_ui(self) -> None:
        """" Initialize and configure the splash screen UI. """

        self.setWindowFlags(self.windowFlags() | Qt.SplashScreen | Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)

        self.ui = view.ui_form_splash_screen.Ui_Window_Main()
        self.ui.setupUi(self)


class UiMainWindow(BaseFramelessWindow):
    """ Main application window containing graphs, logs, and controls. """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.timer_graph_update = QTimer()

        self.pos_mouse_pressed = None
        self._load_ui()

    def _load_ui(self) -> None:
        """ Initialize and configure the main window UI. """

        self._setup_frameless(Qt.Window)

        self.ui = view.ui_form_main.Ui_Window_Main()
        self.ui.setupUi(self)

        self.ui.graphScope.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)

        # Initialize graph views.
        self.graph_scope = GraphView(
            widget=self.ui.graphScope, axes_num=2,
            x_scale='linear', x_unit='s',
            enable_cursors=True,
            )
        self.graph_fra = GraphView(
            widget=self.ui.graphFRA, axes_num=2,
            x_scale='log', x_unit='Hz',
            enable_cursors=True,
            )
        self.graph_math = GraphView(
            widget=self.ui.graphMath, axes_num=2,
            x_scale='log', x_unit='Hz',
            enable_cursors=True,
            )

        self.translator = QTranslator()

        self._add_size_grip(self.ui.horizontalLayoutBottomFrame)

        # Configure table headers.
        _resize_table_columns(self.ui.tableWidgetVariables, 3)
        _resize_table_columns(self.ui.tableWidgetLog, 3)
        _resize_table_columns(self.ui.tableWidgetNumbers, 7)

        # Set application version labels
        self.ui.labelVersion.setText(f'| v{info.__version__}')
        self.ui.labelCurrentVersion.setText(info.__version__)

        # Disable mouse wheel scrolling for input widgets.
        _disable_wheel_events([
            self.ui.spinBoxNodeAddr, self.ui.comboBoxMode,
            self.ui.spinBoxDumpSize, self.ui.spinBoxSampleCount,
            self.ui.doubleSpinBoxTriggerLevel, self.ui.spinBoxPreTrigger,
            self.ui.spinBoxTriggerCount, self.ui.doubleSpinBoxSettlingTime,
            self.ui.comboBoxLanguage,
        ])

        # Initialize popup menus.
        self.popup_scope = UiPopup(view.popups.ui_form_popup_scope)
        self.popup_scope_cursor = (
            UiPopup(view.popups.ui_form_popup_scope_cursor),
            UiPopup(view.popups.ui_form_popup_scope_cursor),
            )
        self.popup_fra_scope = UiPopup(view.popups.ui_form_popup_fra_scope)
        self.popup_fft_scope = UiPopup(view.popups.ui_form_popup_fft_range)
        self.popup_math_scope = UiPopup(view.popups.ui_form_popup_math_scope)
        self.popup_table_variables = UiPopup(view.popups.ui_form_popup_table_variables)

        # Setup regular expression validators for numeric inputs.
        float_validator = QRegularExpressionValidator(
            QRegularExpression(r'[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)')
            )
        self.popup_fft_scope.ui.lineEditXmin.setValidator(float_validator)
        self.popup_fft_scope.ui.lineEditXmax.setValidator(float_validator)
        for cursor_popup in self.popup_scope_cursor:
            cursor_popup.ui.lineEditXCursor1.setValidator(float_validator)
            cursor_popup.ui.lineEditXCursor2.setValidator(float_validator)

        self.ui.lineEditSamplingFrequency.setValidator(float_validator)
        self.ui.lineEditCrossFrequency.setValidator(float_validator)
        self.ui.lineEditPhaseMargin.setValidator(float_validator)
        self.ui.lineEditKCorrection.setValidator(float_validator)
        self.ui.lineEditPhiCorrection.setValidator(float_validator)

        # Populate the numbers table.
        self._setup_numbers_table()

        # Enable word wrapping and auto-resizing for the logger table.
        self.ui.tableWidgetLog.setWordWrap(True)
        self.ui.tableWidgetLog.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
            )

        # Define keyboard shortcuts.
        self.shortcut_tab = QShortcut(QKeySequence('Tab'), self)
        self.shortcut_ctrl_tab = QShortcut(QKeySequence('Ctrl+Tab'), self)
        self.shortcut_ctrl_space = QShortcut(QKeySequence('Ctrl+Space'), self)

        # Apply drop shadow effects to UI frames.
        self.shadow_list = _apply_shadows([
            self.ui.frameLineCom, self.ui.frameLineGraphsMeas,
            self.ui.frameLineTrigger, self.ui.frameLineRTM,
            self.ui.frameLineFRA, self.ui.frameLineUpdate,
            self.ui.frameLineSystem, self.ui.frameLineVariables,
            self.ui.frameControlParameters, self.ui.frameControlSynthesis,
            self.ui.tableWidgetLog ,
        ])

    def _setup_numbers_table(self) -> None:
        """ Populate the numbers table with combo boxes and line edits. """

        num_rows = 4
        self.ui.tableWidgetNumbers.setRowCount(num_rows)

        for i in range(num_rows):
            # Variable selection combo box (Column 0).
            combo_box = QComboBox()
            combo_box.setStyleSheet(COMBO_BOX_STYLE)
            combo_box.setMinimumSize(QSize(16777215, 24))
            combo_box.setMaximumSize(QSize(16777215, 24))
            combo_box.setSizeAdjustPolicy(QComboBox.AdjustToContents)
            combo_box.wheelEvent = lambda e: e.ignore()
            self.ui.tableWidgetNumbers.setCellWidget(i, 0, combo_box)

            # Write limits line edits (Columns 6 and 7).
            for col in (6, 7):
                line_edit = QLineEdit()
                line_edit.setStyleSheet(LINE_EDIT_STYLE)
                line_edit.setMinimumSize(QSize(120, 24))
                line_edit.setMaximumSize(QSize(120, 24))
                line_edit.setDisabled(True)
                self.ui.tableWidgetNumbers.setCellWidget(i, col, line_edit)
                self.ui.tableWidgetNumbers.horizontalHeader().setSectionResizeMode(
                    col, QHeaderView.ResizeToContents
                )

            # Variable name line edit (Column 8).
            line_edit = QLineEdit()
            line_edit.setStyleSheet(LINE_EDIT_STYLE)
            line_edit.setDisabled(True)
            line_edit.setMinimumSize(QSize(16777215, 24))
            line_edit.setMaximumSize(QSize(16777215, 24))
            self.ui.tableWidgetNumbers.setCellWidget(i, 8, line_edit)


class UiComSettingsWindow(BaseFramelessWindow):
    """ Window for configuring serial communication settings. """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.timer_update = QTimer()
        self.timer_update.setSingleShot(False)

        self._load_ui()

    def _load_ui(self) -> None:
        """ Initialize and configure the COM settings UI. """

        self._setup_frameless(Qt.Tool)

        self.ui = view.ui_form_com_settings.Ui_MainWindow()
        self.ui.setupUi(self)

        self._add_size_grip(self.ui.horizontalLayout_6)

        # Populate serial configuration combo boxes.
        for baudrate in serial.Serial.BAUDRATES:
            self.ui.comboBoxSerialBaudrate.addItem(str(baudrate))
        for bytesize in serial.Serial.BYTESIZES:
            self.ui.comboBoxSerialDataBits.addItem(str(bytesize))
        for parity in serial.PARITY_NAMES.values():
            self.ui.comboBoxSerialParity.addItem(parity)
        for stop_bits in serial.Serial.STOPBITS:
            self.ui.comboBoxSerialStopBits.addItem(str(stop_bits))

        self.shadow_list = _apply_shadows([
            self.ui.frameLine_1, self.ui.frameLine_2,
            ])
        self._add_esc_shortcut()


class UiSelectVariablesWindow(BaseFramelessWindow):
    """ Window for selecting variables to monitor or log. """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._load_ui()

    def _load_ui(self) -> None:
        """ Initialize and configure the variable selection UI. """

        self._setup_frameless(Qt.Window)

        self.ui = view.ui_form_select_variables.Ui_Window_Main()
        self.ui.setupUi(self)

        self._add_size_grip(self.ui.horizontalLayout)

        _resize_table_columns(self.ui.tableWidgetVariables, 3)
        _resize_table_columns(self.ui.tableWidgetVariableSelected_1, 3)
        _resize_table_columns(self.ui.tableWidgetVariableSelected_2, 3)

        self.popup_selected_variables = (
            UiPopup(view.popups.ui_form_popup_table_selected_variables),
            UiPopup(view.popups.ui_form_popup_table_selected_variables),
        )

        self.popup_choose_array_index = (
            UiPopup(view.ui_form_array_index_table_selected_variables),
            UiPopup(view.ui_form_array_index_table_selected_variables),
        )

        self.shadow_list = _apply_shadows([
            self.ui.frameLine_1, self.ui.frameLineGraph1,
            self.ui.frameLineGraph2,
        ])
        self._add_esc_shortcut()


class UiFRASettingsWindow(BaseFramelessWindow):
    """ Window for configuring Frequency Response Analysis (FRA) settings. """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._load_ui()

    def _load_ui(self) -> None:
        """ Initialize and configure the FRA settings UI. """

        self._setup_frameless(Qt.Tool)

        self.ui = view.ui_form_fra_settings.Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize FRA graph views.
        self.graph_fra_config = GraphView(
            widget=self.ui.graphFRAConfig, axes_num=1, x_scale='log',
            x_unit='Hz', enable_y2=False, enable_cursors=True,
            selectable_points=True,
        )
        self.graph_fra_config.add_line(
            axis=0, name='Amplitudes of Excitation', type_='float32_t',
            address=0, y_axis='y',
            show_symbols=True, drag_limits=(0, math.inf),
        )

        self.graph_fra_excitation = GraphView(
            widget=self.ui.graphFRAExcitation, axes_num=1, x_unit='s',
            enable_y2=False, enable_cursors=True,
        )
        self.graph_fra_excitation.add_line(
            axis=0, name='Excitation Signal', type_='float32_t',
            address=0, y_axis='y',
        )

        self._add_size_grip(self.ui.horizontalLayout_6)

        # Setup validators for FRA numeric inputs.
        float_validator = QRegularExpressionValidator(
            QRegularExpression(r'[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)')
        )
        self.ui.lineEditFmin.setValidator(float_validator)
        self.ui.lineEditFmax.setValidator(float_validator)
        self.ui.lineEditAmplitude.setValidator(float_validator)

        int_validator = QRegularExpressionValidator(
            QRegularExpression(r'^[1-9][0-9]*$')
            )
        self.ui.lineEditRepeat.setValidator(int_validator)
        self.ui.lineEditNfreq.setValidator(int_validator)

        self.shadow_list = _apply_shadows([self.ui.frame])
        self._add_esc_shortcut()


class UiHelpWindow(BaseFramelessWindow):
    """ Help and documentation window. """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._load_ui()

    def _load_ui(self) -> None:
        """ Initialize and configure the help UI. """

        self._setup_frameless(Qt.Tool)

        self.ui = view.dialogs.ui_form_help.Ui_MainWindow()
        self.ui.setupUi(self)

        self._add_size_grip(self.ui.horizontalLayout_6)
        self.shadow_list = _apply_shadows([self.ui.frame_1])
        self._add_esc_shortcut()


class UiImportCSVWindow(BaseFramelessWindow):
    """ Window for importing CSV data files. """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._load_ui()

    def _load_ui(self) -> None:
        """ Initialize and configure the CSV import UI. """

        self._setup_frameless(Qt.Window)

        self.ui = view.ui_form_import_csv.Ui_Window_Main()
        self.ui.setupUi(self)

        self._add_size_grip(self.ui.horizontalLayout)

        _resize_table_columns(self.ui.tableWidgetVariables, 1)
        _resize_table_columns(self.ui.tableWidgetVariableSelected_1, 3)
        _resize_table_columns(self.ui.tableWidgetVariableSelected_2, 3)

        self.shadow_list = _apply_shadows([
            self.ui.frameLine_1, self.ui.frameLineGraph1,
            self.ui.frameLineGraph2,
        ])
        self._add_esc_shortcut()
