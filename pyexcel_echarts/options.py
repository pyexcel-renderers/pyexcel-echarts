import json
from collections import defaultdict

from datetime import date, datetime
from lml.plugin import PluginInfo, PluginManager


DEFAULTS = dict(
    title={},
    tooltip={},
    legend=defaultdict(list),
    series=[]
)


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            date_string = obj.strftime('%Y/%m/%d')
            return date_string
        if isinstance(obj, datetime):
            datetime_string = obj.strftime("%Y/%m/%d %H:%M:%S")
            return datetime_string
        return json.JSONEncoder.default(self, obj)


def _dumps(data):
    return json.dumps(data, cls=DateTimeEncoder)


class EChartsOption(object):
    def __init__(self):
        self._config = {}
        self._config.update(DEFAULTS)

    def set_title(self, title):
        self._config['title']['text'] = title

    def add_chart(self, name, chart_type, data):
        self._config['legend']['data'].append(name)
        self._config['series'].append(
            dict(
                name=name,
                type=chart_type,
                data=data
            ))

    def configure(self, instance, **keywords):
        raise NotImplementedError("")

    def to_json(self):
        return _dumps(self._config)


@PluginInfo(
    'echarts',
    tags=['bar']
    )
class BarOption(EChartsOption):

    def __init__(self):
        super(BarOption, self).__init__()
        self._config['xAxis'] = {}
        self._config['yAxis'] = {}

    def configure(self, sheet,
                  label_x_in_column=0, label_y_in_row=0, **keywords):
        sheet.name_columns_by_row(label_y_in_row)
        sheet.name_rows_by_column(label_x_in_column)
        self.set_title(sheet.name)
        self.set_axis_x(sheet.colnames)
        for rowname in sheet.rownames:
            self.add_chart(rowname, 'bar', sheet.row[rowname])

    def set_axis_x(self, data):
        self._config['xAxis']['data'] = data

    def set_axis_y(self, data):
        self._config['yAxis']['data'] = data


@PluginInfo(
    'echarts',
    tags=['timeseries']
)
class TimeSeriesOption(EChartsOption):
    def __init__(self):
        super(TimeSeriesOption, self).__init__()
        self._config['xAxis'] = []
        self._config['yAxis'] = []

    def configure(self, sheet,
                  timeseries_in_column=0, value_in_column=1, y_max=500,
                  **keywords):
        self.set_title(sheet.name)
        self._config['xAxis'].append(dict(
            type='category',
            boundayGap=False,
            axisLine=dict(onZero=True),
            data=sheet.column[timeseries_in_column],
            position='top'
        ))
        self._config['yAxis'].append(dict(
            name='NO2(xx)',
            type='value',
            max=y_max
        ))
        self._config['tooltip'] = dict(
            trigger='axis',
            axisPointer=dict(animation=False)
        )
        self._config['axisPointer'] = dict(link=dict(xAxisIndex='all'))
        self._config['legend'] = dict(
            data=['NO2']
        )
        self._config['series'].append(dict(
            name='NO2',
            type='line',
            symbolSize=8,
            hoverAnimation=False,
            data=sheet.column[value_in_column]
        ))


class EChartsOptionManager(PluginManager):
    def __init__(self):
        PluginManager.__init__(self, 'echarts')

    def get_a_plugin(self, key, **keywords):
        plugin = self.load_me_now(key)
        return plugin()

    def raise_exception(self, key):
        raise Exception("No support for diagram %s" % key)


MANAGER = EChartsOptionManager()
