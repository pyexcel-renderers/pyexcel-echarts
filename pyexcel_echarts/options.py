import json
from collections import defaultdict

from lml.plugin import PluginInfo, PluginManager


DEFAULTS = dict(
    title={},
    tooltip={},
    legend=defaultdict(list),
    xAxis={},
    yAxis={},
    series=[]
)


class EChartsOption(object):
    def __init__(self):
        self.__config = {}
        self.__config.update(DEFAULTS)

    def set_title(self, title):
        self.__config['title']['text'] = title

    def set_axis_x(self, data):
        self.__config['xAxis']['data'] = data

    def set_axis_y(self, data):
        self.__config['yAxis']['data'] = data

    def add_chart(self, name, chart_type, data):
        self.__config['legend']['data'].append(name)
        self.__config['series'].append(
            dict(
                name=name,
                type=chart_type,
                data=data
            ))

    def configure(self, instance, **keywords):
        raise NotImplementedError("")

    def to_json(self):
        return json.dumps(self.__config)


@PluginInfo(
    'echarts',
    tags=['bar']
    )
class BarOption(EChartsOption):

    def configure(self, sheet,
                  label_x_in_column=0, label_y_in_row=0, **keywords):
        sheet.name_columns_by_row(label_y_in_row)
        sheet.name_rows_by_column(label_x_in_column)
        self.set_title(sheet.name)
        self.set_axis_x(sheet.colnames)
        for rowname in sheet.rownames:
            self.add_chart(rowname, 'bar', sheet.row[rowname])


class EChartsOptionManager(PluginManager):
    def __init__(self):
        PluginManager.__init__(self, 'echarts')

    def get_a_plugin(self, key, **keywords):
        plugin = self.load_me_now(key)
        return plugin()

    def raise_exception(self, key):
        raise Exception("No support for diagram %s" % key)


MANAGER = EChartsOptionManager()
