
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
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9',
                   '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    s.save_as('scatter3d.echarts.html', chart_type='scatter3d',
              is_visualmap=True,
              visual_range_color=range_color)
