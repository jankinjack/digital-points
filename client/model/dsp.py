import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


def _get_sliding_windows(y_data: np.ndarray, width: int) -> np.ndarray:
    """
    Apply edge padding to the signal and return a sliding window view.

    Args:
        y_data: The 1D input signal array.
        width: The size of the sliding window.

    Returns:
        A 2D view of the sliding windows.
    """

    pad_left = width // 2
    pad_right = (width - 1) // 2

    # 'edge' mode replicates the boundary values.
    y_padded = np.pad(y_data, (pad_left, pad_right), mode='edge')

    return sliding_window_view(y_padded, width)


def median_smooth(y_data: np.ndarray, width: int) -> np.ndarray:
    """
    Apply a 1D Median filter.
    Excellent for removing salt-and-pepper (impulse) noise
    while preserving sharp edges.
    """

    windows = _get_sliding_windows(y_data, width)
    return np.median(windows, axis=1)


def moving_average(y_data: np.ndarray, width: int) -> np.ndarray:
    """
    Apply a Simple Moving Average (SMA) filter.
    Smooths high-frequency noise but tends to blur sharp signal transitions.
    """

    windows = _get_sliding_windows(y_data, width)
    return np.mean(windows, axis=1)


def u_smooth(y_data: np.ndarray, width: int) -> np.ndarray:
    """
    Apply an Upper-smooth (U-smooth) non-linear morphological filter.
    Consists of a moving maximum followed by a moving minimum.
    """

    effective_width = width + 1

    # Step 1: Moving Maximum (Dilation).
    windows = _get_sliding_windows(y_data, effective_width)
    slide_max = np.max(windows, axis=1)

    # Step 2: Moving Minimum (Erosion) applied to the dilated signal.
    windows_max = _get_sliding_windows(slide_max, effective_width)
    return np.min(windows_max, axis=1)


def l_smooth(y_data: np.ndarray, width: int) -> np.ndarray:
    """
    Apply a Lower-smooth (L-smooth) non-linear morphological filter.
    Consists of a moving minimum followed by a moving maximum.
    """

    effective_width = width + 1

    # Step 1: Moving Minimum (Erosion).
    windows = _get_sliding_windows(y_data, effective_width)
    slide_min = np.min(windows, axis=1)

    # Step 2: Moving Maximum (Dilation) applied to the eroded signal.
    windows_min = _get_sliding_windows(slide_min, effective_width)
    return np.max(windows_min, axis=1)


def lu_smooth(y_data: np.ndarray, width: int) -> np.ndarray:
    """
    Apply a compound LU-smooth filter
    (L-smooth followed by U-smooth).
    """
    return l_smooth(u_smooth(y_data, width), width)


def ul_smooth(y_data: np.ndarray, width: int) -> np.ndarray:
    """
    Apply a compound UL-smooth filter
    (U-smooth followed by L-smooth).
    """
    return u_smooth(l_smooth(y_data, width), width)


def lulu_smooth(y_data: np.ndarray, width: int) -> np.ndarray:
    """
    Apply a cascaded LULU-smooth filter
    for aggressive impulse noise removal.
    """

    return lu_smooth(lu_smooth(y_data, width), width)


def ulul_smooth(y_data: np.ndarray, width: int) -> np.ndarray:
    """ Apply a cascaded ULUL-smooth filter
    for aggressive impulse noise removal.
    """

    return ul_smooth(ul_smooth(y_data, width), width)
