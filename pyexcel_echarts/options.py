import tempfile

import pyecharts
from pyexcel._compact import StringIO

from lml.plugin import PluginInfo, PluginManager
from pyexcel._compact import PY2


DEFAULT_TITLE = 'pyexcel via pyechars'

CHART_TYPES = dict(
    box='Box',
    bar='Bar',
    bar3d='Bar3D',
    effectscatter='EffectScatter',
    funnel='Funnel',
    gauge='Gauge',
    heatmap='HeatMap',
    kline='Kline',
    line='Line',
    pie='Pie',
    radar='Radar',
    scatter3d='Scatter3D',
    xy='XY'
)


class Chart(object):

    def __init__(self, cls_name, mode='embed', title=DEFAULT_TITLE,
                 subtitle="", **keywords):
        self._chart_class = CHART_TYPES.get(cls_name, 'line')
        cls = getattr(pyecharts, self._chart_class)
        self.instance = cls(title, subtitle, **keywords)
        self._tmp_io = StringIO()
        self._mode = mode

    def __str__(self):
        if self._mode == 'embed':
            content = self.instance.render_embed()
        elif self._mode == 'notebook':
            content = self.instance._repr_html_()
        else:
            with tempfile.NamedTemporaryFile(suffix=".html") as fout:
                self.instance.render(path=fout.name)
                fout.seek(0)
                content = fout.read()
        if not PY2:
            content = content.decode('utf-8')
        return content


@PluginInfo('chart', tags=['box'])
class SimpleLayout(Chart):

    def render_sheet(self, sheet,
                     label_y_in_row=0,
                     **keywords):
        if len(sheet.colnames) == 0:
            sheet.name_columns_by_row(label_y_in_row)
        the_dict = sheet.to_dict()
        for key in the_dict:
            data_array = [value for value in the_dict[key] if value != '']
            self.instance.add(key, data_array, **keywords)


@PluginInfo('chart', tags=['pie', 'funnel'])
class PieLayout(Chart):

    def render_sheet(self, sheet,
                     label_y_in_row=0,
                     value_x_in_row=1,
                     **keywords):
        self.instance.add("", sheet.row[label_y_in_row],
                          sheet.row[value_x_in_row], **keywords)


@PluginInfo('chart', tags=['gauge'])
class Gauge(Chart):

    def render_sheet(self, sheet,
                     label_y_in_row=0,
                     value_x_in_row=1,
                     **keywords):
        for i in range(len(sheet.row[label_y_in_row])):
            self.instance.add("", sheet.row[label_y_in_row][i],
                              sheet.row[value_x_in_row][i], **keywords)


@PluginInfo('chart', tags=['effectscatter'])
class EffectScatter(Chart):

    def render_sheet(self, sheet,
                     value_x_in_row=0,
                     value_y_in_row=1,
                     **keywords):
        self.instance.add(sheet.name, sheet.row[value_x_in_row],
                          sheet.row[value_y_in_row], **keywords)


@PluginInfo('chart', tags=['kline'])
class KlineLayout(Chart):

    def render_sheet(self, sheet,
                     label_x_in_column=0, label_y_in_row=0, legend="",
                     **keywords):
        if len(sheet.colnames) == 0:
            sheet.name_columns_by_row(label_y_in_row)
        if len(sheet.rownames) == 0:
            sheet.name_rows_by_column(label_x_in_column)
        self.instance.add(legend, sheet.rownames,
                          list(sheet.rows()), **keywords)


@PluginInfo('chart', tags=['line'])
class LineLayout(Chart):

    def render_sheet(self, sheet,
                     label_x_in_column=0, label_y_in_row=0,
                     **keywords):
        if len(sheet.colnames) == 0:
            sheet.name_columns_by_row(label_y_in_row)
        if len(sheet.rownames) == 0:
            sheet.name_rows_by_column(label_x_in_column)

        for legend in sheet.rownames:
            self.instance.add(
                legend, sheet.colnames,
                sheet.row[legend], **keywords)


@PluginInfo('chart', tags=['scatter3d'])
class Scatter3DLayout(Chart):

    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     **keywords):
        self.instance.add("", sheet.array, **keywords)


@PluginInfo('chart',
            tags=['radar'])
class RadarChart(Chart):

    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     label_x_in_column=0, label_y_in_row=0,
                     **keywords):
        if len(sheet.colnames) == 0:
            sheet.name_columns_by_row(label_y_in_row)
        if len(sheet.rownames) == 0:
            sheet.name_rows_by_column(label_x_in_column)
        schema = []
        for name in sheet.rownames:
            schema.append((name, max(sheet.row[name])))
        the_dict = sheet.to_dict()
        self.instance.config(schema)
        for key in the_dict:
            data_array = [value for value in the_dict[key] if value != '']
            self.instance.add(key, [data_array], **keywords)


@PluginInfo('chart',
            tags=['bar'])
class BarChart(Chart):

    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     label_x_in_column=0, label_y_in_row=0,
                     **keywords):
        if len(sheet.colnames) == 0:
            sheet.name_columns_by_row(label_y_in_row)
        if len(sheet.rownames) == 0:
            sheet.name_rows_by_column(label_x_in_column)
        schema = []
        for name in sheet.rownames:
            schema.append((name, max(sheet.row[name])))
        for key in sheet.rownames:
            data_array = [value for value in sheet.row[key] if value != '']
            self.instance.add(key, sheet.colnames, data_array, **keywords)


@PluginInfo('chart',
            tags=['bar3d', 'heatmap'])
class Bar3DChart(Chart):

    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     label_x_in_column=0, label_y_in_row=0,
                     **keywords):
        if len(sheet.colnames) == 0:
            sheet.name_columns_by_row(label_y_in_row)
        if len(sheet.rownames) == 0:
            sheet.name_rows_by_column(label_x_in_column)
        data = []
        for x in range(len(sheet.rownames)):
            for y in range(len(sheet.colnames)):
                data.append([y, x, sheet[x, y]])

        self.instance.add("", sheet.colnames, sheet.rownames,
                          data, **keywords)


class ChartManager(PluginManager):
    def __init__(self):
        PluginManager.__init__(self, 'chart')

    def get_a_plugin(self, key, **keywords):
        self._logger.debug("get a plugin called")
        plugin = self.load_me_now(key)
        return plugin(key, **keywords)

    def raise_exception(self, key):
        raise Exception("No support for " + key)


MANAGER = ChartManager()
