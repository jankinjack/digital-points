
import numpy as np


class Math():
    """
    Mathematical utility class for control system analysis.
    Currently provides digital PID regulator synthesis based on
    Frequency Response Analysis (FRA) data.
    """

    __slots__ = (
        '_frequencies',
        '_amplitudes',
        '_phases',
        '_f_s',
        )

    def __init__(
            self,
            frequencies: np.ndarray,
            magnitudes: np.ndarray,
            phases: np.ndarray,
            f_s: float | int,
            ) -> None:

        self._frequencies = frequencies

        # Convert dB to linear amplitude and degrees to radians.
        self._amplitudes = 10.0 ** (magnitudes / 20.0)
        self._phases = np.deg2rad(phases)
        self._f_s = float(f_s)

    def synthesize_pid(
            self,
            f_c: float | int,
            phi_m: float | int,
            ) -> tuple[float, float, float, np.ndarray, np.ndarray]:
        """
        Synthesize a digital PID regulator using the frequency-domain approach.

        Args:
            f_c: Desired crossover frequency (Hz).
            phi_m: Desired phase margin (degrees).

        Returns:
            A tuple containing:
                (Kp, Ki, Kd, magnitude_response_dB, phase_response_deg).
            Returns zeros and empty arrays
            if synthesis is mathematically impossible.
        """

        # Guard against empty frequency arrays or invalid crossover frequencies
        if (self._frequencies.size == 0 or
                f_c >= self._frequencies[-1] or
                f_c >= self._f_s / 2):
            return 0, 0, 0, np.empty(0, dtype=np.float64), np.empty(0, dtype=np.float64)

        # Base pre-warping frequency parameter.
        w_p = 2 * self._f_s

        # Convert desired phase margin from degrees to radians.
        phi_m = np.deg2rad(phi_m)

        # Convert desired crossover frequency from Hz to rad/s.
        w_c = 2 * np.pi * f_c

        def _interpolate_plant(f_val: float) -> tuple[float, float]:
            """ Interpolate plant amplitude and phase at a given frequency. """

            amp_interp = float(np.interp(
                f_val, self._frequencies, self._amplitudes
                ))
            phase_interp = float(np.interp(
                f_val, self._frequencies, self._phases
                ))
            return amp_interp, phase_interp

        # Pre-warp the crossover frequency using Tustin's approximation base.
        w_c_wr = w_p * np.tan(w_c / w_p)
        f_c_wr = w_c_wr / (2 * np.pi)

        # Get plant amplitude and phase at the pre-warped crossover frequency.
        at_u_c, phi_u_c = _interpolate_plant(f_c_wr)

        # Calculate the required phase contribution from the controller.
        phi_m_u = np.pi + phi_u_c

        # Determine regulator type (PI or PID)
        # based on phase margin requirements.
        if phi_m_u - np.arctan(w_p / w_c_wr) < phi_m < phi_m_u:
            # PI Regulator synthesis
            w_pi = w_c_wr * np.tan(phi_m_u - phi_m)
            w_pd = w_p
            k_pid = 1/at_u_c / np.sqrt(1 + (w_pi/w_c_wr)**2)
        elif phi_m_u <= phi_m < phi_m_u + np.pi/2 - np.arctan(w_c_wr / w_p):
            # PID Regulator synthesis
            # Note: '20.0' is an empirical tuning factor
            # for the integral zero placement.
            w_pi = w_c_wr / 20
            w_pd = w_c_wr / np.tan(
                phi_m - phi_m_u + np.arctan(w_c_wr / w_p)
                )
            k_pid = 1/at_u_c * np.sqrt(
                (1 + (w_c_wr / w_p)**2) / (1 + (w_c_wr / w_pd)**2)
                )
        else:
            # Phase margin requirements cannot be met with this plant model.
            return 0, 0, 0, np.array([]), np.array([])

        # Compute the discrete-time regulator coefficients (Kp, Ki, Kd).
        k_p = k_pid * (1 + w_pi/w_pd - 2*w_pi/w_p)
        k_i = 2 * k_pid * w_pi/w_p
        k_d = k_pid/2 * (1 - w_pi/w_p) * (w_p/w_pd - 1)

        # Compute the regulator's frequency response in the Z-domain
        # Suppress warnings for division by zero at DC (f=0, z=1) where
        # the integrator gain is mathematically infinite.
        with np.errstate(divide='ignore', invalid='ignore'):
            z = np.exp(2j * np.pi * self._frequencies / self._f_s)

            g_pid_z = k_p + k_i / (1 - 1/z) + k_d * (1 - 1/z)
            m_pid = 20 * np.log10(np.abs(g_pid_z))
            phi_pid = np.angle(g_pid_z, deg=True)

        return k_p, k_i, k_d, m_pid, phi_pid
