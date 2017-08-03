
import pyexcel as p
from common import get_fixtures


def test_pie_chart():
    s = p.get_sheet(file_name=get_fixtures('pie.csv'))
    s.save_as('pie.echarts.html', chart_type='pie')


def test_radar_chart():
    s = p.get_sheet(file_name=get_fixtures('radar.csv'))
    s.save_as('radar.echarts.html', chart_type='radar')
