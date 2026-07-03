
import re
from contextlib import suppress
from typing import TYPE_CHECKING
import warnings

import numpy as np

from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QLineEdit
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import Qt, QRegularExpression

from sympy.parsing.sympy_parser import parse_expr

from model.graph_view import DICT_MATH_FUNCTIONS
from controller.common import (
    get_regex_and_dims_from_array_name,
    get_array_item_name_and_offset,
    add_drag_handlers,
    select_variable_in_table,
    )

if TYPE_CHECKING:
    from digital_points import DigitalPoints


def init_signals_select_variables(dp: 'DigitalPoints') -> None:
    """ Init signal for the window with variables selection. """

    def __on_open_window_select_variables() -> None:
        if dp.interface.is_started() and dp.interface.thread_.change_ui:
            return

        dp.variable_sel.show()

        # Focus on searching for variables.
        dp.variable_sel.ui.lineEditSearchVariable.setFocus()

    # Open a window to select variables.
    dp.main.popup_scope.ui.pushButtonSelectVars.clicked.connect(
        __on_open_window_select_variables
        )

    def update_row_labels() -> None:

        length_0 = len(dp.main.graph_scope.axes[0].lines)
        length_1 = len(dp.main.graph_scope.axes[1].lines)

        i = 1
        dp.variable_sel.ui.tableWidgetVariableSelected_1.setVerticalHeaderLabels(
            [f'x{i + j}' for j in range(length_0)]
            )

        i = i + length_0
        dp.variable_sel.ui.tableWidgetVariableSelected_2.setVerticalHeaderLabels(
            [f'x{i + j}' for j in range(length_1)]
            )

    def add_line_to_table(
            table: QTableWidget,
            num: int,
            name: str,
            type_: str,
            address: str,
            index: list | tuple,
            ) -> None:

        if len(index[0]) != len(index[1]):
            return

        dp.variable_sel.popup_choose_array_index[num].close()

        if '[' in name:
            # Get the item's name and offset.
            name, offset = get_array_item_name_and_offset(name, index, type_)

            # Add offset to the address.
            address = hex(
                int(address, base=16) + offset
                )

        row_count = table.rowCount()

        # Add the variables to the table.
        table.insertRow(row_count)
        item = QTableWidgetItem(name)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        table.setItem(row_count, 0, item)

        item = QTableWidgetItem(type_)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        table.setItem(row_count, 1, item)

        item = QTableWidgetItem(address)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        table.setItem(row_count, 2, item)

        # Add the variables as line to the scope view.
        line = dp.main.graph_scope.add_line(
            axis=num,
            name=name,
            type_=type_,
            address=int(address, base=16),
            enable_marks=dp.main.ui.pushButtonEnableScopeCursors.isChecked(),
            )

        dp.logger.info(f'Add line to graph {num + 1}: {name}, {type_}, {address}.')

        # Update axes according to the current mode.
        dp.main.ui.comboBoxMode.currentTextChanged.emit(
            dp.interface.mode
            )

        # Add line-edit for expressions.
        line_edit = QLineEdit()
        line_edit.setStyleSheet(u"QLineEdit {\n"
            "   color: black;\n"
            "	background-color: white;\n"
            "	border: 0px;\n"
            "   padding-bottom: 3px;\n"
            "   padding-left: 3px;\n"
            "}\n")
        table.setCellWidget(row_count, 3, line_edit)
        line_edit.setText(line.expression)

        def __on_line_expression_changed() -> None:
            # Get the expression.
            text = line_edit.text()

            if text == '':
                text = 'x'

            suffix = ''

            with suppress(Exception):
                # Parse the expression.
                parsed = parse_expr(text, evaluate=False)

                x_num = [
                    int(str(sym)[1:])
                    for sym in parsed.free_symbols if str(sym)[1:]
                    ]

                # Check for the user used appropriate arguments.
                if (len(parsed.free_symbols) > 0
                        and all([
                            re.fullmatch(r'x[0-9]*|t', str(sym))
                            for sym in parsed.free_symbols
                            ])
                        and all([
                            n <= len(dp.main.graph_scope.lines) for n in x_num
                            ])):

                    eval(
                        text.replace('^', '**'),
                        DICT_MATH_FUNCTIONS,
                        {'x': np.array([1, 2, 3]), 't': np.array([1, 2, 3])}\
                            | {f'x{n}': np.array([1, 2, 3]) for n in x_num},
                        )

                    # Save the expression.
                    line.expression = text

                    if not parsed.is_Atom:
                        suffix = '*'

            # Update the expression.
            line_edit.setText(line.expression)

            # Update the legend.
            # Note: LegentItem does not update labels itself.
            for axis in dp.main.graph_scope.axes:
                # Find an appropriate item in legend
                # to add/remove a suffix.
                for item in axis.legend.items:
                    if item[0].item is line:
                        item[1].setText(f'{line.name()}{suffix}')

        line_edit.editingFinished.connect(
            __on_line_expression_changed
            )

        update_row_labels()

        # Add line to config file.
        parameter_sel_lines = dp.config.get_parameter(('selected-lines',))

        parameter_sel_lines.append({
            'axis': num,
            'name': name,
            'index': index,
            })

        dp.config.set_parameter(
            ('selected-lines',),
            parameter_sel_lines,
            )

    def __on_drop_from_common(
            event,
            table: QTableWidget,
            num: int,
            ) -> None:
        """ Handler of dropping items on tables with selected variables. """

        rows_count = dp.variable_sel.ui.tableWidgetVariableSelected_1.rowCount() \
            + dp.variable_sel.ui.tableWidgetVariableSelected_2.rowCount()

        # Limit number of variables.
        if rows_count >= dp.interface.vars_number:
            return

        selection_model = dp.variable_sel.ui.tableWidgetVariables.selectionModel()

        if selection_model.hasSelection():
            # Get the row number.
            row = selection_model.selectedRows()[0].row()

            # Get the row's fields.
            name = dp.variable_sel.ui.tableWidgetVariables.item(row, 0).text()
            type_ = dp.variable_sel.ui.tableWidgetVariables.item(row, 1).text()
            address = dp.variable_sel.ui.tableWidgetVariables.item(row, 2).text()

            # Check if it is array.
            if '[' in name:
                try:
                    reg_exp, sizes = get_regex_and_dims_from_array_name(name)
                except AssertionError as err:
                    dp.logger.error(
                        f'{type(err).__name__}: {err}'
                        )
                    return

                line_edit_index = dp.variable_sel.popup_choose_array_index[num]\
                    .ui.lineEditArrayIndex
                button_add = dp.variable_sel.popup_choose_array_index[num]\
                    .ui.pushButtonAdd

                # Clear the line edit.
                line_edit_index.clear()

                # Set validator for the line edit.
                line_edit_index.setValidator(
                    QRegularExpressionValidator(QRegularExpression(reg_exp))
                    )

                dp.variable_sel.popup_choose_array_index[num].popup(
                    table.viewport().mapToGlobal(event.pos())
                    )

                def __handler() -> None:
                    add_line_to_table(
                        table,
                        num,
                        name,
                        type_,
                        address,
                        (tuple(map(int, re.findall(r'(\d+)', line_edit_index.text()))),
                            tuple(map(int, sizes))),
                        )

                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", RuntimeWarning)
                    with suppress(RuntimeError):
                        line_edit_index.editingFinished.disconnect()
                        button_add.clicked.disconnect()

                line_edit_index.editingFinished.connect(__handler)
                button_add.clicked.connect(__handler)

                line_edit_index.setFocus()
            else:
                add_line_to_table(
                    table,
                    num,
                    name,
                    type_,
                    address,
                    ((), ()),
                    )

    dp.add_line_to_table = add_line_to_table

    dp.variable_sel.ui.tableWidgetVariableSelected_1.dropEvent = \
        lambda event: __on_drop_from_common(
            event,
            dp.variable_sel.ui.tableWidgetVariableSelected_1,
            0,
            )
    dp.variable_sel.ui.tableWidgetVariableSelected_2.dropEvent = \
        lambda event: __on_drop_from_common(
            event,
            dp.variable_sel.ui.tableWidgetVariableSelected_2,
            1,
            )

    dp.variable_sel.ui.lineEditSearchVariable.textChanged.connect(
        lambda text: select_variable_in_table(
            dp.variable_sel.ui.tableWidgetVariables,
            text
            )
        )

    # Open a context menu for the tables with selected variables.
    dp.variable_sel.ui.tableWidgetVariableSelected_1.customContextMenuRequested.connect(
        lambda pos: dp.variable_sel.popup_selected_variables[0].popup(
            dp.variable_sel.ui.tableWidgetVariableSelected_1.viewport().mapToGlobal(pos)
            )
        )
    dp.variable_sel.ui.tableWidgetVariableSelected_2.customContextMenuRequested.connect(
        lambda pos: dp.variable_sel.popup_selected_variables[1].popup(
            dp.variable_sel.ui.tableWidgetVariableSelected_2.viewport().mapToGlobal(pos)
            )
        )

    def __on_remove_line(table_num: int) -> None:
        """ Handler of pushButtonRemove clicked. """

        # Close the popup.
        dp.variable_sel.popup_selected_variables[table_num].close()

        # Get the table.
        if table_num == 0:
            table = dp.variable_sel.ui.tableWidgetVariableSelected_1
        else:
            table = dp.variable_sel.ui.tableWidgetVariableSelected_2

        selection_model = table.selectionModel()

        if selection_model.hasSelection():
            # Get the row number.
            row = selection_model.selectedRows()[0].row()

            # Get the row's fields.
            name = table.item(row, 0).text()
            type_ = table.item(row, 1).text()
            address = table.item(row, 2).text()

            dp.logger.info(f'Remove line from graph {table_num + 1}: {name}, {type_}, {address}.')

            # Remove the row.
            table.removeRow(row)

            # Remove the selected line.
            dp.main.graph_scope.remove_line(table_num, address=int(address, base=16))

            # Update axes according to the current mode.
            dp.main.ui.comboBoxMode.currentTextChanged.emit(
                dp.interface.mode
                )

            update_row_labels()

            # Remove line from config file.
            parameter_sel_lines = dp.config.get_parameter(('selected-lines',))
            parameter_sel_lines = [
                sel for sel in parameter_sel_lines if name != sel['name']
                ]

            dp.config.set_parameter(
                ('selected-lines',),
                parameter_sel_lines,
                )

    # Remove selected line.
    dp.variable_sel.popup_selected_variables[0].ui.pushButtonRemove.clicked.connect(
        lambda _: __on_remove_line(0)
        )
    dp.variable_sel.popup_selected_variables[1].ui.pushButtonRemove.clicked.connect(
        lambda _: __on_remove_line(1)
        )

    add_drag_handlers(dp.variable_sel)
