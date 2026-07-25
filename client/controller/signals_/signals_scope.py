
import datetime
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QGraphicsItem,
    QTableWidgetItem
    )
from PySide6.QtCore import Qt, QCoreApplication

import pyqtgraph as pg
import pyqtgraph.exporters

from model.fra.fft import FFT
from model.line import Line
from model.frame_rate_tracker import FrameRateTracker

if TYPE_CHECKING:
    from digital_points import DigitalPoints
    from model.graph_view import GraphView


def init_signals_scope(dp: 'DigitalPoints') -> None:
    """
    Initialize and connect all Qt signals
    related to the oscilloscope views.
    """

    def __on_axis_clicked(event, graph, popup) -> None:
        """ Handle right-click on graph axes to show context menus. """

        if (event.button() == Qt.MouseButton.RightButton
                and not dp.interface.is_started()):
            if not any([axis.right_click for axis in graph.axes]):
                popup.popup(event._screenPos)
            else:
                for axis in graph.axes:
                    axis.right_click = False

            event.accept()
        else:
            event.ignore()

    # Connect context menu signals to all graph views.
    dp.main.ui.graphScope.scene().sigMouseClicked.connect(
        lambda event: __on_axis_clicked(
            event,
            dp.main.graph_scope,
            dp.main.popup_scope
            )
        )
    dp.main.ui.graphFRA.scene().sigMouseClicked.connect(
        lambda event: __on_axis_clicked(
            event,
            dp.main.graph_fra,
            dp.main.popup_fra_scope
            )
        )
    dp.main.ui.graphMath.scene().sigMouseClicked.connect(
        lambda event: __on_axis_clicked(
            event,
            dp.main.graph_math,
            dp.main.popup_math_scope
            )
        )

    def __on_cursors_clicked(event, axis, popup) -> None:
        """ Handle right-click on cursors to show coordinate editing popup. """

        if event.button() == Qt.MouseButton.RightButton:
            # Block the axis's right-click handler to prevent menu conflict.
            axis.right_click = True

            # Initialize line-edits with current cursor x-coordinates.
            popup.ui.lineEditXCursor1.setText(f'{axis.cursors[0].x():.6g}')
            popup.ui.lineEditXCursor2.setText(f'{axis.cursors[1].x():.6g}')

            popup.popup(event._screenPos)

            event.accept()
        else:
            event.ignore()

    # Connect cursor click handlers for all axes in the scope view.
    for axis in dp.main.graph_scope.axes:
        for j, cursor in enumerate(axis.cursors):
            popup = dp.main.popup_scope_cursor[j]
            line_edit = (
                popup.ui.lineEditXCursor1,
                popup.ui.lineEditXCursor2
                )[j]

            cursor.sigClicked.connect(
                lambda _, event, axis=axis, popup=popup: __on_cursors_clicked(
                    event, axis, popup
                    )
                )

            def __on_cursor_moved_manually(popup, cursor, text: str) -> None:
                """ Handle manual cursor position input via line-edit. """

                popup.close()

                cursor.setPos(float(text))
                cursor.sigDragged.emit(cursor)
                cursor.label.valueChanged()

            line_edit.editingFinished.connect(
                lambda cursor=cursor, line_edit=line_edit, popup=popup:
                    __on_cursor_moved_manually(
                        popup, cursor, line_edit.text()
                        )
                )

    def __on_button_compute_fft() -> None:
        """ Show FFT configuration popup. """

        dp.main.popup_scope.close()
        dp.main.popup_fft_scope.popup(dp.main.popup_scope.pos())

    def __on_compute_fft() -> None:
        """ Compute FFT for all visible lines and display results in FRA view. """

        dp.main.popup_fft_scope.close()

        data = []
        num_lines = len(dp.main.graph_scope.lines)
        number = 2 * num_lines
        fft = None

        if num_lines == 0:
            return

        # Parse frequency range from UI
        try:
            x_axis_range = (
                float(dp.main.popup_fft_scope.ui.lineEditXmin.text()),
                float(dp.main.popup_fft_scope.ui.lineEditXmax.text()),
            )
        except ValueError:
            dp.logger.error("Invalid frequency range for FFT computation.")
            return

        for line in dp.main.graph_scope.lines:
            x_data, y_data = line.data

            if x_data is None or y_data is None or x_data.size <= 1:
                continue

            # Extract data within the specified frequency/time range.
            x_range = np.bitwise_and(
                x_data <= x_axis_range[1], x_axis_range[0] <= x_data
                )
            x_data = x_data[x_range]
            y_data = y_data[x_range][np.newaxis, ...]

            if x_data.size <= 1:
                continue

            # Compute FFT.
            f_s = dp.interface.trigger.sampling_frequency
            sample_count = dp.interface.trigger.sample_count or 1

            fft = FFT(y_data, f_s / sample_count)

            data.append(fft.magnitude)
            data.append(fft.phase)

        # Send results to FRA view and switch to FRA page.
        if fft is not None:
            dp.interface.update_fra_data.emit(
                tuple(range(number)),
                fft.frequency, data,
                False, -1
                )

        # Open FRA window.
        dp.main.ui.pushButtonOpenScopeFRA.toggled.emit(True)

    dp.main.popup_scope.ui.pushButtonComputeFFT.clicked.connect(
        __on_button_compute_fft
        )

    dp.main.popup_fft_scope.ui.pushButtonCompute.clicked.connect(
        __on_compute_fft
        )

    def __on_save_data(format_: str, scope: 'GraphView') -> None:
        """ Export graph data as PNG images or CSV files. """

        dp.main.popup_fft_scope.close()

        # Choose export directory.
        dir_str = QFileDialog.getExistingDirectory(
            dp.main.ui.centralwidget,
            QCoreApplication.translate(
                'Window_Main',
                QCoreApplication.translate(
                    'Window_Main', 'Select a folder to save to', None
                    ),
                None
                ),
            str(dp.config.get_parameter(('last-dir',)) or ''),
            QFileDialog.ShowDirsOnly,
            )

        if not dir_str:
            return

        export_dir = Path(dir_str)
        now = datetime.datetime.now()
        timestamp = now.strftime('%d-%m-%Y_%H-%M-%S')

        # Store previous list of the axis' items.
        store_items = [axis.items.copy() for axis in scope.axes]

        try:
            for axis in scope.axes:
                for item in reversed(axis.items):
                    if not isinstance(item, Line):
                        axis.items.remove(item)

            for i, axis in enumerate(scope.axes):
                if not axis.lines:
                    continue

                file_path = export_dir / f'{timestamp}_{i}.{format_}'

                if format_ == 'png':

                    # Transparent background for PNG export.
                    scope._widget.setBackground((255, 255, 255, 100))
                    pg.setConfigOption('background', (255, 255, 255, 100))
                    QApplication.processEvents()

                    exporter = pg.exporters.ImageExporter(axis)
                    exporter.export(str(file_path))

                    # Restore original background.
                    scope._widget.setBackground('#f8f8f2')
                    pg.setConfigOption('background', '#f8f8f2')
                    QApplication.processEvents()

                    dp.logger.info(f'Exported PNG: {file_path}.')
                elif format_ == 'csv':
                    data = np.stack(
                        [axis.lines[0].x_data]
                            + [line.y_data for line in axis.lines],
                        axis=1,
                        )

                    # Choose appropriate x-axis label.
                    x_symbol = 'time' if axis.x_unit == 's' else 'frequency'
                    header = x_symbol + ', ' + ', '.join(line.name() for line in axis.lines)

                    np.savetxt(
                        file_path,
                        data,
                        delimiter=', ',
                        header=header,
                        comments='',
                        )

                    dp.logger.info(f'Export file: {file_path}.')
        except (OSError, PermissionError) as e:
            dp.logger.error(f'Failed to export data: {e}')
        finally:
            # Always restore the previous list of items.
            for i, axis in enumerate(scope.axes):
                axis.items = store_items[i]

        # Save the last used directory.
        dp.config.set_parameter(('last-dir',), str(dir_str))

    # Connect export buttons for all graph views.
    export_buttons = (
        (dp.main.popup_scope.ui.pushButtonExportPng, 'png', dp.main.graph_scope),
        (dp.main.popup_scope.ui.pushButtonExportCsv, 'csv', dp.main.graph_scope),
        (dp.main.popup_fra_scope.ui.pushButtonExportPng, 'png', dp.main.graph_fra),
        (dp.main.popup_fra_scope.ui.pushButtonExportCsv, 'csv', dp.main.graph_fra),
        )

    for button, format_, scope in export_buttons:
        button.clicked.connect(
            lambda format=format_, scope=scope: __on_save_data(format, scope)
            )

    def __on_load_data() -> None:
        """ Load CSV file and populate the import variables table. """

        file_path, _ = QFileDialog.getOpenFileName(
            dp.main.ui.centralwidget,
            QCoreApplication.translate(
                'Window_Main',
                'Select a file to open',
                None
                ),
            str(dp.config.get_parameter(('last-dir',)) or ''),
            'CSV Files (*.csv)',
            )

        file_path = Path(file_path)
        if not file_path.is_file():
            return

        try:
            with file_path.open('r', encoding='utf-8') as file:
                header_line = file.readline()
                if not header_line:
                    dp.logger.error("The selected CSV file is empty.")
                    return

                header = [h.strip() for h in header_line.split(',')[1:]]

                # Clear existing tables.
                dp.import_csv.ui.tableWidgetVariables.setRowCount(0)
                dp.import_csv.ui.tableWidgetVariableSelected_1.setRowCount(0)
                dp.import_csv.ui.tableWidgetVariableSelected_2.setRowCount(0)

                # Populate variables table.
                for i, name in enumerate(header):
                    dp.import_csv.ui.tableWidgetVariables.insertRow(i)
                    dp.import_csv.ui.tableWidgetVariables.setItem(
                        i, 0, QTableWidgetItem(name)
                    )

                dp.import_csv.show()

            dp.config.set_parameter(('last-dir',), str(file_path.parent))

            dp.logger.info(f'Import file: {str(file_path)}.')
        except (OSError, UnicodeDecodeError) as e:
            dp.logger.error(f'Failed to load CSV file: {e}')

    dp.main.popup_scope.ui.pushButtonImportCsv.clicked.connect(
        lambda: __on_load_data()
        )

    dp.main.ui.pushButtonScopeClearImport.clicked.connect(
        lambda: dp.main.graph_scope.remove_all_imported_lines()
        )
    dp.main.ui.pushButtonScopeClearImport.clicked.connect(
        lambda: dp.logger.info('Clear imported data.')
        )

    def __on_open_variable_viewer() -> None:
        """ Toggle visibility of the variable viewer table. """

        table = dp.main.ui.tableWidgetNumbers
        button = dp.main.ui.pushButtonOpenVarViewer

        if table.isHidden():
            table.show()
            button.setText('Variable Viewer ↓')
            dp.logger.info('Opened variable viewer.')
        else:
            table.hide()
            button.setText('Variable Viewer ↑')
            dp.logger.info('Closed variable viewer.')

    dp.main.ui.pushButtonOpenVarViewer.clicked.connect(
        __on_open_variable_viewer
        )

    def __toggle_cursors_visibility(checked: bool, scope: 'GraphView') -> None:
        """
        Show or hide cursors, markers,
        and measurement text for a graph view.
        """

        method = QGraphicsItem.show if checked else QGraphicsItem.hide

        for axis in scope.axes:
            # Toggle cursors.
            for cursor in axis.cursors:
                method(cursor)
                cursor.sigDragged.emit(cursor)

            for line in axis._lines + axis._imported_lines:
                method(line.mark_point_0['point'])
                method(line.mark_point_0['label'])
                method(line.mark_point_1['point'])
                method(line.mark_point_1['label'])

            # Toggle fill region and measurement text box.
            method(axis.fill)
            method(axis.measure_text)

    # Connect cursor enable/disable buttons for all views.
    cursor_buttons = (
        (dp.main.ui.pushButtonEnableScopeCursors, dp.main.graph_scope, 'Scope'),
        (dp.main.ui.pushButtonEnableFRACursors, dp.main.graph_fra, 'FRA'),
        (dp.main.ui.pushButtonEnableMathCursors, dp.main.graph_math, 'Math'),
        (dp.fra_settings.ui.pushButtonEnableFRAConfigCursors, dp.fra_settings.graph_fra_config, 'FRA config'),
        (dp.fra_settings.ui.pushButtonEnableFRAConfigCursors, dp.fra_settings.graph_fra_excitation, 'FRA excitation'),
        )

    for button, scope, name in cursor_buttons:
        button.toggled.connect(
            lambda checked, scope=scope: __toggle_cursors_visibility(checked, scope)
        )
        button.toggled.connect(
            lambda checked, name=name: dp.logger.info(
                f'{"Enabled" if checked else "Disabled"} cursors for {name}.'
            )
        )

    fps_tracker = FrameRateTracker(progress_func=dp.status_tracker.progress)
    dp.interface.frame_rate_changed.connect(lambda fps: fps_tracker(fps))

    dp.interface.trigger.stage_changed.connect(
        lambda: dp.status_tracker.progress(
            dp.interface.trigger.stage,
            ) if dp.interface.mode == 'Triggered Mode' else None,
        )

    dp.interface.trigger.fra_progress_changed.connect(
        lambda: dp.status_tracker.progress(
            f'{dp.interface.trigger.fra_progress[0]:.2f} Hz'
            f' ({dp.interface.trigger.fra_progress[1]}%)'
            f', {dp.interface.trigger.fra_progress[2]}',
            ) if dp.interface.mode == 'FRA Mode' else None,
        )

    def __periodic_update() -> None:

        # grid_enable = not dp.interface.is_started() or dp.interface.mode != 'Real-Time Mode'

        # dp.main.graph_scope.enable_grid(grid_enable)
        # dp.main.graph_fra.enable_grid(grid_enable)
        # dp.main.graph_math.enable_grid(grid_enable)
        # dp.fra_settings.graph_fra_config.enable_grid(grid_enable)
        # dp.fra_settings.graph_fra_excitation.enable_grid(grid_enable)

        dp.main.graph_scope.update_lines()
        dp.main.graph_fra.update_lines()
        dp.main.graph_math.update_lines()
        dp.fra_settings.graph_fra_config.update_lines()
        dp.fra_settings.graph_fra_excitation.update_lines()

    def __periodic_ipc() -> None:
        """
        Handles the periodic Inter-Process Communication (IPC) cycle.
        Sends local graph data to peer instances and processes incoming data
        to dynamically synchronize remote graph lines in the UI.
        """

        # Send local graph data to all connected peers.
        dp.ipc.send_data(dp.main.graph_scope)

        # Process incoming data if IPC synchronization is enabled in the UI.
        if dp.main.ui.checkBoxIPC.isChecked():
            while True:
                # Receive batches of data from all subscribers.
                data = dp.ipc.receive_data()
                if not data:
                    break

                # Process each batch
                #   (grouped by remote instance and axis index).
                for instance, axis, incoming_names, array in data:
                    try:
                        x_data = array[0]
                        y_data = array[1:]

                        # Format incoming names to avoid collisions
                        # (e.g., "ipc1: temperature").
                        formatted_names = [
                            f'ipc{instance}: {name}' for name in incoming_names
                            ]
                        formatted_names_set = set(formatted_names)

                        # Extract current IPC line names for the specific axis
                        # into a set for O(1) lookups.
                        current_names_set = {
                            line.name() for line in dp.main.graph_scope.axes[axis].ipc_lines
                            }

                        # Remove obsolete IPC lines.
                        #   (Lines that were imported previously
                        #   but are no longer present in the incoming batch).
                        obsolete_names = current_names_set - formatted_names_set
                        for line_name in obsolete_names:
                            if line_name.startswith('ipc'):
                                dp.main.graph_scope.remove_ipc_line(
                                    axis, line_name
                                    )

                        # Add new IPC lines
                        #   (Lines that just appeared in the incoming batch).
                        new_names = formatted_names_set - current_names_set
                        for name in new_names:
                            dp.main.graph_scope.add_line(
                                axis=axis,
                                name=name,
                                type_='float32_t',
                                address=0,
                                ipc=True,
                                enable_marks=False,
                                )

                        if formatted_names:
                            dp.main.graph_scope.set_ipc_data_by_name(
                                formatted_names, x_data, y_data
                            )
                    except Exception:
                        continue
        else:
            # If IPC is disabled, clean up all remote lines.
            dp.main.graph_scope.remove_all_ipc_lines()

    dp.main.timer_graph_update.timeout.connect(__periodic_update)
    dp.main.timer_ipc.timeout.connect(__periodic_ipc)
