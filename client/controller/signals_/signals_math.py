
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QCoreApplication

from model.math import Math

if TYPE_CHECKING:
    from digital_points import DigitalPoints


def init_signals_math(dp: 'DigitalPoints') -> None:
    """
    Initialize and connect all Qt signals
    related to the Math / PID synthesis window.
    """

    def __on_load_csv() -> None:
        """
        Handler for pushButtonLoadCSV clicked.
        Loads .dat files with frequency responses.
        """

        dp.main.popup_math_scope.close()

        file, _ = QFileDialog.getOpenFileName(
            dp.main.ui.centralwidget,
            QCoreApplication.translate(
                'Window_Main', 'Select a file to open', None
                ),
            str(dp.config.get_parameter(('last-dir',)) or ''),
            'DAT Files (*.dat);;All Files (*)',
            )

        file_path = Path(file)
        if not file_path.is_file():
            return

        try:
            # Load and transpose data (expects columns: freq, mag, phase).
            data = np.loadtxt(file_path, skiprows=1)

            if data.ndim != 2 or data.shape[1] < 3:
                dp.logger.error(
                    'Invalid DAT file format. Expected at least 3 columns.'
                    )
                return

            data = data.T
            __load_data(data, file_path.name)
            dp.config.set_parameter(('last-dir',), str(file_path.parent))

        except (ValueError, OSError, IndexError) as e:
            dp.logger.error(f"Failed to parse DAT file: {e}")

    def __on_load_fra() -> None:
        """
        Handler for pushButtonLoadFRA clicked.
        Loads data directly from the FRA graph.
        """

        dp.main.popup_math_scope.close()

        if (not dp.main.graph_fra.axes[0].lines
                or not dp.main.graph_fra.axes[1].lines):
            return

        x_data = dp.main.graph_fra.axes[0].lines[0].x_data
        y_amp = dp.main.graph_fra.axes[0].lines[0].y_data
        y_phase = dp.main.graph_fra.axes[1].lines[0].y_data

        # Safe check for empty or uninitialized graph lines.
        if x_data is None or y_amp is None or y_phase is None:
            return

        data = np.stack((x_data, y_amp, y_phase))
        __load_data(data, 'fra')

    def __load_data(data: np.ndarray, name: str) -> None:
        """ Clear graphs and plot the loaded frequency response data. """

        dp.main.graph_math.remove_all_lines()
        dp.main.graph_math.remove_all_imported_lines()

        enable_marks = dp.main.ui.pushButtonEnableMathCursors.isChecked()

        # Add lines for Amplitude (axis 0) and Phase (axis 1).
        dp.main.graph_math.add_line(
            axis=0, name=name, type_='float32_t', address=0,
            imported=True, enable_marks=enable_marks,
            )
        dp.main.graph_math.add_line(
            axis=1, name=name, type_='float32_t', address=0,
            imported=True, enable_marks=enable_marks,
            )

        # Safely parse correction factors.
        k_corr = float(dp.main.ui.lineEditKCorrection.text() or 0.0)
        phi_corr = float(dp.main.ui.lineEditPhiCorrection.text() or 0.0)

        # Apply corrections and set data.
        dp.main.graph_math.set_imported_data(
            lines=(0,), x_data=data[0], y_data=(data[1] + k_corr,),
            )
        dp.main.graph_math.set_imported_data(
            lines=(1,), x_data=data[0], y_data=(data[2] + phi_corr,),
            )

    # Connect Load buttons.
    dp.main.popup_math_scope.ui.pushButtonLoadCSV.clicked.connect(
        __on_load_csv
        )
    dp.main.popup_math_scope.ui.pushButtonLoadFRA.clicked.connect(
        __on_load_fra
        )

    # Connect Clear button (clear lines, imported lines, UI text, and log).
    dp.main.popup_math_scope.ui.pushButtonClear.clicked.connect(
        lambda: dp.main.graph_math.remove_all_lines()
        )
    dp.main.popup_math_scope.ui.pushButtonClear.clicked.connect(
        lambda: dp.main.graph_math.remove_all_imported_lines()
        )
    dp.main.popup_math_scope.ui.pushButtonClear.clicked.connect(
        lambda: dp.main.ui.labelPIDParams.setText('-')
        )
    dp.main.popup_math_scope.ui.pushButtonClear.clicked.connect(
        lambda: dp.logger.info('Clear Math calculations.')
        )

    def __on_synthesize_pid() -> None:
        """
        Synthesize a digital PID regulator
        based on the imported frequency response.
        """

        if len(dp.main.graph_math.imported_lines) < 2:
            return

        line_amp = dp.main.graph_math.imported_lines[0]
        line_phase = dp.main.graph_math.imported_lines[1]

        if (line_amp.x_data is None
                or line_amp.y_data is None
                or line_phase.y_data is None):
            return

        frequencies = line_amp.x_data
        magnitudes = line_amp.y_data
        phases = line_phase.y_data

        try:
            f_s = float(dp.main.ui.lineEditSamplingFrequency.text())
            f_c = float(dp.main.ui.lineEditCrossFrequency.text())
            phi_m = float(dp.main.ui.lineEditPhaseMargin.text())
        except ValueError:
            dp.logger.error(
                'Invalid numeric values for PID synthesis parameters.'
                )
            return

        math_proc = Math(frequencies, magnitudes, phases, f_s)
        k_p, k_i, k_d, m_pid, phi_pid = math_proc.synthesize_pid(f_c, phi_m)

        if m_pid.size == 0:
            dp.logger.warning(
                'PID synthesis failed: requirements cannot be met'
                'or invalid crossover frequency.'
                )
            return

        # Calculate discrete transfer function coefficients.
        b_0 = k_p + k_i + k_d
        b_1 = -2.0 * k_d - k_p
        b_2 = k_d

        reg_type = "PI" if k_d == 0 else "PID"
        name = f'{reg_type} ({f_c:g}, {phi_m:g})'

        # Update UI with formatted numbers
        # (:.6g prevents overly long decimal strings).
        dp.main.ui.labelPIDParams.setText(
            f'{name}\n'
            f'----------\n'
            f'Kp = {k_p:.6g}\nKi = {k_i:.6g}\nKd = {k_d:.6g}\n\n'
            f'b0 = {b_0:.6g}\nb1 = {b_1:.6g}\nb2 = {b_2:.6g}\n'
            f'a1 = -1.0\na2 = 0.0'
        )

        # Calculate open-loop system response.
        at_c = magnitudes + m_pid
        phi_c = phases + phi_pid

        enable_marks = dp.main.ui.pushButtonEnableMathCursors.isChecked()

        # Plot the resulting open-loop response.
        dp.main.graph_math.add_line(
            axis=0, name=name, type_='float32_t',
            address=0, enable_marks=enable_marks,
        )
        dp.main.graph_math.add_line(
            axis=1, name=name, type_='float32_t',
            address=0, enable_marks=enable_marks,
        )

        dp.main.graph_math.set_data(
            lines=(-2,), x_data=frequencies, y_data=(at_c,)
            )
        dp.main.graph_math.set_data(
            lines=(-1,), x_data=frequencies, y_data=(phi_c,)
            )

        dp.logger.info(f'Successfully synthesized {reg_type} regulator.')

    dp.main.ui.pushButtonMathSynthesize.clicked.connect(
        __on_synthesize_pid
        )

    # Save parameters to config when edited.
    dp.main.ui.lineEditSamplingFrequency.editingFinished.connect(
        lambda: dp.config.set_parameter(
            ('math', 'f_s'),
            dp.main.ui.lineEditSamplingFrequency.text(),
            )
        )

    dp.main.ui.lineEditCrossFrequency.editingFinished.connect(
        lambda: dp.config.set_parameter(
            ('math', 'f_c'),
            dp.main.ui.lineEditCrossFrequency.text(),
            )
        )

    dp.main.ui.lineEditPhaseMargin.editingFinished.connect(
        lambda: dp.config.set_parameter(
            ('math', 'phi_m'),
            dp.main.ui.lineEditPhaseMargin.text(),
            )
        )

    def __on_update_corr() -> None:
        """
        Apply amplitude and phase corrections dynamically
        when line edits change.
        """

        if len(dp.main.graph_math.imported_lines) < 2:
            return

        line_amp = dp.main.graph_math.imported_lines[0]
        line_phase = dp.main.graph_math.imported_lines[1]

        if line_amp.y_data is None or line_phase.y_data is None:
            return

        try:
            old_k_corr = float(
                dp.config.get_parameter(('math', 'k_corr')) or 0.0
                )
            old_phi_corr = float(
                dp.config.get_parameter(('math', 'phi_corr')) or 0.0
                )

            new_k_corr = float(
                dp.main.ui.lineEditKCorrection.text() or 0.0
                )
            new_phi_corr = float(
                dp.main.ui.lineEditPhiCorrection.text() or 0.0
                )
        except ValueError:
            return

        # Apply delta correction to the currently displayed data.
        y_amp = line_amp.y_data - old_k_corr + new_k_corr
        y_phase = line_phase.y_data - old_phi_corr + new_phi_corr

        dp.main.graph_math.set_imported_data(
            lines=(0,), x_data=line_amp.x_data, y_data=(y_amp,),
        )
        dp.main.graph_math.set_imported_data(
            lines=(1,), x_data=line_phase.x_data, y_data=(y_phase,),
        )

        # Persist new correction values.
        dp.config.set_parameter(('math', 'k_corr'), str(new_k_corr))
        dp.config.set_parameter(('math', 'phi_corr'), str(new_phi_corr))

    dp.main.ui.lineEditKCorrection.editingFinished.connect(
        __on_update_corr
        )
    dp.main.ui.lineEditPhiCorrection.editingFinished.connect(
        __on_update_corr
        )
