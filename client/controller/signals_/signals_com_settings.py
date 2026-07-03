
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from digital_points import DigitalPoints

from controller.common import add_drag_handlers


def init_signals_com_settings(dp: 'DigitalPoints') -> None:
    """ Initialize and connect all Qt signals related to COM/CAN settings. """

    def __on_com_param_changed(
            instances: list[str] | tuple[str] | set[str],
            param_name: str,
            value: Optional[str | int | float],
            ) -> None:
        """ Handler for serial/CAN parameter changes. """

        changed = False

        for inst_name in instances:
            interface_inst = dp.interface.instances.get(inst_name)
            if interface_inst is None:
                continue

            current_value = getattr(interface_inst, param_name, None)
            if current_value != value:
                setattr(interface_inst, param_name, value)
                dp.config.set_parameter(
                    ('interface', inst_name, param_name),
                    value
                    )
                changed = True

        if changed:
            # Disconnect to apply new settings.
            dp.interface.interface.disconnect_from_port()

            if value:
                dp.logger.info(
                    f'Change parameter "{param_name}": {value}.'
                    )

    # Changing the COM port.
    dp.com_settings.ui.comboBoxSerialPorts.currentTextChanged.connect(
        lambda text: __on_com_param_changed(
            {'serial', 'can'},
            'port',
            text if text != '-- NONE --' and text != '' else '',
            )
        )

    # Changing the baudrate.
    dp.com_settings.ui.comboBoxSerialBaudrate.currentTextChanged.connect(
        lambda text: __on_com_param_changed({'serial', 'can'}, 'baudrate', int(text))
        )

    # Changing the byte size.
    dp.com_settings.ui.comboBoxSerialDataBits.currentTextChanged.connect(
        lambda text: __on_com_param_changed({'serial'}, 'bytesize', int(text))
        )

    # Changing the parity.
    dp.com_settings.ui.comboBoxSerialParity.currentTextChanged.connect(
        lambda text: __on_com_param_changed({'serial'}, 'parity', text)
        )

    # Changing the stop_bits.
    dp.com_settings.ui.comboBoxSerialStopBits.currentTextChanged.connect(
        lambda text: __on_com_param_changed({'serial'}, 'stopbits', float(text))
        )

    # Changing the bus type.
    dp.com_settings.ui.comboBoxCANBusType.currentTextChanged.connect(
        lambda text: __on_com_param_changed({'can'}, 'bus_type', text)
        )

    # Changing the bitrate.
    dp.com_settings.ui.spinBoxCANBitrate.valueChanged.connect(
        lambda value: __on_com_param_changed({'can'}, 'bitrate', value)
        )

    # Changing the ID.
    dp.com_settings.ui.spinBoxCANID.valueChanged.connect(
        lambda value: __on_com_param_changed({'can'}, 'id', value)
        )

    # Changing the ID type.
    dp.com_settings.ui.checkBoxExtendedID.toggled.connect(
        lambda value: __on_com_param_changed({'can'}, 'extended_id', value)
        )

    def __on_list_com_ports_changed(
            list_com_ports: list[str] | tuple[str],
            store_com_ports: list[str] | tuple[str],
            ) -> None:
        """ Handler for available COM ports list updates. """

        was_empty = not bool(store_com_ports)
        is_empty = not bool(list_com_ports)

        combo_box = dp.com_settings.ui.comboBoxSerialPorts

        if not was_empty:
            choose_port = combo_box.currentText()
        elif not is_empty:
            choose_port = dp.config.get_parameter(
                ('interface', 'serial', 'port')
                )
        else:
            choose_port = '-- NONE --'
            dp.interface.interface.disconnect_from_port()

        if choose_port not in list_com_ports:
            choose_port = '-- NONE --'
            dp.interface.interface.disconnect_from_port()

        combo_box.blockSignals(True)

        combo_box.clear()
        combo_box.addItem('-- NONE --')
        combo_box.addItems(list_com_ports)
        combo_box.setCurrentText(choose_port)

        combo_box.blockSignals(False)

        # Manually emit to apply the final selected port.
        combo_box.currentTextChanged.emit(choose_port)

    dp.interface.list_of_com_ports_changed.connect(
        __on_list_com_ports_changed
        )

    add_drag_handlers(dp.com_settings)

    def __on_about_to_quit() -> None:
        """
        Ensure the serial port is safely closed
        before the application exits.
        """

        dp.interface.interface.disconnect_from_port()

    dp.aboutToQuit.connect(__on_about_to_quit)
