
import threading
from typing import Optional
from types import CodeType

import numpy as np

import pyqtgraph as pg

from PySide6.QtCore import Signal

from controller.common import nonblocking

# Mapping of variable types to their internal integer codes.
VAR_TYPE_CODE = {
    'int8_t': 0,
    'uint8_t': 1,
    'int16_t': 2,
    'uint16_t': 3,
    'int32_t': 4,
    'uint32_t': 5,
    'int64_t': 6,
    'uint64_t': 7,
    'float32_t': 8,
    'float64_t': 9,

    'fra_t': 10,
    'immediate_t': 11,

    'none': 12,
    }

# Mapping of variable types to their general mathematical category.
VAR_TYPE_INT_FLOAT = {
    'int8_t': 'integer',
    'uint8_t': 'integer',
    'int16_t': 'integer',
    'uint16_t': 'integer',
    'int32_t': 'integer',
    'uint32_t': 'integer',
    'int64_t': 'integer',
    'uint64_t': 'integer',
    'float32_t': 'float',
    'float64_t': 'float',

    'fra_t': 'integer',
    'immediate_t': 'float',

    'none': 'none',
    }


class Line(pg.PlotDataItem):
    """
    Custom plot line class extending pyqtgraph's PlotDataItem.
    Manages data plotting, marker points, and mathematical expressions.
    """

    __slots__ = (
        '_y_axis',
        '_type',
        '_type_str',
        '_address',
        '_expression',
        '_expression_compiled',
        '_mark_points',
        '_drag_limits',
        '_imported',
        '_y_data',
        '_color',
        '_color_str',
        '_mutex',
        '_data_buf',
        '_needs_update',
        )

    dragged = Signal(int)

    def __init__(
            self,
            name: str,
            type_: str,
            address: int,
            y_axis: str = 'y',
            color: tuple[int, int, int] = (0, 0, 0),
            show_symbols: bool = False,
            drag_limits: Optional[list | tuple] = None,
            imported: bool = False,
            enable_marks: bool = False,
            *args, **kwargs,
            ) -> None:

        # Configure pyqtgraph rendering options for performance.
        base_kwargs = {
            'name': name,
            'skipFiniteCheck': True,
            'clipToView': True,
            'useCache': True,
        }

        if show_symbols:
            base_kwargs.update({
                'symbol': 'o',
                'symbolPen': color,
                'symbolBrush': color,
                'symbolSize': 8,
            })

        super().__init__(*args, **base_kwargs, **kwargs)

        # Downsample data to improve rendering performance on large datasets.
        self.setDownsampling(auto=True, method='peak')

        self.setPen({'color': color, 'width': 0})

        self._data_buf = ([], [])

        self._y_axis = y_axis
        self._type = VAR_TYPE_CODE.get(type_, VAR_TYPE_CODE['uint32_t'])
        self._type_str = type_
        self._address = address

        self._expression = 'x'
        self._expression_compiled = compile('x', 'expr', 'eval')
        self._color = color
        self._color_str = '#{0:02x}{1:02x}{2:02x}'.format(*color)

        # Initialize marker points (e.g., for cursors).
        self._mark_points = []
        for _ in range(2):
            point_item = pg.PlotDataItem(
                symbolSize=5,
                symbolBrush=pg.mkBrush(*color, 255),
                pxMode=True,
                skipFiniteCheck=True,
                clipToView=True,
                autoDownsample=True,
                downsampleMethod='peak',
                useCache=True,
                )
            label_item = pg.TextItem(
                '',
                color=(*color, 255),
                fill=(255, 255, 255, 150),
                )

            # Set initial visibility based on configuration.
            point_item.show() if enable_marks else point_item.hide()
            label_item.show() if enable_marks else label_item.hide()

            self._mark_points.append({
                'point': point_item,
                'label': label_item,
                })

        self._drag_limits = drag_limits
        self._imported = imported
        self._mutex = threading.Lock()
        self._needs_update = False

    @property
    def type_(self) -> int:
        return self._type

    @property
    def type_str(self) -> str:
        return self._type_str

    @type_.setter
    def type_(self, new_type: str) -> None:
        self._type = VAR_TYPE_CODE.get(new_type, VAR_TYPE_CODE['uint32_t'])
        self._type_str = new_type

    @property
    def address(self) -> int:
        return self._address

    @address.setter
    def address(self, new_address: int) -> None:
        self._address = new_address

    @property
    def expression(self) -> str:
        return self._expression

    @property
    def expression_compiled(self) -> CodeType:
        return self._expression_compiled

    @expression.setter
    def expression(self, new_expression: str) -> None:
        """
        Save and pre-compile the mathematical expression.
        WARNING: Using eval() on user-provided strings can be a security risk
        if the input is not strictly validated. Ensure inputs are sanitized.
        """

        self._expression = new_expression.replace('^', '**')
        self._expression_compiled = compile(self._expression, 'expr', 'eval')

    @property
    def data(self) -> tuple[Optional[np.ndarray], Optional[np.ndarray]]:
        return self.xData, self.yData

    @property
    def x_data(self) -> Optional[np.ndarray]:
        return self.xData

    @property
    def y_data(self) -> Optional[np.ndarray]:
        return self.yData

    @property
    def mark_point_0(self) -> dict:
        return self._mark_points[0]

    @property
    def mark_point_1(self) -> dict:
        return self._mark_points[1]

    @property
    def y_axis(self) -> str:
        return self._y_axis

    @y_axis.setter
    def y_axis(self, new_y_axis: str) -> None:
        self._y_axis = new_y_axis

    @property
    def drag_limits(self) -> Optional[list | tuple]:
        return self._drag_limits

    @property
    def color(self) -> tuple[int, int, int]:
        return self._color

    @property
    def color_str(self) -> str:
        return self._color_str

    def get_round_value(
            self,
            x: float,
            x_scale: str,
            ) -> tuple[Optional[float | int], ...]:
        """
        Get the nearest x- and y-data point
        based on the rounded x coordinate.
        """

        if x_scale == 'log':
            x = 10**x

        if (self.x_data is not None
                and self.y_data is not None
                and self.x_data.size > 0):
            index = int(np.abs(self.x_data - x).argmin())

            return float(self.x_data[index]), self.y_data[index]

        return None, None

    def get_floor_value(
            self,
            x: float,
            x_scale: str,
            ) -> tuple[Optional[float | int], ...]:
        """ Get the nearest x- and y-data point where x_data <= x (Floor). """

        if x_scale == 'log':
            x = 10**x

        if (self.x_data is not None
                and self.y_data is not None
                and self.x_data.size > 0):
            index = np.searchsorted(self.x_data, x, side='right') - 1

            # Clamp to valid array bounds
            if index < 0:
                index = 0
            elif index >= len(self.x_data):
                index = len(self.x_data) - 1

            return float(self.x_data[index]), self.y_data[index]

        return None, None

    def get_ceil_value(
            self,
            x: float,
            x_scale: str,
            ) -> tuple[Optional[float | int], ...]:
        """ Get the nearest x- and y-data point where x_data >= x (Ceil). """

        if x_scale == 'log':
            x = 10**x

        if (self.x_data is not None
                and self.y_data is not None
                and self.x_data.size > 0):
            index = np.searchsorted(self.x_data, x, side='left')

            # Clamp to valid array bounds.
            if index >= len(self.x_data):
                index = len(self.x_data) - 1
            elif index < 0:
                index = 0

            return float(self.x_data[index]), self.y_data[index]

        return None, None

    def move_mark_point(
            self,
            n: int,
            x: float,
            y: float,
            x_scale: str,
            update_point: bool
            ) -> None:
        """ Move marker to the new position and update its text label. """

        # Move marker and update text.
        self._mark_points[n]['label'].setPos(
            x if x_scale == 'linear' else np.log10(x),
            y if update_point else self._mark_points[n]['label'].pos().y(),
            )

        if update_point:
            if x_scale == 'linear':
                self._mark_points[n]['point'].setData(
                    [x], [y],
                    pxMode=True,
                    )
            else:
                self._mark_points[n]['point'].hide()

            self._mark_points[n]['label'].setText(f'{y:.6g}')

    @data.setter
    def data(self, new_data: tuple[np.ndarray, np.ndarray]) -> bool:
        """ Thread-safe data update mechanism. """

        if new_data[0].size == new_data[1].size:
            with nonblocking(self._mutex) as locked:
                if locked:
                    self._data_buf = new_data
                    self._needs_update = True
                    return True

        return False

    def update_line(self) -> None:
        if not self._needs_update:
            return

        x, y = self._data_buf

        x_opt = np.ascontiguousarray(x, dtype=np.float32)
        y_opt = np.ascontiguousarray(y, dtype=np.float32)

        self.setData(x_opt, y_opt, pxMode=True)
        self._needs_update = False

    def set_data_shared(self, new_data: tuple[np.ndarray, np.ndarray]) -> None:
        """ Public wrapper for setting data. """

        self.data = new_data
