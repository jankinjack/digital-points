
import os
import platform
from typing import Optional
from contextlib import suppress

import numpy as np

from PySide6.QtCore import Qt, QObject, Slot, Signal

import pyqtgraph as pg

import __main__

from model.axis import Axis
from model.line import Line
from model.dsp import (
    median_smooth,
    u_smooth,
    l_smooth,
    lu_smooth,
    ul_smooth,
    lulu_smooth,
    ulul_smooth,
    moving_average,
    )


DICT_MATH_FUNCTIONS = {
    'sin': np.sin,
    'cos': np.cos,
    'tan': np.tan,
    'arcsin': np.arcsin,
    'arccos': np.arccos,
    'arctan': np.arctan,
    'arctan2': np.arctan2,
    'degrees': np.degrees,
    'radians': np.radians,
    # 'unwrap': np.unwrap,
    'deg2rad': np.deg2rad,
    'rad2deg': np.rad2deg,
    'sinh': np.sinh,
    'cosh': np.cosh,
    'tanh': np.tanh,
    'arcsinh': np.arcsinh,
    'arccosh': np.arccosh,
    'arctanh': np.arctanh,
    'round': np.round,
    # 'around': np.around,
    # 'rint': np.rint,
    'fix': np.fix,
    'floor': np.floor,
    'ceil': np.ceil,
    'trunc': np.trunc,
    # 'cumprod': np.cumprod,
    'cumsum': np.cumsum,
    'gradient': np.gradient,
    'exp': np.exp,
    # 'expm1': np.expm1,
    # 'exp2': np.exp2,
    'log': np.log,
    'log10': np.log10,
    'log2': np.log2,
    # 'log1p': np.log1p,
    'i0': np.i0,
    'sinc': np.sinc,
    # 'spacing': np.spacing,
    # 'add': np.add,
    # 'reciprocal': np.reciprocal,
    # 'positive': np.positive,
    # 'negative': np.negative,
    # 'multiply': np.multiply,
    # 'divide': np.divide,
    # 'power': np.power,
    # 'fmod': np.fmod,
    'mod': np.mod,
    'remainder': np.remainder,
    # 'angle': np.angle,
    # 'real': np.real,
    # 'imag': np.imag,
    # 'conj': np.conj,
    # 'conjugate': np.conjugate,
    'maximum': np.maximum,
    'minimum': np.minimum,
    'clip': np.clip,
    'sqrt': np.sqrt,
    'cbrt': np.cbrt,
    'square': np.square,
    'absolute': np.absolute,
    'abs': np.abs,
    'sign': np.sign,
    'heaviside': np.heaviside,
    # 'real_if_close': np.real_if_close,

    # Custom DSP filters.

    'median_f': median_smooth,
    'l_f': l_smooth,
    'u_f': u_smooth,
    'lu_f': lu_smooth,
    'ul_f': ul_smooth,
    'lulu_f': lulu_smooth,
    'ulul_f': ulul_smooth,
    'ma_f': moving_average,
    '^': '**',
    }


class GraphView(QObject):
    """
    Manages a collection of plot axes, lines, and real-time data updates.
    Acts as a bridge between the background data acquisition thread
    and the GUI.
    """

    __slots__ = (
        '_widget',
        '_axes',
        '_share_objects',
        '_lines',
        '_imported_lines',
        '_number_lines',
        )

    number_lines_changed = Signal(int)

    def __init__(
            self,
            widget: pg.GraphicsLayoutWidget,
            axes_num: int = 1,
            x_scale: str = 'linear',
            disable_autorange: bool = False,
            selectable_points: bool = False,
            x_unit: str = '',
            y_unit: str = '',
            enable_y2: bool = False,
            enable_cursors: bool = True,
            *args,
            **kwargs,
            ) -> None:
        super().__init__(*args, **kwargs)

        self._widget = widget
        self._widget.setBackground('#f8f8f2')
        self._widget.ci.layout.setContentsMargins(3, 3, 3, 3)
        self._widget.ci.layout.setSpacing(3)

        # Initialize axes.
        self._axes = tuple(
            Axis(
                x_scale,
                disable_autorange,
                selectable_points,
                x_unit,
                y_unit,
                enable_y2,
                enable_cursors,
                ) for i in range(axes_num)
            )

        # Link all x-axes to the first one for synchronized panning/zooming.
        for axis in self._axes[1:]:
            axis.setXLink(self._axes[0])

        for i, axis in enumerate(self._axes):
            self._widget.addItem(
                axis, row=i, col=0, rowspan=1, colspan=1,
                )

        # Create share objects between the scope view and serial interface.
        self._share_objects = []

        self._lines = []
        self._imported_lines = []
        self._number_lines = 0

    @property
    def share_objects(self) -> list[tuple[int, int]]:
        return self._share_objects

    @property
    def number_lines(self) -> int:
        return self._number_lines

    @property
    def axes(self) -> tuple[Axis, ...]:
        return self._axes

    @property
    def lines(self) -> list[Line]:
        return self._lines

    @property
    def imported_lines(self) -> list[Line]:
        return self._imported_lines

    def build_share_objects_and_lines(self) -> None:
        """
        Rebuild the flat lists of shared objects
        and lines from all axes.
        """

        self._lines = [line for ax in self._axes for line in ax.lines]
        self._share_objects = [
            (line.type_, line.address) for line in self._lines
            ]

    def add_line(
            self,
            axis: int,
            name: str,
            type_: str,
            address: int,
            y_axis: str = 'y',
            show_symbols: bool = False,
            drag_limits: Optional[list | tuple] = None,
            imported: bool = False,
            enable_marks: bool = False,
            ) -> Line:
        """ Add a new line to the specified axis. """

        line = self._axes[axis].add_line(
            name=name,
            type_=type_,
            address=address,
            y_axis=y_axis,
            show_symbols=show_symbols,
            drag_limits=drag_limits,
            imported=imported,
            enable_marks=enable_marks,
            )

        if not imported:
            self.build_share_objects_and_lines()
            self._number_lines += 1
            self.number_lines_changed.emit(self._number_lines)
        else:
            self._imported_lines.append(line)

        return line

    def remove_line(
            self,
            axis: int,
            name: Optional[str] = None,
            address: Optional[int] = None,
            ) -> None:
        """ Remove a specific line from the specified axis. """

        self._axes[axis].remove_line(name=name, address=address)

        self.build_share_objects_and_lines()
        self._number_lines -= 1
        self.number_lines_changed.emit(self._number_lines)

        self._update_cursor_bounds(
            empty=self._number_lines == 0 and len(self._imported_lines) == 0
            )

    def remove_all_lines(self) -> None:
        """ Remove all non-imported lines from all axes. """

        for axis in self._axes:
            axis.remove_all_lines()

        self._share_objects = []
        self._lines = []

        self._number_lines = 0
        self.number_lines_changed.emit(self._number_lines)

        self._update_cursor_bounds(empty=len(self._imported_lines) == 0)

    def remove_all_imported_lines(self) -> None:
        """ Remove all imported lines from all axes. """

        for axis in self._axes:
            axis.remove_all_imported_lines()

        self._imported_lines = []

        self._update_cursor_bounds(empty=self._number_lines == 0)

    @Slot(int, np.ndarray, np.ndarray, bool, int)
    def set_data(
            self,
            lines: tuple[int, ...] | list[int] | range,
            x_data: np.ndarray,
            y_data: np.ndarray,
            math: bool = False,
            dump: int = -2,
            ) -> None:
        """
        Update data for the specified lines.
        Applies user-defined mathematical expressions if enabled.
        """
        num_lines = len(self._lines)
        if not all(-num_lines <= n < num_lines for n in lines):
            return

        math_vars = {}
        if math:
            # Create base variables x1, x2... and 't' only once
            math_vars = {f'x{j+1}': y_data[k] for k, j in enumerate(lines)}
            math_vars['t'] = x_data

        # Pre-compile safe globals
        # to prevent arbitrary code execution via eval().
        safe_globals = {"__builtins__": {}}
        safe_globals.update(DICT_MATH_FUNCTIONS)

        # Update line data
        for i, l in enumerate(lines):
            line = self._lines[l]

            if math and line.expression != 'x':
                # Update 'x' on the fly to avoid creating
                # a new dict on each iteration.
                math_vars['x'] = y_data[i]
                try:
                    y = eval(
                        line.expression_compiled,
                        safe_globals,
                        math_vars,
                    )
                except Exception:
                    y = y_data[i]
            else:
                y = y_data[i]

            line.data = (x_data, y)

        # Handle dump markers and text items
        if dump == -1:
            for axis in self.axes:
                for dump_text in axis.dump_texts:
                    axis.removeItem(dump_text)

                axis.dump_texts.clear()
                axis.dump_line.setData([], [])

        elif dump >= 0:
            # OS check and resource preparation.
            is_windows = platform.system() == 'Windows'

            if is_windows:
                dump_dir = __main__.FULL_PATH / 'dumps'
                with suppress(FileExistsError):
                    dump_dir.mkdir()
                dump_dir_str = str(dump_dir)

                def __on_link_clicked(link: str) -> None:
                    with suppress(FileNotFoundError):
                        os.startfile(link)

            # Array slices and zeros.
            x_slice = x_data[:dump+2]
            zeros = np.zeros(dump+2)

            for axis in self.axes:
                dump_text = pg.TextItem(
                    color='k',
                    fill=(255, 255, 255, 150),
                    anchor=(1, 0),
                )

                if is_windows:
                    dump_text.setHtml(f'<a href="{dump_dir_str}">dump_{dump}.csv</a>')
                    dump_text.textItem.setOpenExternalLinks(False)
                    dump_text.textItem.setTextInteractionFlags(Qt.TextBrowserInteraction)
                    dump_text.textItem.linkActivated.connect(__on_link_clicked)
                else:
                    dump_text.setText(f'dump_{dump}.csv')

                dump_text.setPos(x_data[dump+1], 0)
                axis.addItem(dump_text, ignoreBounds=True)

                axis.dump_line.setData(x_slice, zeros)
                axis.dump_texts.append(dump_text)

        self._update_cursor_bounds(empty=False)

    def set_imported_data(
            self,
            lines: tuple[int, ...],
            x_data: np.ndarray,
            y_data: tuple[np.ndarray, ...],
            ) -> None:
        """ Update data for imported lines. """

        num_imported = len(self._imported_lines)
        if not all(-num_imported <= line < num_imported for line in lines):
            return

        for i, l in enumerate(lines):
            self._imported_lines[l].data = (x_data, y_data[i])

        self._update_cursor_bounds(empty=False)

    def _update_cursor_bounds(self, empty: bool) -> None:
        """
        Update the movable bounds for cursors
        based on the current data view.
        """

        for axis in self.axes:
            if not axis.cursors:
                continue

            if empty:
                axis_bounds = (0.1, 0.9)
            else:
                view_box = axis.getViewBox()
                axis_bounds = view_box.childrenBounds()[0] if view_box else None

                if axis_bounds is None:
                    axis_bounds = (0.1, 0.9)

            axis.cursors[0].setBounds(axis_bounds)
            axis.cursors[1].setBounds(axis_bounds)

    def update_lines(self) -> None:
        """ Update (periodically) the line after data change. """

        for axis in self.axes:
            axis.update_lines()

    def enable_grid(self, enable: bool = True) -> None:
        """ Enable/disable grid for all axes. """

        for axis in self.axes:
            axis.showGrid(x=enable, y=enable, alpha=0.3)
