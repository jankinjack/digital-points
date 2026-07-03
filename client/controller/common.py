
import re
import threading
from contextlib import contextmanager, suppress
from typing import Any, Iterator

from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QMainWindow,
    QTableWidget,
    QAbstractItemView,
    )


def chunks(list_: list[Any] | tuple[Any, ...], chunk_size: int) -> Iterator[Any]:
    """ Yield successive 'chunk_size'-sized chunks from 'list_'. """

    for i in range(0, len(list_), chunk_size):
        yield list_[i:i + chunk_size]


@contextmanager
def nonblocking(lock: threading.Lock) -> Iterator[bool]:
    """
    Context manager for acquiring a lock without blocking the thread.
    Yields True if the lock was successfully acquired, False otherwise.
    """

    locked = lock.acquire(False)
    try:
        yield locked
    finally:
        if locked:
            lock.release()


def get_regex_and_dims_from_array_name(name: str) -> tuple[str, list[str]]:
    """
    Generate a RegExp pattern to validate array indices
    against their maximum dimensions.
    """

    dims = get_dims_from_array_name(name)
    regex_parts = []

    for dim_str in dims:
        alternatives = []
        for i, digit_char in enumerate(dim_str):
            digit_val = int(digit_char)
            if digit_val > 0:
                prefix = dim_str[:i]

                # Match digits from 0 up to (current_digit - 1).
                range_pattern = f"[0-{digit_val - 1}]"

                # The '?[0-9]' makes the trailing digits optional,
                # allowing shorter numbers (e.g., matching '5'
                # when dimension is '25').
                opt_suffix = r"?[0-9]" * (len(dim_str) - i - 1)

                alternatives.append(f"{prefix}{range_pattern}{opt_suffix}")

        # Wrap the alternatives in a non-capturing group (?:...).
        if alternatives:
            regex_parts.append(r"(?:" + "|".join(alternatives) + r")")
        else:
            # Fallback for dimension '0'.
            regex_parts.append(r"0")

    # Join dimensions with comma or dot separators, allowing optional spaces
    return r"[,.][ ]*".join(regex_parts), dims


def get_dims_from_array_name(name: str) -> list[Any]:
    """ Extract array dimensions from a string representation. """

    return re.findall(r'\[(\d+)\]', name)


def get_array_item_name_and_offset(
        name: str,
        index: tuple | list,
        type_: str,
        ) -> tuple[str, int]:
    """
    Calculate the memory offset and formatted name
    for a specific item in a multi-dimensional array.
    """

    indices, dimensions = index[0], index[1]

    # Calculate address offset for the array's item.
    coeff = [1]
    for dim in reversed(dimensions[1:]):
        coeff.append(dim * coeff[-1])

    from model.line import VAR_TYPE_CODE
    from model.elf_file_parser import ARCH_BYTESIZE
    from model.interface.interface_base import PACK_SIZE

    # Get type size in bytes.
    type_code = VAR_TYPE_CODE.get(type_, VAR_TYPE_CODE['uint32_t'])
    type_size = PACK_SIZE[type_code][1]

    # Calculate linear index and final offset.
    linear_index = sum(i * c for i, c in zip(reversed(indices), coeff))
    offset = (type_size * linear_index * 8) // ARCH_BYTESIZE

    # Format the name with selected indexes.
    base_name = name.split('[', 1)[0]
    indices_str = ''.join(f'[{i}]' for i in indices)

    return f"{base_name}{indices_str}", offset


def add_drag_handlers(window: QMainWindow) -> None:
    """
    Attach drag-and-drop handlers to the window's top frame
    for moving frameless windows.
    WARNING: This uses monkey-patching
    which overrides existing mouse eventson the widget.
    """

    def on_mouse_pressed(event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            window.pos_mouse_pressed = event.globalPosition().toPoint()

    def on_mouse_moved(event: QMouseEvent) -> None:
        if (event.buttons() & Qt.LeftButton) and hasattr(window, 'pos_mouse_pressed'):
            delta = event.globalPosition().toPoint() - window.pos_mouse_pressed
            window.move(window.pos() + delta)
            window.pos_mouse_pressed = event.globalPosition().toPoint()

    with suppress(AttributeError):
        # Moving a frameless modules pressing mouse on the top center frame.
        window.ui.frameTop_1.mousePressEvent = on_mouse_pressed
        window.ui.frameTop_1.mouseMoveEvent = on_mouse_moved


def select_variable_in_table(table: QTableWidget, var: str) -> None:
    """ Find and select a variable in a table, scrolling it into view. """

    found_items = table.findItems(
        var,
        Qt.MatchContains | Qt.MatchCaseSensitive,
        )

    if found_items:
        table.clearSelection()
        table.selectRow(found_items[0].row())
        table.scrollToItem(
            found_items[0],
            QAbstractItemView.PositionAtTop,
            )
