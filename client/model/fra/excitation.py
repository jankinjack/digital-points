from typing import Callable, Optional
import numpy as np


def single_sine_signal(
    amplitude: float | int,
    num_points: int,
    period: Optional[float | int] = None,
    harmonic: int = 1,
    divisor: int = 1
) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate a single sine wave signal.

    Args:
        amplitude: Peak amplitude of the sine wave.
        num_points: Base number of points in the signal.
        period: Time period of the signal. If None, time array is empty.
        harmonic: Harmonic multiplier for the frequency.
        divisor: Step divisor for downsampling the generated signal.

    Returns:
        A tuple containing the signal array and the time array.
    """
    total_points = num_points * divisor

    if period is not None:
        time_array = np.arange(
            0, period, period / total_points,
            dtype=np.float64
            )
    else:
        time_array = np.empty(0, dtype=np.float64)

    # Generate the sine wave and apply the divisor step.
    phase = 2 * np.pi * np.arange(
        0, total_points * harmonic, harmonic
        ) / total_points
    signal = amplitude * np.sin(phase)[::divisor]

    return signal, time_array[::divisor]


def multi_sine_signal(
    amplitudes: np.ndarray,
    num_points: int,
    period: float | int,
    harmonics: np.ndarray,
    progress_callback: Callable[[float], None] = lambda _: None
) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate a multi-sine signal with minimized crest factor using
    the Levenberg-Marquardt algorithm (Schroeder's method variant).

    Args:
        amplitudes: Array of amplitudes for each harmonic.
        period: Time period of the signal.
        harmonics: Array of harmonic indices.
        num_points: Number of points in the time array.
        progress_callback: Function to report progress (0-100%).

    Returns:
        A tuple containing the optimized signal array and the time array.
    """

    # Exclude the first harmonic=.
    ku_all = harmonics[1:]
    a_all = amplitudes[1:]
    num_harmonics = len(ku_all)

    # Calculate power 'q' for crest factor minimization heuristic.
    p = 2**(int(round((num_points - 1) / harmonics[-1] * 2)) - 1).bit_length()
    q = p // 2

    # Create time array.
    time_array = np.arange(0, period, period / num_points, dtype=np.float64)

    # Initialize Levenberg-Marquardt damping matrix (positive-definite).
    lm_damping = np.diag(np.full(num_harmonics, 0.1, dtype=np.float64))

    min_crest_factor = np.inf
    crest_factor = np.inf
    best_signal = np.zeros_like(time_array)

    # Precompute constants to avoid redundant calculations inside loops.
    omega_all = (2 * np.pi / period) * np.array(ku_all, dtype=np.float64)
    omega_t = (2 * np.pi / period) * time_array
    omega_t_all = np.outer(time_array, omega_all)
    fundamental_signal = amplitudes[0] * np.cos(omega_t)

    num_iterations = 500
    max_gauss_newton_steps = 1000
    convergence_threshold = 0.05

    for i in range(num_iterations):
        progress_callback(i / num_iterations * 100)

        # Initialize random phases for this iteration.
        phases = 2 * np.pi * np.random.rand(num_harmonics)

        # Compute the initial excitation signal for this iteration.
        signal = fundamental_signal + np.cos(omega_t_all + phases) @ a_all

        # Compute initial Jacobian matrix.
        x_qm1 = -q * signal ** (q - 1)
        jacobian = x_qm1[:, np.newaxis] * np.sin(omega_t_all + phases)

        prev_crest_factor = None

        for _ in range(max_gauss_newton_steps):
            # Gauss-Newton step with Levenberg-Marquardt regularization.
            jtj_lm = jacobian.T @ jacobian + lm_damping
            x_q = signal ** q
            jt_xq = jacobian.T @ x_q

            phases -= np.linalg.solve(jtj_lm, jt_xq)

            # Update the excitation signal with new phases.
            cos_ph = np.cos(omega_t_all + phases)
            signal = fundamental_signal + cos_ph @ a_all

            # Compute Crest Factor (CF): Peak Amplitude / RMS.
            peak_amplitude = np.ptp(signal) / 2

            # Add epsilon to prevent division by zero
            # if signal becomes completely flat.
            rms = np.sqrt(np.mean(signal ** 2)) + np.finfo(np.float64).eps
            crest_factor = peak_amplitude / rms

            # Check for convergence
            if (prev_crest_factor is not None
                    and abs((crest_factor - prev_crest_factor) / prev_crest_factor) < convergence_threshold):
                break

            prev_crest_factor = crest_factor

            # Update Jacobian matrix for the next step.
            x_qm1 = -q * signal ** (q - 1)
            jacobian = x_qm1[:, np.newaxis] * np.sin(omega_t_all + phases)

        # Evaluate the best signal after the inner optimization loop finishes.
        if crest_factor < min_crest_factor:
            min_crest_factor = crest_factor
            best_signal = signal

    progress_callback(100)

    return best_signal, time_array
