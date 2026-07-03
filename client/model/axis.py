
import threading
from typing import Optional

import numpy as np
import pyqtgraph as pg

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor

from model.line import Line
from controller.common import nonblocking


# Color palette from GeoDataViz:
# https://github.com/OrdnanceSurvey/GeoDataViz-Toolkit/tree/master/Colours
LINE_COLORS = (
    (0, 154, 222),
    (255, 31, 91),
    (0, 205, 108),
    (175, 88, 186),
    (255, 198, 30),
    (242, 133, 34),
    (160, 177, 186),
    (166, 118, 29),
    (31, 119, 180),
    (255, 127, 14),
    (44, 160, 44),
    (214, 39, 40),
    (148, 103, 189),
    (140, 86, 75),
    (227, 119, 194),
    (127, 127, 127),
    (188, 189, 34),
    (23, 190, 207),
    )


class LogLinearInfiniteLabel(pg.InfLineLabel):
    """
    Custom label for InfiniteLine that supports both linear
    and logarithmic scales.
    """

    __slots__ = (
        '_x_scale',
        '_real_value',
        )

    def __init__(
            self,
            x_scale: str = 'linear',
            real_value: float | int = 0,
            *args, **kwargs,
            ) -> None:

        self._x_scale = x_scale
        self._real_value = real_value

        super().__init__(*args, **kwargs)

    def valueChanged(self) -> None:
        if not self.isVisible():
            return

        display_value = self._real_value if self._x_scale == 'linear' else 10**self._real_value
        self.setText(self.format.format(value=display_value))

        self.updatePosition()

    @property
    def real_value(self) -> float | int:
        return self._real_value

    @real_value.setter
    def real_value(self, new_value: float | int) -> None:
        self._real_value = new_value


class Axis(pg.PlotItem):
    """
    Custom plot axis class managing lines, cursors,
    and interactive measurements.
    """

    __slots__ = (
        '_x_label',
        '_y_label',
        '_x_unit',
        '_y_unit',
        '_y2_label',
        '_lines',
        '_imported_lines',
        '_selected_point',
        '_selectable_points',
        'cursors',
        '_cursors_mutex',
        'fill',
        'right_click',
        '_color_set',
        'measure_text',
        'dump_texts',
        'dump_line',
        '_x_scale',
        '_drag_point',
        )

    def __init__(
            self,
            x_scale: str = 'linear',
            disable_autorange: bool = False,
            selectable_points: bool = False,
            x_unit: str = '',
            y_unit: str = '',
            enable_y2: bool = False,
            enable_cursors: bool = True,
            *args, **kwargs,
            ) -> None:
        super().__init__(*args, **kwargs)

        self._setup_basic_ui(x_scale, disable_autorange, enable_y2)
        self._init_state_variables(x_unit, y_unit, selectable_points)

        if enable_cursors:
            self._setup_measure_and_dump_items()
            self._setup_cursors(x_scale)
        else:
            self.cursors = ()

        self.sigXRangeChanged.connect(self.__on_x_range_changed)

    def _setup_basic_ui(
            self,
            x_scale: str,
            disable_autorange: bool,
            enable_y2: bool
            ) -> None:
        """ Configure grid, legend, and basic view box settings. """

        self.showGrid(x=True, y=True, alpha=0.3)

        self.addLegend(
            brush=(255, 255, 255, 150),
            offset=0,
            verSpacing=-5,
            horSpacing=20,
            labelTextColor=(0, 0, 0, 255),
            labelTextSize='10pt',
            colCount=1,
            )

        self.legend.anchor(itemPos=(1, 0), parentPos=(1, 0), offset=(5, -5))

        for item in self.legend.items:
            item[0].setCacheMode(item[0].ItemCoordinateCache)

        self.setMenuEnabled(False)

        view_box = self.getViewBox()
        if view_box is not None:
            if disable_autorange:
                self.hideButtons()
                view_box.disableAutoRange('xy')
            view_box.setBackgroundColor('w')
            view_box.setBorder(color='#868482', width=1)
            view_box.setDefaultPadding(0.0)

        self.setLogMode(x=True if x_scale == 'log' else None)
        self._x_scale = x_scale

        self.showAxis('right', show=enable_y2)

        # Set axis labels color.
        for pos in ('left', 'bottom', 'top', 'right'):
            self.getAxis(pos).setTextPen('k')

        self.getAxis('bottom').setTickDensity(0.5)

    def _init_state_variables(
            self,
            x_unit: str,
            y_unit: str,
            selectable_points: bool
            ) -> None:
        """ Initialize internal state and tracking variables. """

        self._x_unit = x_unit
        self._y_unit = y_unit
        self._x_label = 'x'
        self._y_label = 'y'
        self._y2_label = 'y2'
        self._selected_point = 0
        self._selectable_points = selectable_points
        self._color_set = set()
        self._lines = []
        self._imported_lines = []
        self.right_click = False
        self._reset_drag_point()

    def _reset_drag_point(self) -> None:
        """ Reset the drag-and-drop tracking dictionary. """

        self._drag_point = {
            'point': None,
            'line': 0,
            'index': 0,
            'start': pg.Point(0, 0),
            'finish': pg.Point(0, 0),
            'offset': pg.Point(0, 0),
            }

    def _setup_cursors(self, x_scale: str) -> None:
        """ Initialize and configure the measurement cursors. """

        self._cursors_mutex = threading.Lock()

        bounds = [0.1, 0.9] if x_scale == 'linear' else [
            np.log10(2), np.log10(1000)
            ]
        pos_0 = 0.1 if x_scale == 'linear' else np.log10(2)
        pos_1 = 0.9 if x_scale == 'linear' else np.log10(8)
        real_val_0 = 0.1 if x_scale == 'linear' else 2
        real_val_1 = 0.9 if x_scale == 'linear' else 8

        pen_main = pg.mkPen(color='k', width=1)
        pen_hover_main = pg.mkPen(color='k', width=2)
        pen_aux = pg.mkPen(color='k', width=1, dash=[10, 10])
        pen_hover_aux = pg.mkPen(color='k', width=2, dash=[5, 5])

        self.cursors = (
            pg.InfiniteLine(
                pos=pos_0, angle=90, movable=True, bounds=bounds,
                pen=pen_main, hoverPen=pen_hover_main
                ),
            pg.InfiniteLine(
                pos=pos_1, angle=90, movable=True, bounds=bounds,
                pen=pen_aux, hoverPen=pen_hover_aux
                ),
            )

        self.cursors[0].label = LogLinearInfiniteLabel(
            line=self.cursors[0], text='x0={value:.6g}', movable=True,
            position=0.04, color='k', fill=(255, 255, 255, 150),
            x_scale=x_scale, real_value=real_val_0,
            )
        self.cursors[1].label = LogLinearInfiniteLabel(
            line=self.cursors[1], text='x1={value:.6g}', movable=True,
            position=0.04, color='k', fill=(255, 255, 255, 150),
            x_scale=x_scale, real_value=real_val_1,
            )

        # Add cursors in reverse order to manage Z-index properly.
        for c in reversed(self.cursors):
            c.setCursor(QCursor(Qt.SizeHorCursor))
            self.addItem(c, ignoreBounds=True)

        self.fill = pg.LinearRegionItem(
            values=[0.2, 0.8], orientation='vertical', swapMode='sort',
            movable=False, pen=(0, 0, 0, 0), brush=(235, 235, 250, 255),
            )

        self.fill.setZValue(-10)

        self.addItem(self.fill, ignoreBounds=True)

        self.fill.setCacheMode(
            self.fill.CacheMode.DeviceCoordinateCache
            )

        self.cursors[0].sigDragged.connect(lambda: self.__on_cursor_dragged(0))
        self.cursors[1].sigDragged.connect(lambda: self.__on_cursor_dragged(1))

        # Trigger initial position update.
        self.cursors[0].sigDragged.emit(self.cursors[0])
        self.cursors[1].sigDragged.emit(self.cursors[1])

    def _setup_measure_and_dump_items(self) -> None:
        """ Initialize text boxes for measurements and dump markers. """

        self.measure_text = pg.TextItem(
            'dx=x1-x0: 1.000000 s\n|1/dx|: 1.000000 Hz',
            color='k', anchor=(0, 0), fill=(255, 255, 255, 150),
            )
        self.measure_text.setFlag(self.measure_text.GraphicsItemFlag.ItemIgnoresTransformations)
        self.addItem(self.measure_text, ignoreBounds=True)
        self.measure_text.setParentItem(self.getViewBox())
        self.measure_text.setCacheMode(
            self.measure_text.CacheMode.DeviceCoordinateCache
            )

        self.dump_texts = []
        self.dump_line = pg.PlotDataItem(
            symbol='s', symbolSize=7, symbolPen='k', symbolBrush='w',
            pen={'color': 'k', 'width': 3}, pxMode=True, skipFiniteCheck=True,
            clipToView=True, autoDownsample=True, downsampleMethod='peak', useCache=True,
            )
        self.addItem(self.dump_line)
        self.dump_line.show()

    def mouseDragEvent(self, event) -> None:
        """ Handle drag-and-drop events for selectable points on lines. """

        if event.button() != Qt.LeftButton or not self._selectable_points:
            event.ignore()
            return

        view_box = self.getViewBox()
        if view_box is None:
            event.ignore()
            return

        if event.isStart():
            local_pos = view_box.mapSceneToView(event.buttonDownScenePos())
            for i, line in enumerate(self._lines):
                point = line.scatter.pointsAt(local_pos)

                if point.size > 0:
                    self._drag_point['point'] = point[0]
                    self._drag_point['line'] = i
                    self._drag_point['index'] = point[0].index()
                    self._drag_point['start'] = point[0].pos()
                    self._drag_point['finish'] = self._drag_point['start']
                    self._drag_point['offset'] = pg.Point(0, 0)
                    break
            else:
                self._reset_drag_point()
        elif event.isFinish():
            self._reset_drag_point()
        else:
            event.ignore()
            return

        if self._drag_point['point'] is not None:
            self._drag_point['finish'] = view_box.mapSceneToView(event.pos())
            self._drag_point['offset'] = self._drag_point['finish'] - self._drag_point['start']

            line = self._lines[self._drag_point['line']]
            y_data = line.y_data
            y_new = self._drag_point['finish'].y()

            if line.drag_limits:
                y_new = max(line.drag_limits[0], min(y_new, line.drag_limits[1]))

            y_data[self._drag_point['index']] = y_new
            line.data = line.x_data, y_data
            line.dragged.emit(self._drag_point['index'])

            event.accept()
        else:
            event.ignore()

    def __on_cursor_dragged(self, n: int) -> None:
        self.update_cursor_data(n, update_label=True)

        self.cursors[n].label.real_value = self.cursors[n].value()
        self.cursors[n].label.valueChanged()

    def update_cursor_data(
            self,
            n: int,
            method: str = 'round',
            update_label: bool = False
            ) -> None:
        """ Update cursor snap positions based on the selected interpolation method. """

        with nonblocking(self._cursors_mutex) as locked:
            if not locked:
                return

            mouse_point_x = self.cursors[n].getXPos()

            for line in self._lines:
                if method == 'round':
                    near_x, near_y = line.get_round_value(
                        mouse_point_x,
                        self.x_scale,
                        )
                elif method == 'floor':
                    near_x, near_y = line.get_floor_value(
                        mouse_point_x,
                        self.x_scale,
                        )
                elif method == 'ceil':
                    near_x, near_y = line.get_ceil_value(
                        mouse_point_x,
                        self.x_scale,
                        )
                else:
                    return

                if near_x is not None:
                    line.move_mark_point(
                        n, near_x, near_y,
                        self.x_scale,
                        update_label
                        )
                    self.cursors[n].setValue(near_x if self.x_scale == 'linear' else np.log10(near_x))

            self.fill.setRegion((self.cursors[0].pos(), self.cursors[1].pos()))

            if update_label:
                self.__update_measure_text_label()

    def __update_measure_text_label(self) -> None:
        """
        Recalculate and update the HTML text box
        displaying cursor statistics.
        """

        x0 = self.cursors[0].value()
        x1 = self.cursors[1].value()

        if self._x_scale == 'log':
            x0 = 10**x0
            x1 = 10**x1

        delta_x = x1 - x0
        inv_delta_x = 1 / np.abs(delta_x) if delta_x != 0 else float('inf')

        inv_x_unit = {
            's': 'Hz',
            'Hz': 's',
            }.get(self._x_unit, self._x_unit)

        x0, x1 = min(x0, x1), max(x0, x1)

        extra_lines = []

        if self._x_unit == 's':
            for line in self._lines:
                if line.x_data is not None and line.y_data is not None:
                    y_data = line.y_data[(line.x_data >= x0) & (line.x_data <= x1)]

                    if len(y_data) > 0:
                        y_mean = np.mean(y_data)
                        y_max = np.max(y_data)
                        y_min = np.min(y_data)
                        y_rms = np.sqrt(np.mean(y_data**2))
                        cf = y_max / y_rms if y_rms != 0 else float('inf')

                        extra_lines.append(
                            f'<br><span style="color: {line.color_str};">'
                            f'min: {y_min:.6g} max: {y_max:.6g} av: {y_mean:.6g} '
                            f'rms: {y_rms:.6g} cf: {cf:.6g}</span>'
                            )

        html_content = (
            f'<span style="color: #000000;">dx=x1-x0: {delta_x:.6g} {self._x_unit}</span><br>'
            f'<span style="color: #000000;">|1/dx|: {inv_delta_x:.6g} {inv_x_unit}</span>'
            + ''.join(extra_lines)
            )
        self.measure_text.setHtml(html_content)

    def __on_x_range_changed(self, _) -> None:
        """ Adjust cursor interpolation methods when they move out of the visible view box. """

        x0 = self.cursors[0].label.real_value
        x1 = self.cursors[1].label.real_value

        method_0 = 'round'
        method_1 = 'round'

        view_range = self.getViewBox().viewRange()[0]

        # Change default round method for moving cursors
        # when they are out of view box.
        if x0 < view_range[0]:
            x0 = view_range[0]
            method_0 = 'floor'
        elif x0 > view_range[1]:
            x0 = view_range[1]
            method_0 = 'ceil'

        if x1 < view_range[0]:
            x1 = view_range[0]
            method_1 = 'floor'
        elif x1 > view_range[1]:
            x1 = view_range[1]
            method_1 = 'ceil'

        self.cursors[0].setValue(x0)
        self.cursors[1].setValue(x1)

        self.update_cursor_data(0, method=method_0)
        self.update_cursor_data(1, method=method_1)

    @property
    def x_scale(self) -> str:
        return self._x_scale

    @property
    def x_label(self) -> str:
        return self._x_label

    @x_label.setter
    def x_label(self, new_x_label: str) -> None:
        self._x_label = new_x_label
        self.setLabel('bottom', new_x_label, color='k')

    @property
    def y_label(self) -> str:
        return self._y_label

    @y_label.setter
    def y_label(self, new_y_label: str) -> None:
        self._y_label = new_y_label
        self.setLabel('left', new_y_label)

    @property
    def y2_label(self) -> str:
        return self._y2_label

    @y2_label.setter
    def y2_label(self, new_y_label: str) -> None:
        self._y2_label = new_y_label
        self.setLabel('right', new_y_label)

    @property
    def selected_point(self) -> int:
        return self._selected_point

    @selected_point.setter
    def selected_point(self, new_selected_point: int) -> None:
        self._selected_point = new_selected_point

    @property
    def lines(self) -> list[Line]:
        return self._lines

    @property
    def x_unit(self) -> str:
        return self._x_unit

    def add_line(
            self,
            name: str,
            type_: str,
            address: int,
            y_axis: str = 'y',
            show_symbols: bool = False,
            drag_limits: Optional[list | tuple] = None,
            imported: bool = False,
            enable_marks: bool = False,
            ) -> Line:
        """ Create and add a new interactive line to the plot. """

        # Select individual color for the line.
        select_color = (0, 0, 0)
        for color in LINE_COLORS:
            if color not in self._color_set:
                select_color = color
                self._color_set.add(color)
                break

        new_line = Line(
            name=name,
            type_=type_,
            address=address,
            y_axis=y_axis,
            color=select_color,
            show_symbols=show_symbols,
            drag_limits=drag_limits,
            imported=imported,
            enable_marks=enable_marks,
            )

        if not imported:
            self._lines.append(new_line)
        else:
            self._imported_lines.append(new_line)

        self.addItem(new_line)
        self.addItem(new_line.mark_point_0['point'])
        self.addItem(new_line.mark_point_0['label'], ignoreBounds=True)
        self.addItem(new_line.mark_point_1['point'])
        self.addItem(new_line.mark_point_1['label'], ignoreBounds=True)

        return new_line

    def _remove_line_from_plot(
            self,
            line: Line
            ) -> None:
        """
        Helper to safely remove a line,
        its markers, and free its color.
        """

        self.removeItem(line.mark_point_0['point'])
        self.removeItem(line.mark_point_0['label'])
        self.removeItem(line.mark_point_1['point'])
        self.removeItem(line.mark_point_1['label'])
        self.removeItem(line)

        if line in self._lines:
            self._lines.remove(line)

        # Use discard to prevent KeyError if the color was already removed.
        if line.color != (0, 0, 0):
            self._color_set.discard(line.color)

    def remove_all_lines(self) -> None:
        """ Remove all standard lines from the plot. """

        for line in reversed(self._lines):
            self._remove_line_from_plot(line)

    def remove_all_imported_lines(self) -> None:
        """ Remove all imported lines. """

        for line in reversed(self._imported_lines):
            self.removeItem(line.mark_point_0['point'])
            self.removeItem(line.mark_point_0['label'])
            self.removeItem(line.mark_point_1['point'])
            self.removeItem(line.mark_point_1['label'])
            self.removeItem(line)
            self._imported_lines.remove(line)

            if line.color != (0, 0, 0):
                self._color_set.remove(line.color)

    def remove_line(
            self,
            name: Optional[str] = None,
            address: Optional[int] = None,
            ) -> None:
        """ Remove a specific line by name or address. """

        for line in self._lines:
            if (name and line.name() == name) or (address and line.address == address):
                self._remove_line_from_plot(line)
                break

    def update_lines(self) -> None:
        for line in self._lines:
            line.update_line()
