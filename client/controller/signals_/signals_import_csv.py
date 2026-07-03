
from typing import TYPE_CHECKING
from pathlib import Path

import numpy as np

from PySide6.QtWidgets import (
    QTableWidget,
    QLineEdit,
    QTableWidgetItem,
    QFileDialog,
    )
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import Qt, QRegularExpression

from controller.common import add_drag_handlers, select_variable_in_table

if TYPE_CHECKING:
    from digital_points import DigitalPoints


# CSS style for the time-shift line edits in the import tables.
LINE_EDIT_STYLE = """
    QLineEdit {
        color: black;
        background-color: white;
        border: 0px;
        padding-bottom: 3px;
        padding-left: 3px;
    }
"""

# Pre-compile validator to avoid recreating it on every drop event
FLOAT_VALIDATOR = QRegularExpressionValidator(
    QRegularExpression(r'[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)')
)


def init_signals_import_csv(dp: 'DigitalPoints') -> None:
    """ Initialize and connect all Qt signals related to CSV importing. """

    def __on_import_csv() -> None:
        """ Handler for pushButtonImportCSV clicked. """

        last_dir = dp.config.get_parameter(('last-dir',)) or ''

        # Using QFileDialog to let the user select the file,
        # starting from the last used directory.
        file_path_str, _ = QFileDialog.getOpenFileName(
            dp.import_csv,
            "Select CSV File",
            last_dir,
            "CSV Files (*.csv);;All Files (*)"
        )

        if not file_path_str:
            return

        file_path = Path(file_path_str)
        if not file_path.is_file():
            return

        try:
            with file_path.open('r', encoding='utf-8') as file:
                # Parse header.
                header_line = file.readline()
                if not header_line:
                    dp.logger.error("The selected CSV file is empty.")
                    return

                header = [h.strip() for h in header_line.split(',')[1:]]

                selected_names = []
                time_shifts = []
                axes_mapping = []

                # Consolidate table processing to avoid code duplication.
                tables_and_axes = [
                    (dp.import_csv.ui.tableWidgetVariableSelected_1, 0),
                    (dp.import_csv.ui.tableWidgetVariableSelected_2, 1),
                ]

                i_start = len(dp.main.graph_scope.imported_lines)

                for table, axis_idx in tables_and_axes:
                    for row in range(table.rowCount()):
                        name_item = table.item(row, 0)
                        if not name_item:
                            continue

                        name = name_item.text()

                        # Validate that the variable actually
                        # exists in the CSV header.
                        if name not in header:
                            dp.logger.warning(
                                f"Variable '{name}' not found in CSV header. Skipping."
                                )
                            continue

                        enable_marks = dp.main.ui.pushButtonEnableScopeCursors.isChecked()

                        dp.main.graph_scope.add_line(
                            axis=axis_idx,
                            name=f'Import: {name}',
                            type_='float32_t',
                            address=0,
                            imported=True,
                            enable_marks=enable_marks,
                        )

                        selected_names.append(name)
                        axes_mapping.append(axis_idx)

                        shift_widget = table.cellWidget(row, 1)
                        shift_val = float(shift_widget.text()) if shift_widget else 0.0
                        time_shifts.append(shift_val)

                if not selected_names:
                    dp.logger.info("No valid variables selected for import.")
                    return

                # Read numeric data.
                # Reset file pointer to beginning before passing to loadtxt.
                file.seek(0)
                data = np.loadtxt(file, delimiter=',', skiprows=1)

                if data.ndim == 1:
                    # Handle single-column CSVs gracefully.
                    x_data = data
                    rest_data = []
                else:
                    x_data = data[:, 0]
                    rest_data = data[:, 1:].T

                # Apply data to the graph
                for i, (name, time_shift) in enumerate(zip(
                        selected_names, time_shifts
                        )):
                    try:
                        j = header.index(name)
                        # Apply time shift and set data
                        dp.main.graph_scope.set_imported_data(
                            (i_start + i,),
                            x_data + time_shift,
                            (rest_data[j],),
                        )
                    except (IndexError, ValueError) as e:
                        dp.logger.error(
                            f"Failed to map variable '{name}': {e}"
                            )

            dp.import_csv.close()
            dp.config.set_parameter(('last-dir',), str(file_path.parent))
            dp.logger.info(f'Successfully imported file: {file_path.name}.')

        except (ValueError, IndexError, UnicodeDecodeError) as e:
            dp.logger.error(f'Failed to parse CSV file: {e}')
        except Exception as e:
            dp.logger.error(f'Unexpected error during CSV import: {e}')

    dp.import_csv.ui.pushButtonImportCSV.clicked.connect(__on_import_csv)

    def __on_drop_from_common(_, table: QTableWidget) -> None:
        """ Handler for dropping items onto tables with selected variables. """

        selection_model = dp.import_csv.ui.tableWidgetVariables.selectionModel()
        if not selection_model.hasSelection():
            return

        row = selection_model.selectedRows()[0].row()
        name_item = dp.import_csv.ui.tableWidgetVariables.item(row, 0)
        if not name_item:
            return

        name = name_item.text()
        row_count = table.rowCount()

        # Add the variable to the table.
        table.insertRow(row_count)
        item = QTableWidgetItem(name)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        table.setItem(row_count, 0, item)

        # Add line-edit for time shifts.
        line_edit = QLineEdit()
        line_edit.setStyleSheet(LINE_EDIT_STYLE)
        line_edit.setValidator(FLOAT_VALIDATOR)
        line_edit.setText('0.0')

        table.setCellWidget(row_count, 1, line_edit)

    dp.import_csv.ui.tableWidgetVariableSelected_1.dropEvent = \
        lambda event: __on_drop_from_common(
            event,
            dp.import_csv.ui.tableWidgetVariableSelected_1
            )
    dp.import_csv.ui.tableWidgetVariableSelected_2.dropEvent = \
        lambda event: __on_drop_from_common(
            event,
            dp.import_csv.ui.tableWidgetVariableSelected_2
            )

    dp.import_csv.ui.lineEditSearchVariable.textChanged.connect(
        lambda text: select_variable_in_table(
            dp.import_csv.ui.tableWidgetVariables, text
            )
        )

    add_drag_handlers(dp.import_csv)
