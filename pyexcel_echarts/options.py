import sys
import pyecharts
from pyexcel._compact import StringIO

from lml.plugin import PluginInfo, PluginManager

PY2 = sys.version_info[0] == 2

DEFAULT_TITLE = 'pyexcel via pyechars'

CHART_TYPES = dict(
    pie='Pie',
    box='Box',
    line='Line',
    bar='Bar',
    stacked_bar='StackedBar',
    radar='Radar',
    dot='Dot',
    funnel='Funnel',
    xy='XY',
    histogram='Histogram',
    scatter3d='Scatter3D'
)


class Chart(object):

    def __init__(self, cls_name):
        self._chart_class = CHART_TYPES.get(cls_name, 'line')
        self._tmp_io = StringIO()


@PluginInfo('chart', tags=['box'])
class SimpleLayout(Chart):

    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     label_y_in_row=0,
                     **keywords):
        params = {}
        self.params = {}
        if len(sheet.colnames) == 0:
            sheet.name_columns_by_row(label_y_in_row)
        params.update(keywords)
        the_dict = sheet.to_dict()
        cls = getattr(pyecharts, self._chart_class)
        instance = cls(title=title, **params)
        for key in the_dict:
            data_array = [value for value in the_dict[key] if value != '']
            instance.add(key, data_array)

        return instance


@PluginInfo('chart', tags=['pie'])
class PieLayout(Chart):

    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     label_y_in_row=0,
                     value_x_in_row=1,
                     **keywords):
        params = {}
        self.params = {}
        params.update(keywords)
        cls = getattr(pyecharts, self._chart_class)
        instance = cls(title=title, **params)
        instance.add("", sheet.row[0], sheet.row[1])
        return instance


@PluginInfo('chart', tags=['scatter3d'])
class Scatter3DLayout(Chart):

    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     **keywords):
        params = {}
        self.params = {}
        params.update(keywords)
        cls = getattr(pyecharts, self._chart_class)
        instance = cls(title=title, **params)
        instance.add("", sheet.array)
        return instance


@PluginInfo('chart',
            tags=['line', 'bar', 'stacked_bar',
                  'radar', 'dot', 'funnel'])
class ComplexLayout(Chart):

    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     label_x_in_column=0, label_y_in_row=0,
                     **keywords):
        params = {}
        self.params = {}
        if len(sheet.colnames) == 0:
            sheet.name_columns_by_row(label_y_in_row)
        if len(sheet.rownames) == 0:
            sheet.name_rows_by_column(label_x_in_column)
        schema = []
        for name in sheet.rownames:
            schema.append((name, max(sheet.row[name])))
        the_dict = sheet.to_dict()
        cls = getattr(pyecharts, self._chart_class)
        instance = cls(title=title, **params)
        instance.config(schema)
        for key in the_dict:
            data_array = [value for value in the_dict[key] if value != '']
            instance.add(key, [data_array])
        return instance


@PluginInfo('chart', tags=['histogram'])
class Histogram(Chart):
    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     height_in_column=0, start_in_column=1,
                     stop_in_column=2,
                     **keywords):
        cls = getattr(pyecharts, self._chart_class)
        instance = cls(title=title, **keywords)
        self._render_a_sheet(instance, sheet,
                             height_in_column=height_in_column,
                             start_in_column=start_in_column,
                             stop_in_column=stop_in_column)
        return instance

    def render_book(self, book, title=DEFAULT_TITLE,
                    height_in_column=0, start_in_column=1,
                    stop_in_column=2,
                    **keywords):
        from pyexcel.book import to_book
        cls = getattr(pyecharts, self._chart_class)
        instance = cls(title=title, **keywords)
        for sheet in to_book(book):
            self._render_a_sheet(instance, sheet,
                                 height_in_column=height_in_column,
                                 start_in_column=start_in_column,
                                 stop_in_column=stop_in_column)
        return instance

    def _render_a_sheet(self, instance, sheet,
                        height_in_column=0, start_in_column=1,
                        stop_in_column=2):
        histograms = zip(sheet.column[height_in_column],
                         sheet.column[start_in_column],
                         sheet.column[stop_in_column])
        if PY2 is False:
            histograms = list(histograms)
        instance.add(sheet.name, histograms)


@PluginInfo('chart', tags=['xy'])
class XY(Chart):

    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     x_in_column=0,
                     y_in_column=1,
                     **keywords):
        cls = getattr(pyecharts, self._chart_class)
        instance = cls(title=title, **keywords)
        self._render_a_sheet(instance, sheet,
                             x_in_column=x_in_column,
                             y_in_column=y_in_column)
        points = zip(sheet.column[x_in_column],
                     sheet.column[y_in_column])
        instance.add(sheet.name, points)
        instance.render(path=self._tmp_io)
        return self._tmp_io.getvalue()

    def render_book(self, book, title=DEFAULT_TITLE,
                    x_in_column=0,
                    y_in_column=1,
                    **keywords):
        from pyexcel.book import to_book
        cls = getattr(pyecharts, self._chart_class)
        instance = cls(title=title, **keywords)
        for sheet in to_book(book):
            self._render_a_sheet(instance, sheet,
                                 x_in_column=x_in_column,
                                 y_in_column=y_in_column)
        instance.render(path=self._tmp_io)
        return self._tmp_io.getvalue()

    def _render_a_sheet(self, instance, sheet,
                        x_in_column=0,
                        y_in_column=1):

        points = zip(sheet.column[x_in_column],
                     sheet.column[y_in_column])
        if not PY2:
            points = list(points)
        instance.add(sheet.name, points)


class ChartManager(PluginManager):
    def __init__(self):
        PluginManager.__init__(self, 'chart')

    def get_a_plugin(self, key, **keywords):
        self._logger.debug("get a plugin called")
        plugin = self.load_me_now(key)
        return plugin(key)

    def raise_exception(self, key):
        raise Exception("No support for " + key)


MANAGER = ChartManager()
