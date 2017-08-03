
import pyexcel as p
from common import get_fixtures


def test_pie_chart():
    s = p.get_sheet(file_name=get_fixtures('pie.csv'))
    s.save_as('pie.echarts.html', chart_type='pie')


def test_radar_chart():
    s = p.get_sheet(file_name=get_fixtures('radar.csv'))
    s.save_as('radar.echarts.html', chart_type='radar')


def test_scatter3d_chart():
    s = p.get_sheet(file_name=get_fixtures('scatter_3d.csv'))
    s.save_as('scatter3d.echarts.html', chart_type='scatter3d')
