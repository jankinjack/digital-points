import numpy as np


class FFT:
    """
    A class to compute and store the Fast Fourier Transform (FFT) of a signal.
    Provides properties to access frequency, complex spectrum, amplitude,
    magnitude (in dB), and phase.
    """

    __slots__ = (
        '_frequency',
        '_complex',
        '_amplitude',
        '_magnitude',
        '_phase'
    )

    def __init__(
        self,
        y_data: np.ndarray,
        sampling_frequency: float | int
    ) -> None:
        """
        Initialize the FFT object.

        Args:
            y_data: Signal amplitude array to be transformed.
            num_points: Total number of samples used to compute the FFT.
            sampling_frequency: Sampling frequency of the signal (Fs) in Hz.
        """

        num_points = y_data.shape[-1]

        # Compute the frequency bins (excludes DC component at 0 Hz).
        self._frequency = np.fft.rfftfreq(
            num_points, d=1.0/sampling_frequency
            )[1:]

        # Compute the FFT.
        fft_result = np.fft.rfft(y_data)

        # Handle potential 2D input arrays (e.g., shape (1, N))
        # by extracting the first row.
        if fft_result.ndim > 1:
            fft_result = fft_result[0]

        # Normalize the complex spectrum by the total number of points
        self._complex = fft_result[1:] / num_points

        self._amplitude = np.abs(self._complex)

        with np.errstate(divide='ignore'):
            self._magnitude = 20 * np.log10(self._amplitude)

        # np.angle already returns values in [-180, 180],
        # but the modulo operation ensures strict wrapping
        # in case of any floating-point edge cases.
        self._phase = (np.angle(self._complex, deg=True) + 180) % 360 - 180

    @property
    def complex_(self) -> np.ndarray:
        """ Return the complex frequency spectrum. """

        return self._complex

    @property
    def frequency(self) -> np.ndarray:
        """ Return the array of frequency bins. """

        return self._frequency

    @property
    def amplitude(self) -> np.ndarray:
        """
        Return the amplitude spectrum
        (absolute value of the complex spectrum).
        """

        return self._amplitude

    @property
    def magnitude(self) -> np.ndarray:
        """ Return the magnitude spectrum in decibels (dB)."""

        return self._magnitude

    @property
    def phase(self) -> np.ndarray:
        """
        Return the phase spectrum in degrees,
        strictly wrapped to the [-180, 180] range.
        """

        return self._phase
