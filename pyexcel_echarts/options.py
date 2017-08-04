import tempfile

import pyecharts
from pyexcel._compact import StringIO

from lml.plugin import PluginInfo, PluginManager
from pyexcel._compact import PY2


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

    def __init__(self, cls_name, embed=False, title=DEFAULT_TITLE,
                 subtitle="", **keywords):
        chart_class = CHART_TYPES.get(cls_name, 'line')
        cls = getattr(pyecharts, chart_class)
        self.instance = cls(title, subtitle, **keywords)
        self._tmp_io = StringIO()
        self._embed = embed

    def __str__(self):
        if self._embed:
            content = self.instance.render_embed()
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


@PluginInfo('chart', tags=['pie'])
class PieLayout(Chart):

    def render_sheet(self, sheet,
                     label_y_in_row=0,
                     value_x_in_row=1,
                     **keywords):
        self.instance.add("", sheet.row[0], sheet.row[1], **keywords)


@PluginInfo('chart', tags=['scatter3d'])
class Scatter3DLayout(Chart):

    def render_sheet(self, sheet, title=DEFAULT_TITLE,
                     **keywords):
        self.instance.add("", sheet.array, **keywords)


@PluginInfo('chart',
            tags=['line', 'bar', 'stacked_bar',
                  'radar', 'dot', 'funnel'])
class ComplexLayout(Chart):

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
