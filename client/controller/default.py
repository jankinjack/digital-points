from typing import TYPE_CHECKING
import copy

if TYPE_CHECKING:
    from digital_points import DigitalPoints


def init_default(dp: 'DigitalPoints') -> None:
    """ Init default settings. """

    # Get settings from the JSON config file.
    dp.config.enable = True
    config = copy.deepcopy(dp.config.get_config(load_file=True))

    #
    # Settings from main window.
    #

    # Hide the variable viewer.
    if not dp.main.ui.tableWidgetNumbers.isHidden():
        dp.main.ui.pushButtonOpenVarViewer.clicked.emit()

    # Disable cursors.
    dp.main.ui.pushButtonEnableScopeCursors.setChecked(False)
    dp.main.ui.pushButtonEnableScopeCursors.toggled.emit(False)
    dp.main.ui.pushButtonEnableFRACursors.setChecked(False)
    dp.main.ui.pushButtonEnableFRACursors.toggled.emit(False)
    dp.main.ui.pushButtonEnableMathCursors.setChecked(False)
    dp.main.ui.pushButtonEnableMathCursors.toggled.emit(False)
    dp.fra_settings.ui.pushButtonEnableFRAConfigCursors.setChecked(False)
    dp.fra_settings.ui.pushButtonEnableFRAConfigCursors.toggled.emit(False)

    # Load default language.
    dp.main.ui.comboBoxLanguage.setCurrentIndex(config['language'])
    dp.main.ui.comboBoxLanguage.currentIndexChanged.emit(
        config['language']
        )

    # Open the Scope by default.
    dp.main.ui.pushButtonOpenScope.toggled.emit(True)

    # Default value for the type of communication interface.
    dp.main.ui.spinBoxNodeAddr.setValue(
        config['node address']
        )
    dp.main.ui.spinBoxNodeAddr.valueChanged.emit(
        config['node address']
        )

    # Default value for the mode.
    dp.main.ui.comboBoxMode.setCurrentText(
        config['mode']
        )
    dp.main.ui.comboBoxMode.currentTextChanged.emit(
        config['mode']
        )

    # Default value for the saving selection.
    dp.main.ui.checkBoxSaveSelection.setChecked(
        config['save-selection']
        )
    dp.main.ui.checkBoxSaveSelection.toggled.emit(
        config['save-selection']
        )

    # Default value for the edge type.
    edge = config['trigger']['edge']
    if edge == 'Leading Edge':
        dp.main.ui.pushButtonLeadEdge.setChecked(True)
        dp.main.ui.pushButtonTrailEdge.setChecked(False)
        dp.main.ui.pushButtonAlterEdge.setChecked(False)
        dp.main.ui.pushButtonLeadEdge.toggled.emit(True)
    elif edge == 'Trailing Edge':
        dp.main.ui.pushButtonLeadEdge.setChecked(False)
        dp.main.ui.pushButtonTrailEdge.setChecked(True)
        dp.main.ui.pushButtonAlterEdge.setChecked(False)
        dp.main.ui.pushButtonTrailEdge.toggled.emit(True)
    else:
        dp.main.ui.pushButtonLeadEdge.setChecked(False)
        dp.main.ui.pushButtonTrailEdge.setChecked(False)
        dp.main.ui.pushButtonAlterEdge.setChecked(True)
        dp.main.ui.pushButtonAlterEdge.toggled.emit(True)

    # Default value for the dump size.
    dp.main.ui.spinBoxDumpSize.setValue(
        config['rtm']['dump_size_mb']
        )
    dp.main.ui.spinBoxDumpSize.valueChanged.emit(
        config['rtm']['dump_size_mb']
        )

    # Default value for the trigger level.
    dp.main.ui.doubleSpinBoxTriggerLevel.setValue(
        config['trigger']['level']
        )
    dp.main.ui.doubleSpinBoxTriggerLevel.valueChanged.emit(
        config['trigger']['level']
        )

    # Default value for the one shot mode.
    dp.main.ui.checkBoxOneShotMode.setChecked(
        config['trigger']['one_shot_mode']
        )
    dp.main.ui.checkBoxOneShotMode.toggled.emit(
        config['trigger']['one_shot_mode']
        )

    # Default value for the pre-trigger.
    dp.main.ui.spinBoxPreTrigger.setValue(
        config['trigger']['pre_trigger']
        )
    dp.main.ui.spinBoxPreTrigger.valueChanged.emit(
        config['trigger']['pre_trigger']
        )

    # Default value for the post-trigger.
    dp.main.ui.spinBoxPostTrigger.setValue(
        config['trigger']['post_trigger']
        )
    dp.main.ui.spinBoxPostTrigger.valueChanged.emit(
        config['trigger']['post_trigger']
        )

    # Default value for the trigger count.
    dp.main.ui.spinBoxTriggerCount.setValue(
        config['trigger']['count']
        )
    dp.main.ui.spinBoxTriggerCount.valueChanged.emit(
        config['trigger']['count']
        )

    # Default value for the settling time.
    dp.main.ui.doubleSpinBoxSettlingTime.setValue(
        config['trigger']['settling time'])
    dp.main.ui.doubleSpinBoxSettlingTime.valueChanged.emit(
        config['trigger']['settling time'])

    # Default value for the sample count.
    dp.main.ui.spinBoxSampleCount.setValue(
        config['sample count']
        )
    dp.main.ui.spinBoxSampleCount.valueChanged.emit(
        config['sample count']
        )

    # Default graph visibility.
    dp.main.ui.comboBoxGraphVisibility.setCurrentIndex(0)
    dp.main.ui.comboBoxGraphVisibility.currentIndexChanged.emit(0)

    #
    # Settings from the window of communication settings.
    #

    # Changing the interface.
    if config['interface']['type'] == 'serial':
        dp.main.ui.pushButtonSetSerial.setChecked(True)
        dp.main.ui.pushButtonSetCAN.setChecked(False)
        dp.main.ui.pushButtonSetSerial.toggled.emit(True)
    elif config['interface']['type'] == 'can':
        dp.main.ui.pushButtonSetCAN.setChecked(True)
        dp.main.ui.pushButtonSetSerial.setChecked(False)
        dp.main.ui.pushButtonSetCAN.toggled.emit(True)

    # Changing the baudrate.
    dp.com_settings.ui.comboBoxSerialBaudrate.setCurrentText(
        str(config['interface']['serial']['baudrate'])
        )
    dp.com_settings.ui.comboBoxSerialBaudrate.currentTextChanged.emit(
        str(config['interface']['serial']['baudrate'])
        )

    # Changing the byte size.
    dp.com_settings.ui.comboBoxSerialDataBits.setCurrentText(
        str(config['interface']['serial']['bytesize'])
        )
    dp.com_settings.ui.comboBoxSerialDataBits.currentTextChanged.emit(
        str(config['interface']['serial']['bytesize'])
        )

    # Changing the parity.
    dp.com_settings.ui.comboBoxSerialParity.setCurrentText(
        config['interface']['serial']['parity']
        )
    dp.com_settings.ui.comboBoxSerialParity.currentTextChanged.emit(
        config['interface']['serial']['parity']
        )

    # Changing the stop_bits.
    dp.com_settings.ui.comboBoxSerialStopBits.setCurrentText(
        str(config['interface']['serial']['stopbits'])
        )
    dp.com_settings.ui.comboBoxSerialStopBits.currentTextChanged.emit(
        str(config['interface']['serial']['stopbits'])
        )

    # Changing the bitrate.
    dp.com_settings.ui.spinBoxCANBitrate.setValue(
        config['interface']['can']['bitrate']
        )
    dp.com_settings.ui.spinBoxCANBitrate.valueChanged.emit(
        config['interface']['can']['bitrate']
        )

    # Changing the ID.
    dp.com_settings.ui.spinBoxCANID.setValue(
        config['interface']['can']['id']
        )
    dp.com_settings.ui.spinBoxCANID.valueChanged.emit(
        config['interface']['can']['id']
        )

    # Changing the ID type.
    dp.com_settings.ui.checkBoxExtendedID.setChecked(
        config['interface']['can']['extended_id']
        )
    dp.com_settings.ui.checkBoxExtendedID.toggled.emit(
        config['interface']['can']['extended_id']
        )

    # Changing the bus type.
    dp.com_settings.ui.comboBoxCANBusType.setCurrentText(
        config['interface']['can']['bus_type']
        )
    dp.com_settings.ui.comboBoxCANBusType.currentTextChanged.emit(
        config['interface']['can']['bus_type']
        )

    #
    # Settings from the window of FRA settings.
    #

    dp.fra_settings.ui.lineEditFmin.setText('1')
    dp.fra_settings.ui.lineEditFmax.setText('1000')
    dp.fra_settings.ui.lineEditNfreq.setText('20')
    # dp.fra_settings.ui.lineEditFmin.editingFinished.emit()
    # dp.fra_settings.ui.lineEditFmax.editingFinished.emit()
    dp.fra_settings.ui.lineEditNfreq.editingFinished.emit()

    dp.fra_settings.ui.lineEditAmplitude.setText('1')
    dp.fra_settings.ui.lineEditRepeat.setText('1')
    dp.fra_settings.ui.lineEditAmplitude.editingFinished.emit()
    dp.fra_settings.ui.lineEditRepeat.editingFinished.emit()

    #
    # Settings from the window of Math.
    #

    dp.main.ui.lineEditSamplingFrequency.setText(config['math']['f_s'])
    dp.main.ui.lineEditCrossFrequency.setText(config['math']['f_c'])
    dp.main.ui.lineEditPhaseMargin.setText(config['math']['phi_m'])
    dp.main.ui.lineEditKCorrection.setText(config['math']['k_corr'])
    dp.main.ui.lineEditPhiCorrection.setText(config['math']['phi_corr'])

    #
    # Settings from the window of FRA.
    #

    # Min frequency for FRA range.
    dp.fra_settings.ui.lineEditFmin.setText(
        config['fra']['frequency min']
        )
    dp.fra_settings.ui.lineEditFmin.editingFinished.emit()

    # Max frequency for FRA range.
    dp.fra_settings.ui.lineEditFmax.setText(
        config['fra']['frequency max']
        )
    dp.fra_settings.ui.lineEditFmax.editingFinished.emit()

    # Frequency count for FRA range.
    dp.fra_settings.ui.lineEditNfreq.setText(
        config['fra']['frequency count']
        )
    dp.fra_settings.ui.lineEditNfreq.editingFinished.emit()

    # Amplitudes of excitation.
    dp.fra_settings.ui.lineEditAmplitude.setText(
        config['fra']['amplitude']
        )

    # Repeats for averaging.
    dp.fra_settings.ui.lineEditRepeat.setText(
        config['fra']['repeat']
        )

    # Averaging method.
    dp.fra_settings.ui.comboBoxAverageType.setCurrentText(
        config['fra']['average type']
        )

    # Excitation type.
    dp.fra_settings.ui.comboBoxExcitationType.setCurrentText(
        config['fra']['excitation type']
        )

    # Normalize amplitude.
    dp.fra_settings.ui.checkBoxNormalize.setChecked(
        config['fra']['norm amp']
        )
    dp.fra_settings.ui.checkBoxNormalize.toggled.emit(
        config['fra']['norm amp']
        )

    # dp.fra_settings.ui.lineEditRepeat.editingFinished.emit()
    dp.fra_settings.ui.lineEditAmplitude.editingFinished.emit()

    # Load the last used ELF file.
    dp.main.ui.pushButtonUpdateELF.clicked.emit()

    # Cursor measurements.
    dp.main.ui.checkBoxMeasDelta.setChecked(
        config['measurement']['delta']
        )
    dp.main.ui.checkBoxMeasMin.setChecked(
        config['measurement']['min']
        )
    dp.main.ui.checkBoxMeasMax.setChecked(
        config['measurement']['max']
        )
    dp.main.ui.checkBoxMeasRMS.setChecked(
        config['measurement']['rms']
        )
    dp.main.ui.checkBoxMeasMean.setChecked(
        config['measurement']['mean']
        )
    dp.main.ui.checkBoxMeasCF.setChecked(
        config['measurement']['crest factor']
        )
