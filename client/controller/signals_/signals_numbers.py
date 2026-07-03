from enum import IntEnum
from typing import TYPE_CHECKING

from PySide6.QtWidgets import QTableWidgetItem, QLineEdit
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

from model.line import VAR_TYPE_INT_FLOAT, VAR_TYPE_CODE

if TYPE_CHECKING:
    from digital_points import DigitalPoints


class NumCol(IntEnum):
    """ Column indices for the Numbers table to avoid magic numbers. """
    COMBO_BOX = 0
    TYPE = 1
    ADDRESS = 2
    MIN_LIMIT = 6
    MAX_LIMIT = 7
    VALUE = 8


# Pre-compile validators at the module level to avoid recreating them
# every time a variable is selected from the combo box.
INT_VALIDATOR = QRegularExpressionValidator(QRegularExpression(r'^[-+]?[0-9]+'))
FLOAT_VALIDATOR = QRegularExpressionValidator(
    QRegularExpression(r'[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)')
)


def init_signals_numbers(dp: 'DigitalPoints') -> None:
    """ Initialize and connect all Qt signals related to the Numbers table. """

    table = dp.main.ui.tableWidgetNumbers
    main_table = dp.main.ui.tableWidgetVariables

    def _on_var_selected(name: str, row: int) -> None:
        """
        Handle variable selection from the combo box
        in the Numbers table.
        """

        min_edit = table.cellWidget(row, NumCol.MIN_LIMIT)
        max_edit = table.cellWidget(row, NumCol.MAX_LIMIT)
        val_edit = table.cellWidget(row, NumCol.VALUE)
        line_edits = (min_edit, max_edit, val_edit)

        if name == '-- NONE --':
            # Clear type, address, and other text fields.
            for col in range(1, table.columnCount()):
                table.setItem(row, col, QTableWidgetItem(''))

            for edit in line_edits:
                if edit:
                    edit.setDisabled(True)

            return

        # Find the selected variable in the main variables table.
        for r in range(main_table.rowCount()):
            item_name = main_table.item(r, 0)
            if item_name and item_name.text() == name:
                item_type = main_table.item(r, 1)
                item_addr = main_table.item(r, 2)

                # Populate type and address in the numbers table.
                table.setItem(
                    row, NumCol.TYPE, QTableWidgetItem(item_type.text())
                    )
                table.setItem(
                    row, NumCol.ADDRESS, QTableWidgetItem(item_addr.text())
                    )

                # Assign the appropriate validator based on the variable type.
                var_category = VAR_TYPE_INT_FLOAT.get(
                    item_type.text(), 'float'
                    )
                validator = INT_VALIDATOR if var_category == 'integer' else FLOAT_VALIDATOR

                for edit in line_edits:
                    if edit:
                        edit.setEnabled(True)
                        edit.setText('')
                        edit.setValidator(validator)
                break

    # Connect all combo boxes in the table.
    for i in range(table.rowCount()):
        combo_box = table.cellWidget(i, NumCol.COMBO_BOX)
        if combo_box:
            # Use default argument 'row=i'
            # to correctly capture the loop variable.
            combo_box.currentTextChanged.connect(
                lambda text, row=i: _on_var_selected(text, row)
                )

    def __on_var_changed(line_edit: QLineEdit, row: int) -> None:
        """ Handle value submission (editingFinished) in the Numbers table. """

        value_text = line_edit.text()
        if not value_text:
            return

        min_edit = table.cellWidget(row, NumCol.MIN_LIMIT)
        max_edit = table.cellWidget(row, NumCol.MAX_LIMIT)

        min_text = min_edit.text() if min_edit else ''
        max_text = max_edit.text() if max_edit else ''

        item_type = table.item(row, NumCol.TYPE)
        item_addr = table.item(row, NumCol.ADDRESS)

        if not item_type or not item_addr:
            return

        try:
            type_code = VAR_TYPE_CODE.get(item_type.text())

            # Addresses in the table are stored as hex strings.
            address = int(item_addr.text(), 16)
        except (ValueError, TypeError):
            return

        var_category = VAR_TYPE_INT_FLOAT.get(item_type.text(), 'float')

        # Wrap parsing.
        try:
            if var_category == 'integer':
                value = int(value_text)
                min_val = int(min_text) if min_text else float('-inf')
                max_val = int(max_text) if max_text else float('inf')
            else:
                value = float(value_text)
                min_val = float(min_text) if min_text else float('-inf')
                max_val = float(max_text) if max_text else float('inf')
        except ValueError:
            return

        # Enforce user-defined limits.
        if not (min_val <= value <= max_val):
            return

        # Send the write command to the microcontroller.
        if type_code is not None:
            dp.interface.write_value_0x03(type_code, address, value)

        # Clear the input field after successful transmission.
        line_edit.setText('')

    # Connect all value line edits in the table.
    for i in range(table.rowCount()):
        val_edit = table.cellWidget(i, NumCol.VALUE)
        if val_edit:
            val_edit.editingFinished.connect(
                lambda edit=val_edit, row=i: __on_var_changed(edit, row)
                )
