
import re
import itertools
from typing import TYPE_CHECKING, Optional
from contextlib import suppress
import orjson
import warnings

from struct import pack, unpack

from pathlib import Path

from watchdog.events import FileSystemEventHandler

import numpy as np

from PySide6.QtWidgets import QFileDialog, QTableWidgetItem, QApplication
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import Qt, QRegularExpression, QCoreApplication, Signal, QObject

import __main__
from model.elf_file_parser import ELF_Parser, VAR_TYPE_BITS
from model.line import VAR_TYPE_CODE, VAR_TYPE_INT_FLOAT
from controller.common import (
    get_regex_and_dims_from_array_name,
    get_array_item_name_and_offset,
    )
from controller.default import init_default

if TYPE_CHECKING:
    from digital_points import DigitalPoints


def init_signals_settings(dp: 'DigitalPoints') -> None:
    """ Init signal related to settings. """

    #
    # Settings from main window.
    #

    # Changing the type of communication interface.
    dp.main.ui.spinBoxNodeAddr.valueChanged.connect(
        lambda value: dp.interface.__setattr__('node_address', value)
        )

    def __on_mode_changed(new_mode: str) -> None:
        """ Handler of comboBoxMode changed. """
        if not new_mode:
            return

        if dp.interface.mode != new_mode:
            dp.logger.info(f'Change mode: {new_mode}.')

        dp.interface.mode = new_mode

        # Remove all lines from FRA axes.
        dp.main.graph_fra.remove_all_lines()

        # Determine current mode flags
        is_rtm = new_mode == 'Real-Time Mode'
        is_trig = new_mode == 'Triggered Mode'
        is_fra = new_mode == 'FRA Mode'

        # Update common UI elements visibility based on flags
        dp.main.ui.labelTrigger.setVisible(not is_rtm)
        dp.main.ui.frameLineTrigger.setVisible(not is_rtm)

        dp.main.ui.labelRTM.setVisible(is_rtm)
        dp.main.ui.frameLineRTM.setVisible(is_rtm)

        dp.main.ui.labelFRA.setVisible(is_fra)
        dp.main.ui.frameLineFRA.setVisible(is_fra)

        # Enable FFT button only in Triggered Mode
        dp.main.popup_scope.ui.pushButtonComputeFFT.setEnabled(is_trig)

        # Group Triggered Mode specific layouts and lines to toggle them in a loop
        trigger_widgets = (
            dp.main.ui.widgetLayoutSampleCount,
            dp.main.ui.widgetLayoutOneShotMode,
            dp.main.ui.widgetLayoutTriggerLevel,
            dp.main.ui.widgetLayoutPreTrigger,
            dp.main.ui.widgetLayoutPostTrigger,
            dp.main.ui.widgetLayoutTriggerCount,
            )
        trigger_lines = (
            dp.main.ui.line_4, dp.main.ui.line_6, dp.main.ui.line_7,
            dp.main.ui.line_8, dp.main.ui.line_11, dp.main.ui.line_10,
            )

        for widget in trigger_widgets:
            widget.setVisible(is_trig)
        for line in trigger_lines:
            line.setVisible(is_trig)

        # Cache the cursor marks state to avoid repeated method calls.
        enable_marks = dp.main.ui.pushButtonEnableFRACursors.isChecked()

        # Helper function to avoid duplicating the add_line boilerplate.
        def add_to_fra_axes(name: str):
            for i in range(len(dp.main.graph_fra.axes)):
                dp.main.graph_fra.add_line(
                    axis=i,
                    name=name,
                    type_='none',
                    address=0,
                    show_symbols=True,
                    enable_marks=enable_marks,
                )

        # Add lines to FRA axes based on the current mode.
        if is_trig:
            for axis in dp.main.graph_scope.axes:
                for line in axis.lines:
                    add_to_fra_axes(line.name())
        elif is_fra:
            scope_axes = dp.main.graph_scope.axes

            # Check if we have at least 2 axes and both have lines.
            if len(scope_axes) >= 2 and scope_axes[0].lines and scope_axes[1].lines:
                for line_a, line_b in itertools.product(
                        scope_axes[0].lines, scope_axes[1].lines
                        ):
                    add_to_fra_axes(f'{line_b.name()}/{line_a.name()}')

            # Show both Scope Graphs.
            dp.main.ui.comboBoxGraphVisibility.setCurrentIndex(0)
            dp.main.ui.comboBoxGraphVisibility.currentIndexChanged.emit(0)

        # Update mode status label
        dp.main.ui.labelModeStatus.setText(new_mode)

    # Changing the mode.
    dp.main.ui.comboBoxMode.currentTextChanged.connect(
        __on_mode_changed
        )

    # Changing the saving selection.
    dp.main.ui.checkBoxSaveSelection.toggled.connect(
        lambda value: dp.config.set_parameter(('save-selection',), value)
        )

    def __on_edge_change(checked: bool, edge: str) -> None:
        """ Handler of edge changing. """

        if checked:
            dp.interface.trigger.edge = edge

        edge_name = dp.interface.trigger.edge_name

        dp.main.ui.pushButtonLeadEdge.setChecked(edge_name == 'Leading Edge')
        dp.main.ui.pushButtonTrailEdge.setChecked(edge_name == 'Trailing Edge')
        dp.main.ui.pushButtonAlterEdge.setChecked(edge_name == 'Alter Edge')

    # Changing the edge type.
    dp.main.ui.pushButtonLeadEdge.toggled.connect(
        lambda checked: __on_edge_change(checked, 'Leading Edge')
        )
    dp.main.ui.pushButtonTrailEdge.toggled.connect(
        lambda checked: __on_edge_change(checked, 'Trailing Edge')
        )
    dp.main.ui.pushButtonAlterEdge.toggled.connect(
        lambda checked: __on_edge_change(checked, 'Alter Edge')
        )

    # Changing the one shot mode.
    dp.main.ui.checkBoxOneShotMode.toggled.connect(
        lambda value: dp.interface.trigger.__setattr__('one_shot_mode', value)
        )

    # Changing the trigger level.
    dp.main.ui.doubleSpinBoxTriggerLevel.valueChanged.connect(
        lambda value: dp.interface.trigger.__setattr__('level', value)
        )

    def __recompute_pre_post_triggers() -> None:

        pre_trigger = dp.main.ui.spinBoxPreTrigger.value()
        post_trigger = dp.main.ui.spinBoxPostTrigger.value()

        if dp.interface.trigger.number_of_variables > 0:
            number_samples_per_variable =\
                dp.interface.trigger.max_number_samples // dp.interface.trigger.number_of_variables
        else:
            number_samples_per_variable = dp.interface.trigger.max_number_samples

        # Limit the pre- and post-triggers based on limitation of memory size.
        if number_samples_per_variable > 0 and pre_trigger + post_trigger >= number_samples_per_variable:
            if pre_trigger >= number_samples_per_variable:
                pre_trigger = number_samples_per_variable
                post_trigger = 1
            else:
                post_trigger = number_samples_per_variable - pre_trigger

        dp.interface.trigger.__setattr__('pre_trigger', pre_trigger)
        dp.interface.trigger.__setattr__('post_trigger', post_trigger)

        dp.main.ui.spinBoxPreTrigger.setValue(pre_trigger)
        dp.main.ui.spinBoxPostTrigger.setValue(post_trigger)

    # Changing the dump size.
    dp.main.ui.spinBoxDumpSize.valueChanged.connect(
        lambda value: dp.interface.__setattr__('dump_size_mb', value)
        )

    # Changing the pre-trigger.
    dp.main.ui.spinBoxPreTrigger.valueChanged.connect(
        lambda value: dp.interface.trigger.__setattr__('pre_trigger', value)
        )

    # Changing the post-trigger.
    dp.main.ui.spinBoxPostTrigger.valueChanged.connect(
        lambda value: dp.interface.trigger.__setattr__('post_trigger', value)
        )

    dp.interface.trigger.recompute_pre_post_triggers.connect(
        __recompute_pre_post_triggers
        )

    # Changing the trigger count.
    dp.main.ui.spinBoxTriggerCount.valueChanged.connect(
        lambda value: dp.interface.trigger.__setattr__('count', value)
        )

    # Changing the sample count.
    dp.main.ui.spinBoxSampleCount.valueChanged.connect(
        lambda value: dp.interface.trigger.__setattr__('sample_count', value)
        )

    # Changing the settling time.
    dp.main.ui.doubleSpinBoxSettlingTime.valueChanged.connect(
        lambda value: dp.interface.trigger.__setattr__('settling_time', value)
        )

    def __on_button_open_elf() -> None:
        """ Handler of pushButtonOpenELF clicked. """

        # Open an ELF file.
        file, _ = QFileDialog.getOpenFileName(
            dp.main.ui.centralwidget,
            QCoreApplication.translate(
                'Window_Main',
                'Select a file to open',
                None
                ),
            str(Path(dp.config.get_parameter(('elf-file', 'path'))).parent),
            'ELF Files (*.elf *.axf *.bin *.o *.out *.prx *.puff *.ko *.mod *.so)',
            )

        __open_elf_file(file)

    class ELFModifyHandler(FileSystemEventHandler, QObject):

        elf_file_modified = Signal()

        def on_created(self, event) -> None:
            self.on_event(event)

        def on_modified(self, event) -> None:
            self.on_event(event)

        def on_event(self, event) -> None:
            self.elf_file_modified.emit()

    def __on_elf_file_modified() -> None:
        # Update the ELF file.
        dp.interface.disconnect_from_node()
        __open_elf_file(str(
            Path(dp.config.get_parameter(('elf-file', 'path')))
            ))

    dp.elf_watchdog['timer'].timeout.connect(__on_elf_file_modified)

    def __open_elf_file(file: str) -> None:

        path_file = Path(file)

        if file and path_file.is_file():
            # Get variables from the ELF file.
            elf_parser = ELF_Parser()

            try:
                list_of_variables = elf_parser.get_variables_from_elf(
                    file,
                    lambda val: dp.main.ui.progressBarOpenELF.setValue(val),
                    ('MICRO_DP', 'NULL_MICRO_DP', 'SIGNALS_DP')
                    )
            except Exception as err:
                dp.logger.error(
                    f'{type(err).__name__}: {err}'
                    )
                return

            # Clear the tables with variables.
            dp.main.ui.tableWidgetVariables.setRowCount(0)
            dp.variable_sel.ui.tableWidgetVariables.setRowCount(0)
            dp.variable_sel.ui.tableWidgetVariableSelected_1.setRowCount(0)
            dp.variable_sel.ui.tableWidgetVariableSelected_2.setRowCount(0)

            # Clear combo-boxes for Numbers.
            combo_boxes = []
            for i in range(dp.main.ui.tableWidgetNumbers.rowCount()):
                c_b = dp.main.ui.tableWidgetNumbers.indexWidget(
                    dp.main.ui.tableWidgetNumbers.model().index(i, 0)
                    )
                c_b.clear()
                c_b.addItem('-- NONE --')
                combo_boxes.append(c_b)

            # Clear the trigger.
            dp.interface.trigger.clear()
            dp.main.ui.labelTriggerName.setText('')

            # Remove all lines.
            dp.main.graph_scope.remove_all_lines()
            dp.main.graph_fra.remove_all_lines()

            # Update axes according to the current mode.
            dp.main.ui.comboBoxMode.currentTextChanged.emit(
                dp.interface.mode
                )

            # Disconnect from current node.
            dp.interface.disconnect_from_node()

            # Add the variables to the tables with variables.
            for i, var in enumerate(list_of_variables):
                dp.main.ui.tableWidgetVariables.insertRow(i)

                item = QTableWidgetItem(var['name'])
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

                dp.main.ui.tableWidgetVariables.setItem(i, 0, item)

                item = QTableWidgetItem(var['type'])
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

                dp.main.ui.tableWidgetVariables.setItem(i, 1, item)

                item = QTableWidgetItem(hex(var['address']))
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

                dp.main.ui.tableWidgetVariables.setItem(i, 2, item)

                item = QTableWidgetItem()
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)

                dp.main.ui.tableWidgetVariables.setItem(i, 3, item)

                dp.variable_sel.ui.tableWidgetVariables.insertRow(i)
                dp.variable_sel.ui.tableWidgetVariables.setItem(
                    i, 0,
                    QTableWidgetItem(var['name']),
                    )
                dp.variable_sel.ui.tableWidgetVariables.setItem(
                    i, 1,
                    QTableWidgetItem(var['type']),
                    )
                dp.variable_sel.ui.tableWidgetVariables.setItem(
                    i, 2,
                    QTableWidgetItem(hex(var['address'])),
                    )
                dp.variable_sel.ui.tableWidgetVariables.setItem(
                    i, 3,
                    QTableWidgetItem(),
                    )

                # Add variable to Variable Viewer.
                if '[' not in var['name']:
                    for c_b in combo_boxes:
                        c_b.addItem(var['name'])

            dp.main.ui.pushButtonOpenELF.setText(' ' + path_file.name)

            # Add the ELF file's name to the config file.
            dp.config.set_parameter(('elf-file', 'path'), file)
            dp.config.set_parameter(
                ('elf-file', 'mtime'),
                path_file.stat().st_mtime
                )

            def __on_watchdog_signal() -> None:
                # Time for 2 s to handle ELF file modifications.
                dp.elf_watchdog['timer'].stop()
                dp.elf_watchdog['timer'].start(2000)

            handler = ELFModifyHandler()
            handler.elf_file_modified.connect(__on_watchdog_signal)

            # Reschedule the ELF file observer according to new path.
            dp.elf_watchdog['observer'].unschedule_all()
            dp.elf_watchdog['observer'].schedule(
                handler,
                path=str(path_file.parent),
                recursive=False
                )

            dp.logger.info(f'Download ELF file: {str(path_file)}.')

            # Select variables from config file.
            if dp.config.get_parameter(('save-selection',)):
                parameter_sel_lines = dp.config.get_parameter(
                    ('selected-lines',)
                    )
                dp.config.set_parameter(('selected-lines',), [])

                for sel in parameter_sel_lines:
                    for var in list_of_variables:
                        if sel['name'].split('[')[0] == var['name'].split('[')[0]:
                            dp.add_line_to_table(
                                dp.variable_sel.ui.tableWidgetVariableSelected_1 if sel['axis'] == 0 else dp.variable_sel.ui.tableWidgetVariableSelected_2,
                                sel['axis'],
                                var['name'],  var['type'], hex(var['address']),
                                sel['index'],
                                )

                name_sel_trigger = dp.config.get_parameter(
                    ('trigger', 'selected-line')
                    )
                dp.config.set_parameter(
                    ('trigger', 'selected-line'),
                    {'name': '', 'index': None}
                    )

                if name_sel_trigger['name']:
                    for i, var in enumerate(list_of_variables):
                        if name_sel_trigger['name'].split('[')[0] == var['name'].split('[')[0]:
                            dp.main.ui.tableWidgetVariables.selectRow(i)
                            __on_set_trigger(name_sel_trigger['index'])

    dp.main.ui.pushButtonOpenELF.clicked.connect(__on_button_open_elf)

    dp.main.ui.pushButtonUpdateELF.clicked.connect(
        lambda _: __open_elf_file(
            dp.config.get_parameter(('elf-file', 'path'))
            )
        )

    def __on_popup_table_variables(pos) -> None:
        """ Handler of customContextMenuRequested. """

        selection_model = dp.main.ui.tableWidgetVariables.selectionModel()

        if selection_model.hasSelection():
            # Get the row number.
            row = selection_model.selectedRows()[0].row()

            # Get the row's fields.
            name = dp.main.ui.tableWidgetVariables.item(row, 0).text()
            type_ = dp.main.ui.tableWidgetVariables.item(row, 1).text()
            # address = dp.main.ui.tableWidgetVariables.item(row, 2).text()

            dp.main.popup_table_variables.store_name = name

            if type_ not in VAR_TYPE_CODE:
                return

            temp1 = dp.main.popup_table_variables\
                .ui.lineEditArrayIndex

            # Check if it is array.
            if '[' in name:
                try:
                    reg_exp, _ = get_regex_and_dims_from_array_name(name)
                except AssertionError as err:
                    dp.logger.error(
                        f'{type(err).__name__}: {err}'
                        )
                    return

                # Clear the line edit.
                temp1.clear()

                # Set validator for the line edit.
                temp1.setValidator(
                    QRegularExpressionValidator(QRegularExpression(reg_exp))
                    )

                temp1.show()
                temp1.setFocus()
            else:
                temp1.hide()

            dp.main.popup_table_variables.show()

            dp.main.popup_table_variables.move(
                dp.main.ui.tableWidgetVariables.viewport().mapToGlobal(pos)
                )

    # Open a context menu for the table with variables.
    dp.main.ui.tableWidgetVariables.customContextMenuRequested.connect(
        __on_popup_table_variables
        )

    def __on_set_trigger(
            preset_index: Optional[tuple[tuple[int], tuple[int]]] = None
            ) -> None:
        """ Handler of pushButtonSetTrigger clicked. """

        dp.main.popup_table_variables.hide()

        selection_model = dp.main.ui.tableWidgetVariables.selectionModel()

        if selection_model.hasSelection():
            # Get the row number.
            row = selection_model.selectedRows()[0].row()

            # Get the row's fields.
            name = dp.main.ui.tableWidgetVariables.item(row, 0).text()
            type_ = dp.main.ui.tableWidgetVariables.item(row, 1).text()
            address = dp.main.ui.tableWidgetVariables.item(row, 2).text()

            if '[' in name:
                try:
                    _, sizes = get_regex_and_dims_from_array_name(name)
                except AssertionError as err:
                    dp.logger.error(
                        f'{type(err).__name__}: {err}'
                        )
                    return

                temp = dp.main.popup_table_variables\
                    .ui.lineEditArrayIndex

                if preset_index is None:
                    index = (
                        tuple(map(int, re.findall(r'(\d+)', temp.text()))),
                        tuple(map(int, sizes))
                        )
                else:
                    index = preset_index

                # Get the item's name and offset.
                name, offset = get_array_item_name_and_offset(
                    name, index, type_
                    )

                # Add offset to the address.
                address = hex(
                    int(address, base=16) + offset
                    )
            else:
                index = None

            # Set the data to the trigger.
            dp.interface.trigger.type_ = type_
            dp.interface.trigger.address = int(address, base=16)

            if (dp.interface.trigger.type_ in {
                    VAR_TYPE_CODE.get('float32_t'),
                    VAR_TYPE_CODE.get('float64_t'),
                    }):
                dp.main.ui.doubleSpinBoxTriggerLevel.setDecimals(6)
                dp.main.ui.doubleSpinBoxTriggerLevel.setSingleStep(0.1)
            else:
                dp.main.ui.doubleSpinBoxTriggerLevel.setDecimals(0)
                dp.main.ui.doubleSpinBoxTriggerLevel.setSingleStep(1)

            # Update the label with information about the trigger.
            dp.main.ui.labelTriggerName.setText(
                f' {name} ({type_}, {address})'
                )

            # Add line to the config file.
            dp.config.set_parameter(
                ('trigger', 'selected-line'),
                {'name': name, 'index': index},
                )

            dp.logger.info(f'Add trigger: {name}, {type_}, {address}.')

    # Setting the variable as trigger.
    dp.main.popup_table_variables.ui.pushButtonSetTrigger.clicked.connect(
        lambda: __on_set_trigger()
        )

    def __on_check_update() -> None:
        """ Hander of pushButtonCheckUpdates clicked. """
        pass

    # Checking new updates.
    dp.main.ui.pushButtonCheckUpdates.clicked.connect(__on_check_update)

    def __on_update_app() -> None:
        """ Hander of pushButtonDownload clicked. """
        pass

    # Download updates.
    dp.main.ui.pushButtonDownload.clicked.connect(
        __on_update_app
        )

    def __on_change_language(index: int) -> None:
        """Handle language change event."""

        instance = QApplication.instance()
        is_russian = index == 0

        # Translation strings dictionary.
        translations = {
            'ru': {
                'time': 'Время (с)',
                'value': 'Значение',
                'graph': 'График',
                'frequency': 'Частота (Гц)',
                'magnitude': 'Амплитуда (дБ)',
                'phase': 'Фаза (град)',
                'excitation_amp': 'Амплитуда возмущений',
                'excitation_signal': 'Возмущающий сигнал',
                'file': 'eng-ru.qm'
            },
            'en': {
                'time': 'Time (s)',
                'value': 'Value',
                'graph': 'Graph',
                'frequency': 'Frequency (Hz)',
                'magnitude': 'Magnitude (dB)',
                'phase': 'Phase (deg)',
                'excitation_amp': 'Amplitudes of Excitation',
                'excitation_signal': 'Excitation Signal',
                'file': None
            }
        }

        t = translations['ru'] if is_russian else translations['en']

        # Load or remove translator.
        if is_russian:
            file_name = __main__.FULL_PATH / 'translations' / t['file']
            dp.main.translator.load(str(file_name))
            if instance is not None:
                instance.installTranslator(dp.main.translator)
        else:
            if instance is not None:
                instance.removeTranslator(dp.main.translator)

        # Update scope labels.
        for i, axis in enumerate(dp.main.graph_scope.axes):
            axis.x_label = t['time']
            axis.y_label = f'{t["value"]} / {t["graph"]} {i+1}'

        # Update FRA and Math graph labels.
        for graph in [dp.main.graph_fra, dp.main.graph_math]:
            graph.axes[0].x_label = t['frequency']
            graph.axes[1].x_label = t['frequency']
            graph.axes[0].y_label = t['magnitude']
            graph.axes[1].y_label = t['phase']

        # Update FRA config labels.
        config_axis = dp.fra_settings.graph_fra_config.axes[0]
        config_axis.x_label = t['frequency']
        config_axis.y_label = t['excitation_amp']
        config_axis.legend.items[0][1].setText(t['excitation_amp'])

        # Update FRA excitation labels.
        excitation_axis = dp.fra_settings.graph_fra_excitation.axes[0]
        excitation_axis.x_label = t['time']
        excitation_axis.y_label = t['excitation_signal']
        excitation_axis.legend.items[0][1].setText(t['excitation_signal'])

        # Update legend sizes.
        dp.fra_settings.graph_fra_config.axes[0].legend.updateSize()
        dp.fra_settings.graph_fra_excitation.axes[0].legend.updateSize()

        # Retranslate all UI components.
        ui_components = [
            dp.main,
            dp.main.popup_scope,
            dp.main.popup_fft_scope,
            dp.main.popup_math_scope,
            dp.main.popup_table_variables,
            dp.com_settings,
            dp.variable_sel,
            dp.fra_settings,
            dp.help
        ]

        for component in ui_components:
            component.ui.retranslateUi(component)

        # Retranslate popup_selected_variables and popup_choose_array_index.
        for i in range(2):
            dp.variable_sel.popup_selected_variables[i].ui.retranslateUi(
                dp.variable_sel.popup_selected_variables[i]
            )
            dp.variable_sel.popup_choose_array_index[i].ui.retranslateUi(
                dp.variable_sel.popup_choose_array_index[i]
            )

        # Save language setting and log the change.
        dp.config.set_parameter(('language',), index)
        dp.logger.info(f'Change language: {dp.main.ui.comboBoxLanguage.currentText()}.')

    # Change language.
    dp.main.ui.comboBoxLanguage.currentIndexChanged.connect(
        __on_change_language
        )

    def __on_toggle_settings_buttons(interface: str) -> None:
        """ Handler of settings buttons clicked. """

        if interface == 'serial':
            dp.main.ui.pushButtonSetSerial.setChecked(True)
            dp.main.ui.pushButtonSetCAN.setChecked(False)
            dp.main.ui.pushButtonSetCAN.setEnabled(True)
            dp.main.ui.pushButtonSetSerial.setDisabled(True)
            dp.interface.interface = dp.interface.instances['serial']
        elif interface == 'can':
            dp.main.ui.pushButtonSetCAN.setChecked(True)
            dp.main.ui.pushButtonSetSerial.setChecked(False)
            dp.main.ui.pushButtonSetCAN.setDisabled(True)
            dp.main.ui.pushButtonSetSerial.setEnabled(True)
            dp.interface.interface = dp.interface.instances['can']

        dp.config.set_parameter(('interface', 'type'), interface)
        dp.logger.info(f'Change communication interface: {interface}')

    dp.main.ui.pushButtonSetSerial.toggled.connect(
        lambda checked:
            __on_toggle_settings_buttons('serial')
            if checked
            else None
        )
    dp.main.ui.pushButtonSetCAN.toggled.connect(
        lambda checked:
            __on_toggle_settings_buttons('can')
            if checked
            else None
        )

    # Open window to configure communication interface.
    dp.main.ui.pushButtonConfigureInterface.clicked.connect(
        lambda: dp.com_settings.show()
        )

    def __on_hide_show_scope_graphs(index: int) -> None:
        """ Handler of comboBoxGraphVisibility's current index changed. """

        if index == 0:
            dp.main.graph_scope.axes[0].setVisible(True)
            dp.main.graph_scope.axes[1].setVisible(True)

            dp.variable_sel.ui.frameLineGraph1.show()
            dp.variable_sel.ui.frameLineGraph2.show()
        elif index == 1:
            dp.main.graph_scope.axes[0].setVisible(True)
            dp.main.graph_scope.axes[1].setVisible(False)

            dp.variable_sel.ui.frameLineGraph1.show()
            dp.variable_sel.ui.frameLineGraph2.hide()
        elif index == 2:
            dp.main.graph_scope.axes[0].setVisible(False)
            dp.main.graph_scope.axes[1].setVisible(True)

            dp.variable_sel.ui.frameLineGraph1.hide()
            dp.variable_sel.ui.frameLineGraph2.show()

    # Hide/show Scope graphs.
    dp.main.ui.comboBoxGraphVisibility.currentIndexChanged.connect(
        __on_hide_show_scope_graphs
        )

    def __on_save_json_config_file() -> None:
        """ Handler of pushButtonSaveSettings clicked. """

        # Choose a path.
        file, _ = QFileDialog.getSaveFileName(
            dp.main.ui.centralwidget,
            QCoreApplication.translate(
                'Window_Main',
                'Save settings as',
                None
                ),
            str(dp.config.get_parameter(('last-dir',))),
            'JSON Files (*.json)',
            )

        if not file:
            return

        path = Path(file)

        # If the suffix is not .json then add .json suffix.
        if path.suffix != '.json':
            path = path.parent / (path.name + '.json')

        dp.config.save_config(path)
        dp.logger.info(f'Save settings: {path.name}')
        dp.config.set_parameter(('last-dir',), str(path.parent))

    # Save JSON config file.
    dp.main.ui.pushButtonSaveSettings.clicked.connect(
        __on_save_json_config_file
        )

    def __on_load_json_config_file() -> None:
        """ Handler of pushButtonLoadSettings clicked. """

        # Choose a path.
        file, _ = QFileDialog.getOpenFileName(
            dp.main.ui.centralwidget,
            QCoreApplication.translate('Window_Main', 'Load settings', None),
            str(dp.config.get_parameter(('last-dir',))),
            'JSON Files (*.json)',
            )

        if not file:
            return

        # Temporary disable logging.
        dp.logger.debug('LOG DISABLE')

        path = Path(file)
        dp.config.load_config(path)
        init_default(dp)

        dp.logger.debug('LOG ENABLE')
        dp.logger.info(f'Load settings: {path.name}')
        dp.config.set_parameter(('last-dir',), str(path.parent))

    # Load JSON config file.
    dp.main.ui.pushButtonLoadSettings.clicked.connect(
        __on_load_json_config_file
        )

    def __on_remove_trigger() -> None:
        """ Handler of pushButtonRemoveTrigger clicked. """

        dp.interface.trigger.clear()
        dp.main.ui.labelTriggerName.setText('')

        # Change the config file.
        dp.config.set_parameter(
            ('trigger', 'selected-line'),
            {'name': '', 'index': None},
            )

        dp.logger.info('Remove trigger.')

    dp.main.ui.pushButtonRemoveTrigger.clicked.connect(
        __on_remove_trigger
        )

    def __periodic_update() -> None:
        """ Handler of timeout of timer_update. """

        # Keep connection.
        if not dp.interface.interface.is_connected():
            dp.interface.interface.connect_to_port()

        if __periodic_update.count == 0:
            status = dp.interface.is_started() and dp.interface.thread_.change_ui

            # Fix the 'connect' button state because it is chackable.
            dp.main.ui.pushButtonConnect.setChecked(status)

            if status:
                if __periodic_update.last_connection_status is False:
                    dp.status_tracker.status('Started')

                    dp.main.ui.pushButtonConnect.setText(
                        QCoreApplication.translate(
                            'Window_Main', '  Stop', None,
                            )
                        )

                    # Change progress status.
                    if dp.interface.mode not in (
                            'Real-Time Mode', 'Triggered Mode'
                            ):
                        dp.status_tracker.progress('-')

                    # Disable settings while connected.
                    dp.main.ui.frameLineCom.setDisabled(True)
                    dp.main.ui.frameLineGraphsMeas.setDisabled(True)
                    dp.main.ui.frameLineTrigger.setDisabled(True)
                    dp.main.ui.frameLineRTM.setDisabled(True)
                    dp.main.ui.frameLineFRA.setDisabled(True)
                    dp.main.ui.frameLineUpdate.setDisabled(True)
                    dp.main.ui.frameLineSystem.setDisabled(True)

                    __periodic_update.last_connection_status = True
            elif __periodic_update.last_connection_status is True:
                dp.status_tracker.status('Stopped')
                dp.main.ui.pushButtonConnect.setText(
                    QCoreApplication.translate(
                        'Window_Main', '  Start', None,
                        )
                    )
                dp.main.ui.labelProgress.setText('')

                # Enable settings while disconnected.
                dp.main.ui.frameLineCom.setEnabled(True)
                dp.main.ui.frameLineGraphsMeas.setEnabled(True)
                dp.main.ui.frameLineTrigger.setEnabled(True)
                dp.main.ui.frameLineRTM.setEnabled(True)
                dp.main.ui.frameLineFRA.setEnabled(True)
                dp.main.ui.frameLineUpdate.setEnabled(True)
                dp.main.ui.frameLineSystem.setEnabled(True)

                # Change progress status.
                dp.status_tracker.progress('-')

                __periodic_update.last_connection_status = False
        elif __periodic_update.count == 1:
            # Update cursors.
            if dp.main._current_page_index == 0:        # Scope.
                for axis in dp.main.graph_scope.axes:
                    for i, _ in enumerate(axis.cursors):
                        axis.update_cursor_data(i, update_label=True)
            elif dp.main._current_page_index == 1:      # FRA.
                for axis in dp.main.graph_fra.axes:
                    for i, _ in enumerate(axis.cursors):
                        axis.update_cursor_data(i, update_label=True)
            elif dp.main._current_page_index == 2:      # Math.
                for axis in dp.main.graph_math.axes:
                    for i, _ in enumerate(axis.cursors):
                        axis.update_cursor_data(i, update_label=True)

            if dp.fra_settings.isVisible():      # FRA Config.
                for axis in dp.fra_settings.graph_fra_config.axes:
                    for i, _ in enumerate(axis.cursors):
                        axis.update_cursor_data(i, update_label=True)
        elif __periodic_update.count == 2:
            # Read numeric variables if page with numbers is open.
            if not dp.main.ui.tableWidgetNumbers.isHidden():
                numbers_table = dp.main.ui.tableWidgetNumbers
                types = []
                addresses = []
                numbers = []

                # Search for filled rows (variables).
                for row in range(numbers_table.rowCount()):
                    item_type = numbers_table.item(row, 1)
                    item_address = numbers_table.item(row, 2)

                    # If we need to read value.
                    if (item_type and item_address
                            and item_type.text() and item_address.text()):

                        # Add the variable to lists.
                        types.append(
                            VAR_TYPE_CODE.get(item_type.text(), 'float')
                            )
                        addresses.append(int(item_address.text(), base=16))
                        numbers.append(row)

                if types and addresses:
                    def __on_read_numeric_var(
                            n: int,
                            data: tuple[np.ndarray, np.ndarray],
                            ) -> None:

                        if data is None or data[1] is None:
                            return

                        item_type = numbers_table.item(n, 1)
                        type_ = item_type.text()

                        if type_ not in VAR_TYPE_INT_FLOAT:
                            return

                        # Convert the data into float of integer
                        # with different bases.
                        int_float = VAR_TYPE_INT_FLOAT.get(type_)
                        bits = VAR_TYPE_BITS.get(type_)

                        value_10 = str(int(data[1][0]))\
                            if int_float == 'integer'\
                            else str(float(data[1][0]))

                        if int_float == 'integer':
                            value_16 = hex(int(data[1][0]))[2:]
                            value_2 = bin(int(data[1][0]))[2:].zfill(bits)
                        else:
                            if type_ == 'float32_t':
                                value_16 = hex(unpack('<I', pack('<f', data[1][0]))[0])[2:]
                                value_2 = bin(int(value_16, 16))[2:].zfill(32)
                            else:
                                value_16 = hex(unpack('<Q', pack('<d', data[1][0]))[0])[2:]
                                value_2 = bin(int(value_16, 16))[2:].zfill(64)

                        numbers_table.setItem(
                            n, 3,
                            QTableWidgetItem(value_10),
                            )
                        numbers_table.setItem(
                            n, 4,
                            QTableWidgetItem(value_16),
                            )
                        numbers_table.setItem(
                            n, 5,
                            QTableWidgetItem(value_2),
                            )

                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore", RuntimeWarning)
                        with suppress(RuntimeError):
                            dp.interface.ext_handler_0x01.disconnect()

                    dp.interface.ext_handler_0x01.connect(
                        lambda i, data, numbers=numbers:
                            __on_read_numeric_var(numbers[i], data)
                        )

                    # Read the numbers.
                    dp.interface.read_values_0x01(types, addresses)

        __periodic_update.count += 1

        if __periodic_update.count == 3:
            __periodic_update.count = 0

    # Update a list of COM ports periodically.
    __periodic_update.count = 0
    __periodic_update.last_connection_status = False
    dp.com_settings.timer_update.timeout.connect(__periodic_update)
