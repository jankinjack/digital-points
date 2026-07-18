
import shutil
from typing import Self, Optional
from contextlib import suppress
from pathlib import Path
import logging
from datetime import datetime

from PySide6.QtWidgets import QLabel, QTableWidget, QTableWidgetItem, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QCoreApplication

import __main__


LOG_DIR_NAME = 'log'
ENABLE_CMD = 'LOG ENABLE'
DISABLE_CMD = 'LOG DISABLE'

LOG_LEVEL_COLOR = {
    'CRITICAL': '#ED1941',
    'ERROR': '#ED1941',
    'WARNING': '#FA8128',
    'INFO': '#74B72E',
    'DEBUG': '#30B5C8',
    'NOTSET': '#FFFFFF',
    }

BUTTON_STYLE_TEMPLATE = """
    QPushButton {{
        min-width: 80px;
        max-width: 80px;
        min-height: 20px;
        max-height: 20px;
        background-color: {color};
        border: none;
        border-radius: 10px;
        color: #f8f8f2;
    }}
"""

LOG_FILE_HEADER = (
    f"{'[Timestamp]':<19}\t"
    f"{'[Module]':<20}\t\t"
    f"{'[Type]':<8}\t\t"
    f"{'[Message]'}\n"
)


class LogHandler(logging.Handler):
    """
    Custom logging handler that routes log records to a Qt GUI 
    (QLabel and QTableWidget) and simultaneously writes them
    to a daily text file.
    """

    __slots__ = (
        '_label_messages',
        '_table_messages',
        '_text_messages',
        '_is_enabled',
        '_log_dir',
        )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._log_dir = __main__.FULL_PATH / 'log'

        # Clear previous logs on startup to keep the environment clean
        with suppress(FileNotFoundError, OSError):
            shutil.rmtree(self._log_dir)

        self._log_dir.mkdir(exist_ok=True)
        self._is_enabled = False
        self._label_messages = None
        self._table_messages = None

    def emit(self, record: logging.LogRecord) -> None:
        """ Process a log record: update GUI and write to file if enabled. """

        # Handle remote enable/disable commands via specific debug messages
        if record.levelno == logging.DEBUG:
            if record.msg == ENABLE_CMD:
                self._is_enabled = True
                return
            elif record.msg == DISABLE_CMD:
                self._is_enabled = False
                return

        if not self._is_enabled:
            return

        timestamp = datetime.now()
        time_str = timestamp.strftime('%d-%m-%Y %H:%M:%S')

        # Update the quick-view label
        if self._label_messages is not None:
            formatted_msg = self.format(record).strip()
            self._label_messages.setText(
                QCoreApplication.translate('Window_Main', formatted_msg, None)
            )

        # Update the detailed log table
        if self._table_messages is not None:
            self._table_messages.insertRow(0)
            self._table_messages.setItem(0, 0, QTableWidgetItem(time_str))
            self._table_messages.setItem(0, 2, QTableWidgetItem(record.msg.strip()))

            # Create a styled push button to represent the log level
            color = LOG_LEVEL_COLOR.get(record.levelname, LOG_LEVEL_COLOR['NOTSET'])
            push_button = QPushButton(record.levelname)
            push_button.setStyleSheet(BUTTON_STYLE_TEMPLATE.format(color=color))

            # Wrap the button in a widget to center it within the table cell.
            push_button_widget = QWidget()
            push_button_layout = QVBoxLayout(push_button_widget)
            push_button_layout.addWidget(push_button)
            push_button_layout.setAlignment(Qt.AlignCenter)
            push_button_layout.setContentsMargins(0, 0, 10, 0)

            self._table_messages.setCellWidget(0, 1, push_button_widget)

        file_path = self._log_dir / f"log_{timestamp.strftime('%d-%m-%Y')}.log"
        file_exists = file_path.is_file()

        try:
            with file_path.open('a', encoding='utf-8') as log_file:
                if not file_exists:
                    log_file.write(LOG_FILE_HEADER)

                log_file.write(
                    f"{time_str:<19}\t"
                    f"{record.module:<20}\t\t"
                    f"{record.levelname:<8}\t\t"
                    f"{record.message}\n"
                )
        except OSError:
            # Fail silently if the file system is unavailable or locked.
            pass

    def set_widgets(self, label: QLabel, table: QTableWidget) -> None:
        """ Bind the Qt widgets that will display the log messages. """

        self._label_messages = label
        self._table_messages = table

    def get_logger(self) -> logging.Logger:
        """ Retrieve and configure the application-wide logger instance. """

        logger = logging.getLogger('logger')
        logger.setLevel(logging.DEBUG)
        
        # Prevent adding multiple handlers
        # if get_logger is called repeatedly.
        if self not in logger.handlers:
            logger.addHandler(self)

        return logger

class StatusTracker():
    """
    Singleton class for tracking and displaying application status 
    on the main window's status bar labels.
    """

    __slots__ = (
        '_label_status',
        '_label_node_status',
        '_label_progress',
        '_is_initialized',
        )
    __instance = None

    def __new__(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self) -> None:
        # Prevent re-initialization of the Singleton instance
        if getattr(self, '_is_initialized', False):
            return

        self._label_status = None
        self._label_node_status = None
        self._label_progress = None
        self._is_initialized = True

    def _update_label(self, label: Optional[QLabel], text: str) -> None:
        """ Helper to safely update a QLabel with translated text. """

        if label is not None:
            label.setText(
                QCoreApplication.translate('Window_Main', text, None)
                )

    def set_widgets(
            self,
            label_status: QLabel,
            label_node_status: QLabel,
            label_progress: QLabel
            ) -> None:

        self._label_status = label_status
        self._label_node_status = label_node_status
        self._label_progress = label_progress

    def status(self, new_status: str) -> None:
        """ Update the general application status. """

        self._update_label(self._label_status, new_status)

    def node_status(self, new_node_status: str) -> None:
        """ Update the microcontroller node connection status. """

        self._update_label(self._label_node_status, new_node_status)

    def progress(self, new_progress: str) -> None:
        """ Update the current operation progress (e.g., FRA sweep). """

        self._update_label(self._label_progress, new_progress)
