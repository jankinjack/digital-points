
from typing import Self, Optional

from watchdog.observers import Observer

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtCore import QTimer

import info
from view.ui_windows import (
    UiSplashScreen,
    UiMainWindow,
    UiComSettingsWindow,
    UiSelectVariablesWindow,
    UiFRASettingsWindow,
    UiHelpWindow,
    UiImportCSVWindow,
    )
from model.interface.interface_base import InterfaceBase
from controller.signals import init_signals
from controller.default import init_default
from model.json_config import JSON_Config
from model.loggers import LogHandler, StatusTracker


class DigitalPoints(QApplication):
    """
    Main application class for Digital Points.
    Implements the Singleton pattern to ensure only one instance exists.
    """

    __slots__ = (
        '_is_initialized',
        'interface',
        'splash_screen',
        'main',
        'com_settings',
        'variable_sel',
        'fra_settings',
        'import_csv',
        'logger',
        'status_tracker',
        'config',
        'help',
        'elf_watchdog',
        )
    __instance = None

    def __new__(cls, *args, **kwargs) -> Self:
        """ Create and return the single instance of the application. """

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, *args, **kwargs) -> None:
        # Prevent re-initialization of the Singleton instance
        if getattr(self, '_is_initialized', False):
            return

        super().__init__(*args, **kwargs)
        self._is_initialized = True

        self.setApplicationVersion(info.__version__)

        # Initialize core components and UI.
        self.interface = InterfaceBase(self)
        self._load_fonts()
        self._load_ui_windows()

        # Setup controllers and default states.
        init_signals(self)
        init_default(self)

        # Start the application sequence.
        self.main.show()
        self.splash_screen.close()

        # Start background tasks.
        self.com_settings.timer_update.start(200)
        self.main.timer_graph_update.start(15)
        self.interface.thread_.start()

        self.logger.debug('LOG ENABLE')

    def _load_fonts(self) -> None:
        """ Load custom application fonts and set the default font. """

        mono_font_id = QFontDatabase.addApplicationFont(":/fonts/fonts/DroidSansMono.ttf")
        if mono_font_id != -1:
            font_families = QFontDatabase.applicationFontFamilies(mono_font_id)
            if font_families:
                self.setFont(QFont(font_families[0]))

        # Load secondary font (e.g., for fallback or specific UI elements)
        QFontDatabase.addApplicationFont(":/fonts/fonts/DroidSans.ttf")

    def _load_ui_windows(self) -> None:
        """ Initialize and configure all GUI windows and core services. """

        # Splash Screen.
        self.splash_screen = UiSplashScreen()
        self.set_window_geometry_and_center(self.splash_screen)
        self.splash_screen.show()

        # Main Window.
        self.main = UiMainWindow()
        self.set_window_geometry_and_center(self.main, 2/3)

        # Settings & Configuration Windows.
        self.com_settings = UiComSettingsWindow(self.main)
        self.set_window_geometry_and_center(self.com_settings, 1/3)

        self.variable_sel = UiSelectVariablesWindow(self.main)
        self.set_window_geometry_and_center(self.variable_sel, 1/2)

        self.fra_settings = UiFRASettingsWindow(self.main)
        self.set_window_geometry_and_center(self.fra_settings, 1/2)

        self.import_csv = UiImportCSVWindow(self.main)
        self.set_window_geometry_and_center(self.import_csv, 1/3)

        self.help = UiHelpWindow(self.main)
        self.set_window_geometry_and_center(self.help, 1/2)

        # Logger Setup.
        logger_handler = LogHandler()
        logger_handler.set_widgets(
            self.main.ui.labelLog,
            self.main.ui.tableWidgetLog
            )
        self.logger = logger_handler.get_logger()

        # Status Tracker Setup.
        self.status_tracker = StatusTracker()
        self.status_tracker.set_widgets(
            self.main.ui.labelStatus,
            self.main.ui.labelNodeStatus,
            self.main.ui.labelProgress,
            )

        # Configuration Manager.
        self.config = JSON_Config()

        self.elf_watchdog = {
            'observer': Observer(),
            'timer': QTimer(),
            }
        self.elf_watchdog['observer'].start()
        self.elf_watchdog['timer'].setSingleShot(True)

    def set_window_geometry_and_center(
            self,
            window,
            proportion: Optional[float] = None
            ) -> None:
        """
        Resize the window based on a screen proportion and center it.
        Handles multi-monitor setups correctly by using the window's
        current screen.
        """

        # Fallback to primary screen
        # if the window's screen is not yet available.
        available_geometry = self.primaryScreen().availableGeometry()
        screen_width = available_geometry.width()
        screen_height = available_geometry.height()

        if proportion is not None:
            window.resize(
                int(screen_width * proportion),
                int(screen_height * proportion)
                )

        # Center the window on the available screen geometry.
        frame_geometry = window.frameGeometry()
        center = window.screen().availableGeometry().center()
        frame_geometry.moveCenter(center)
        window.move(frame_geometry.topLeft())
