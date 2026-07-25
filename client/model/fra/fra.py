
import numpy as np

from model.fra.fft import FFT


class FRA():
    """
    Frequency Response Analysis (FRA) processor.
    Computes and averages FFT spectra for input/output signals 
    and calculates the system's frequency response.
    """

    __slots__ = (
        '_a_fft_complex',
        '_b_fft_complex',
        '_sampling_frequency',
        '_harmonic_indices',
        '_average_type',
        '_num_repeats',
        )

    def __init__(
            self,
            sampling_frequency: float | int,
            harmonic_indices: np.ndarray | list[int] | tuple[int, ...],
            average_type: str,
            num_repeats: int
            ) -> None:

        self._sampling_frequency = sampling_frequency
        self._harmonic_indices = np.asarray(harmonic_indices)
        self._average_type = average_type
        self._num_repeats = num_repeats

        num_harmonics = len(self._harmonic_indices)

        # Initialize complex arrays
        # to prevent implicit type casting during accumulation.
        self._a_fft_complex = np.zeros(num_harmonics, dtype=np.complex128)
        self._b_fft_complex = np.zeros(num_harmonics, dtype=np.complex128)

    def add_data(self, y_a_data: np.ndarray, y_b_data: np.ndarray) -> None:
        """
        Process a new pair of input/output signals
        and update the averaged spectra.

        Args:
            y_a_data: Input (excitation) signal array.
            y_b_data: Output (response) signal array.
        """

        # Compute FFT and extract bins at the specified harmonic indices.
        a_fft = FFT(y_a_data, self._sampling_frequency).complex_[
            self._harmonic_indices-1
            ]
        b_fft = FFT(y_b_data, self._sampling_frequency).complex_[
            self._harmonic_indices-1
            ]

        if self._average_type == 'Vector Averaging':
            self._a_fft_complex += a_fft / self._num_repeats
            self._b_fft_complex += b_fft / self._num_repeats
        elif self._average_type == 'Exponential Averaging':
            weight_old = (self._num_repeats - 1) / self._num_repeats
            weight_new = 1.0 / self._num_repeats

            self._a_fft_complex = self._a_fft_complex * weight_old + a_fft * weight_new
            self._b_fft_complex = self._b_fft_complex * weight_old + b_fft * weight_new

    @property
    def response_complex(self) -> np.ndarray:
        """ Complex frequency response (Output / Input). """

        return self._b_fft_complex / self._a_fft_complex

    @property
    def response_amplitude(self) -> np.ndarray:
        """ Amplitude of the frequency response. """

        return np.abs(self.response_complex)

    @property
    def response_magnitude(self) -> np.ndarray:
        """ Magnitude of the frequency response in decibels (dB). """

        with np.errstate(divide='ignore', invalid='ignore'):
            return 20*np.log10(self.response_amplitude)

    @property
    def response_phase(self) -> np.ndarray:
        """
        Phase of the frequency response in degrees,
        wrapped to [-180, 180].
        """

        return (np.rad2deg(np.angle(self.response_complex)) + 180) % 360 - 180

    @staticmethod
    def sse_parameters_from_frequency_range(
            f_min: float | int,
            f_max: float | int,
            n_freq: int,
            n_max: int,
            f_s: float | int,
            freq_distrib: str,
            ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Calculate Single-Sine Excitation (SSE) parameters: frequencies,
        number of points, decimation factors, and harmonics.
        """

        def _h_const(
                f_min: float | int,
                f_max: float | int,
                n_freq: int,
                n_max: int,
                f_s: float | int,) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
            """ Constant harmonics. """

            # Initial calculation of the number of points
            # and frequencies with logarithmic spacing.
            f = np.geomspace(f_min, f_max, num=n_freq)
            n = np.maximum(np.floor(f_s / f + 0.5), 1).astype(np.uint64)

            # Calculate decimation factors.
            d = np.maximum(np.ceil(n / n_max), 1).astype(np.uint64)

            # Recalculate the number of points accounting for decimation.
            n = np.maximum(np.floor(n / d.astype(np.float64) + 0.5), 1).astype(np.uint64)

            # Recalculate frequencies.
            f = f_s / (n * d)

            # Calculate harmonic numbers.
            # For this method, all harmonics are unity.
            h = np.ones(n_freq).astype(np.uint64)

            # Get the frequencies, number of samples,
            # decimation coefficients, and harmonics.
            return f, n, d, h

        def _h_var(
                f_min: float | int,
                f_max: float | int,
                n_freq: int,
                n_max: int,
                f_s: float | int,
                ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
            """ Variable harmonics. """

            # Initial calculation of the number of points
            # and frequencies with logarithmic spacing.
            f = np.geomspace(f_min, f_max, num=n_freq)
            n_base = np.maximum(np.floor(f_s / f + 0.5), 1).astype(np.uint64)

            # Mask for the number of points exceeding the maximum.
            mask = n_base > n_max
            inv_mask = ~mask

            # Initialize decimation factors and harmonic numbers.
            d = np.ones(n_freq, dtype=np.uint64)
            h = np.ones(n_freq, dtype=np.uint64)

            n = n_base.copy()

            # If the number of points exceeds the limit, calculate decimation.
            d[mask] = np.ceil(n_base[mask] / n_max).astype(np.uint64)
            n[mask] = np.ceil(n_base[mask] / d[mask]).astype(np.uint64)
            f[mask] = f_s / (n[mask] * d[mask])

            # If the number of points is below the limit,
            # calculate harmonic numbers.
            h[inv_mask] = np.maximum(
                np.floor(n_max / n_base[inv_mask]), 1
                ).astype(np.uint64)
            n[inv_mask] = np.floor(
                h[inv_mask] * n_base[inv_mask] + 0.5
                ).astype(np.uint64)
            f[inv_mask] = (h[inv_mask] * f_s) / n[inv_mask]

            # Recalculate the number of points.
            n = np.maximum(np.floor(n + 0.5), 1).astype(np.uint64)

            # Get the frequencies, number of samples,
            # decimation coefficients, and harmonics.
            return f, n, d, h

        n_max_half = np.floor(n_max/2)

        if freq_distrib and freq_distrib == 'h=1 Frequency Distribution':
            return _h_const(f_min, f_max, n_freq, n_max_half, f_s)
        else:
            return _h_var(f_min, f_max, n_freq, n_max_half, f_s)

    @staticmethod
    def mse_parameters_from_frequency_range(
            f_min: float | int,
            f_max: float | int,
            n_freq: int,
            n_max: int,
            f_s: float | int,
            freq_distrib: str,
            ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Calculate Multi-Sine Excitation (MSE) parameters.
        Returns frequencies, number of points,
        decimation factors, and harmonics.
        """

        n_max_half = np.floor(n_max / 2)

        # Calculate the decimation factor.
        d = np.maximum(np.ceil(f_s / f_min / n_max_half), 1).astype(np.uint64)

        # Recalculate the number of points.
        n_max_half = np.round(f_s / f_min / d).astype(np.uint64)

        # Calculate the maximum harmonic.
        h_max = int(min(n_max_half / 2, f_max / f_min / 2))

        # Generate an array of harmonics with logarithmic spacing.
        h = np.unique(np.rint(np.geomspace(1, h_max, num=n_freq)).astype(np.uint64))

        # Recalculate the decimation factor.
        d = np.full(len(h), d, dtype=np.uint64)

        # Calculate the number of points and frequencies.
        n = np.full(len(h), n_max_half, dtype=np.uint64)
        f = f_s / (d * n) * h

        return f, n, d, h
