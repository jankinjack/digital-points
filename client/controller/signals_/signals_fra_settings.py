
from typing import TYPE_CHECKING

import numpy as np

import model.fra.excitation as excitation
from model.fra.fra import FRA
from controller.common import add_drag_handlers

if TYPE_CHECKING:
    from digital_points import DigitalPoints


def init_signals_fra_settings(dp: 'DigitalPoints') -> None:
    """
    Initialize and connect all Qt signals related
    to FRA (Frequency Response Analysis) settings.
    """

    # Cache frequently accessed objects to improve readability and performance.
    ui = dp.fra_settings.ui
    trigger = dp.interface.trigger
    graph_config = dp.fra_settings.graph_fra_config
    graph_excitation = dp.fra_settings.graph_fra_excitation

    dp.main.ui.pushButtonConfigureFRA.clicked.connect(dp.fra_settings.show)

    def __update_graph_from_data() -> None:
        """
        Update the FRA configuration graph
        with current frequencies and amplitudes.
        """

        frequencies = trigger.fra_frequencies
        amplitudes = trigger.fra_amplitudes

        if amplitudes.size > 0:
            graph_config.set_data(
                lines=(0,),
                x_data=frequencies,
                y_data=(amplitudes,),
                )

            graph_config.axes[0].setYRange(
                np.min(amplitudes) * 0.9,
                np.max(amplitudes) * 1.1,
                )

    def __update_fra_config() -> None:
        """
        Save current FRA UI parameters to the JSON configuration file.
        """

        dp.config.set_parameter(
            ('fra', 'frequency min'),
            ui.lineEditFmin.text(),
            )
        dp.config.set_parameter(
            ('fra', 'frequency max'),
            ui.lineEditFmax.text(),
            )
        dp.config.set_parameter(
            ('fra', 'frequency count'),
            ui.lineEditNfreq.text(),
            )
        dp.config.set_parameter(
            ('fra', 'amplitude'),
            ui.lineEditAmplitude.text(),
            )
        dp.config.set_parameter(
            ('fra', 'repeat'),
            ui.lineEditRepeat.text(),
            )
        dp.config.set_parameter(
            ('fra', 'average type'),
            ui.comboBoxAverageType.currentText(),
            )
        dp.config.set_parameter(
            ('fra', 'excitation type'),
            ui.comboBoxExcitationType.currentText(),
            )

    def __on_frequencies_changed() -> None:
        """
        Recalculate FRA parameters when frequency bounds,
        count, or excitation type changes.
        """

        f_min_str = ui.lineEditFmin.text()
        f_max_str = ui.lineEditFmax.text()
        n_freq_str = ui.lineEditNfreq.text()

        f_s = trigger.sampling_frequency
        n_max = trigger.max_number_samples

        first_change = trigger.fra_frequencies.size == 0

        if not n_max or n_max < 2 or not f_min_str or not f_max_str:
            return

        f_min = float(f_min_str)
        f_max = float(f_max_str)
        n_freq = int(n_freq_str)

        # Clamp maximum frequency to the Nyquist limit.
        if f_max > f_s / 2:
            f_max = f_s / 2

        if f_min >= f_max:
            f_min = f_max / 2

        exc_type = ui.comboBoxExcitationType.currentText()

        # Calculate discrete FRA parameters
        # based on the selected excitation strategy.
        calc_func = (
            FRA.sse_parameters_from_frequency_range
            if exc_type == 'Single-Sine Excitation'
            else FRA.mse_parameters_from_frequency_range
            )

        (trigger.fra_frequencies, trigger.fra_n_list, trigger.fra_dividers, trigger.fra_harmonics) = \
            calc_func(f_min, f_max, n_freq, n_max, f_s)

        if first_change:
            __on_set_for_all()

        __update_graph_from_data()
        __update_fra_config()

    ui.lineEditFmin.editingFinished.connect(__on_frequencies_changed)
    ui.lineEditFmax.editingFinished.connect(__on_frequencies_changed)
    ui.lineEditNfreq.editingFinished.connect(__on_frequencies_changed)
    ui.comboBoxExcitationType.currentIndexChanged.connect(
        __on_frequencies_changed
        )

    def __on_set_for_all() -> None:
        """
        Apply global amplitude, repeat count,
        and averaging settings to all FRA points.
        """

        amp_str = ui.lineEditAmplitude.text()
        exc_type = ui.comboBoxExcitationType.currentText()
        is_normalized = ui.checkBoxNormalize.isChecked()

        if amp_str:
            # Apply uniform amplitude if Single-Sine
            # or normalization is disabled.
            if exc_type == 'Single-Sine Excitation' or not is_normalized:
                trigger.fra_amplitudes = np.full(
                    len(trigger.fra_frequencies),
                    float(amp_str),
                    dtype=np.float64,
                )

        trigger.fra_repeat = int(ui.lineEditRepeat.text())
        trigger.fra_average_type = ui.comboBoxAverageType.currentText()
        trigger.fra_excitation_type = exc_type

        __update_graph_from_data()
        __update_fra_config()

    ui.lineEditAmplitude.editingFinished.connect(__on_set_for_all)
    ui.lineEditRepeat.editingFinished.connect(__on_set_for_all)
    ui.comboBoxAverageType.currentIndexChanged.connect(__on_set_for_all)
    ui.comboBoxExcitationType.currentIndexChanged.connect(__on_set_for_all)

    def __update_data_from_graph(index: int) -> None:
        """
        Interpolate amplitudes between dragged points
        on a logarithmic frequency scale.
        """

        line = graph_config.axes[0].lines[0]
        x_data = line.x_data
        y_data = line.y_data.copy()

        length = len(y_data)
        if length < 2:
            return

        # Convert frequencies to dB scale for logarithmic interpolation.
        log_x = 20 * np.log10(x_data)
        f_first, f_last = log_x[0], log_x[-1]
        y_first, y_last = y_data[0], y_data[-1]

        if 0 < index < length - 1:
            y_n = y_data[index]
            f_n = log_x[index]

            # Interpolate below the dragged point.
            y_data[:index] = np.interp(
                log_x[:index], [f_first, f_n], [y_first, y_n]
                )
            # Interpolate above the dragged point.
            y_data[index + 1:] = np.interp(
                log_x[index + 1:], [f_n, f_last], [y_n, y_last]
                )
        else:
            # If dragging the first or last point,
            # interpolate the entire middle section.
            y_data[1:-1] = np.interp(
                log_x[1:-1], [f_first, f_last], [y_first, y_last]
                )

        # Update graph data and the interface trigger atomically.
        line.data = (x_data, y_data)
        trigger.fra_amplitudes = y_data

    graph_config.axes[0].lines[0].dragged.connect(
        __update_data_from_graph
        )

    def __on_update_excitation() -> None:
        """
        Generate and plot the time-domain excitation signal
        based on current FRA settings.
        """

        frequencies = trigger.fra_frequencies
        amplitudes = trigger.fra_amplitudes
        dividers = trigger.fra_dividers
        harmonics = trigger.fra_harmonics
        n_list = trigger.fra_n_list

        normalize = bool(ui.checkBoxNormalize.isChecked())
        exc_type = trigger.fra_excitation_type

        if n_list is None or n_list.size == 0 or int(n_list[0]) == 0:
            return

        amp_str = ui.lineEditAmplitude.text()
        norm_amplitude = float(amp_str) if amp_str else None
        base_amplitude = norm_amplitude or 1.0

        if exc_type == 'Single-Sine Excitation':
            signal, t = excitation.single_sine_signal(
                base_amplitude,
                int(n_list[0]),
                1.0 / frequencies[0],
                harmonics[0],
                dividers[0]
            )
        else:
            signal, t = excitation.multi_sine_signal(
                amplitudes,
                int(n_list[0]),
                1.0 / frequencies[0],
                harmonics,
                progress_callback=lambda i: ui.progressBarExcitationSynhesis.setValue(int(i))
            )

            # Normalize the multi-sine signal
            # to match the desired peak amplitude.
            if normalize and norm_amplitude:
                peak_val = max(abs(np.min(signal)), abs(np.max(signal)))
                if peak_val > 0:
                    k_n = norm_amplitude / peak_val
                    signal *= k_n
                    trigger.fra_amplitudes *= k_n

        __update_graph_from_data()

        graph_excitation.set_data(
            lines=(0,),
            x_data=t,
            y_data=(signal,),
        )

    ui.pushButtonUpdateFRAExcitation.clicked.connect(
        __on_update_excitation
        )

    ui.checkBoxNormalize.toggled.connect(
        lambda value: dp.config.set_parameter(('fra', 'norm amp'), value)
        )

    add_drag_handlers(dp.fra_settings)
