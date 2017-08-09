import pyexcel as p
from common import get_fixtures

RANGE_COLOR = ['#313695', '#4575b4', '#74add1', '#abd9e9',
               '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']


def test_pie_chart():
    s = p.get_sheet(file_name=get_fixtures('pie.csv'))
    s.save_as('pie.echarts.html', chart_type='pie')


def test_kline_chart():
    s = p.get_sheet(file_name=get_fixtures('kline.csv'))
    s.save_as('kline.echarts.html', chart_type='kline', legend='daily k')


def test_radar_chart():
    s = p.get_sheet(file_name=get_fixtures('radar.csv'))
    s.save_as('radar.echarts.html', chart_type='radar')


def test_bar_chart():
    s = p.get_sheet(file_name=get_fixtures('bar.csv'))
    s.save_as('bar.echarts.html', chart_type='bar')


def test_scatter3d_chart():
    s = p.get_sheet(file_name=get_fixtures('scatter_3d.csv'))
    s.save_as('scatter3d.echarts.html', chart_type='scatter3d',
              is_visualmap=True,
              visual_range_color=RANGE_COLOR)


def test_bar3d_chart():
    s = p.get_sheet(file_name=get_fixtures('bar3d.csv'))
    s.save_as('bar3d.echarts.html', chart_type='bar3d',
              is_visualmap=True, visual_range_color=RANGE_COLOR,
              visual_range=[0, 20],
              grid3D_width=200, grid3D_depth=80)


def test_heatmap_chart():
    s = p.get_sheet(file_name=get_fixtures('bar3d.csv'))
    s.save_as('heatmap.echarts.html', chart_type='heatmap',
              is_visualmap=True, visual_range_color=RANGE_COLOR,
              visual_range=[0, 20],
              visual_text_color="#000", visual_orient='horizontal')


def test_effectscatter_chart():
    s = p.get_sheet(file_name=get_fixtures('effectscatter.csv'))
    s.save_as('effectscatter.echarts.html', chart_type='effectscatter')


def test_funnel_chart():
    s = p.get_sheet(file_name=get_fixtures('funnel.csv'))
    s.save_as('funnel.echarts.html', chart_type='funnel')


def test_line_chart():
    s = p.get_sheet(file_name=get_fixtures('line.csv'))
    s.save_as('line.echarts.html', chart_type='line')


def test_gauge_chart():
    s = p.get_sheet(file_name=get_fixtures('gauge.csv'))
    s.save_as('gauge.echarts.html', chart_type='gauge')
