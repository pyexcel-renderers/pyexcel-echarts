Plot echarts
================================================================================

Pie chart
********************************************************************************

.. pyexcel-table:: data/pie.csv
   :width: 400

Here is the source code using pyexcel

.. pyexcel-code::

    title = 'Browser usage in February 2012 (in %)'
    sheet = pyexcel.get_sheet(file_name='data/pie.csv')
    chart = sheet.plot(chart_type='pie', file_type='echarts.html',
         title=title, width=800, height=600, mode='embed', legend_top='bottom')


Funnel chart
********************************************************************************

.. pyexcel-table:: data/funnel.csv
   :width: 400

Here is the source code using pyexcel

.. pyexcel-code::

    title = 'Some sales figures'
    sheet = pyexcel.get_sheet(file_name='data/funnel.csv')
    chart = sheet.plot(chart_type='funnel', file_type='echarts.html',
         title=title, width=800, height=600, mode='embed', legend_top='bottom')


Line chart
********************************************************************************

.. pyexcel-table:: data/line.csv
   :width: 400

Here is the source code using pyexcel

.. pyexcel-code::

    title = 'Some sales figures'
    sheet = pyexcel.get_sheet(file_name='data/line.csv')
    chart = sheet.plot(chart_type='line', file_type='echarts.html',
         title=title, width=800, height=600, mode='embed', legend_top='bottom')


Gauge chart
********************************************************************************

.. pyexcel-table:: data/gauge.csv
   :width: 400

Here is the source code using pyexcel

.. pyexcel-code::

    title = 'Some sales figures'
    sheet = pyexcel.get_sheet(file_name='data/gauge.csv')
    chart = sheet.plot(chart_type='gauge', file_type='echarts.html',
         title=title, width=800, height=600, mode='embed', legend_top='bottom')


Effectscatter chart
********************************************************************************

.. pyexcel-table:: data/effectscatter.csv
   :width: 400

Here is the source code using pyexcel

.. pyexcel-code::

    title = 'Effect scatter'
    sheet = pyexcel.get_sheet(file_name='data/effectscatter.csv')
    chart = sheet.plot(chart_type='effectscatter', file_type='echarts.html',
         title=title, width=800, height=600, mode='embed', legend_top='bottom')


Kline chart
********************************************************************************

.. pyexcel-table:: data/kline.csv
   :width: 400
   :height: 350

Here is the source code using pyexcel

.. pyexcel-code::

    title = 'Daily K Line'
    sheet = pyexcel.get_sheet(file_name='data/kline.csv')
    chart = sheet.plot(chart_type='kline', file_type='echarts.html',
         title=title, legend='daily k',
		 width=800, height=400, mode='embed', legend_top='bottom')


Radar chart
********************************************************************************

.. pyexcel-table:: data/radar.csv
   :width: 500

Here is the source code using pyexcel

.. pyexcel-code::

    title = 'Browser usage in February 2012 (in %)'
    sheet = pyexcel.get_sheet(file_name='data/radar.csv')
    chart = sheet.plot(chart_type='radar', file_type='echarts.html',
         title=title, width=800, height=600, mode='embed', legend_top='bottom')

Bar chart
********************************************************************************

.. pyexcel-table:: data/bar.csv
   :width: 800

Here is the source code using pyexcel

.. pyexcel-code::

    title = 'Water precipitation vs evaporation in a year'
    sheet = pyexcel.get_sheet(file_name='data/bar.csv')
    chart = sheet.plot(chart_type='bar', file_type='echarts.html',
         title=title, width=800, height=600, mode='embed', legend_top='bottom')


Bar 3D chart
********************************************************************************
.. pyexcel-table:: data/bar3d.csv
   :width: 800
   :height: 300

Here is the source code using pyexcel

.. pyexcel-code::

    title = 'Example scattered points in 3D'
    sheet = pyexcel.get_sheet(file_name='data/bar3d.csv')
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9',
                   '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    chart = sheet.plot(chart_type='bar3d', file_type='echarts.html',
         visual_range_color=range_color, is_visualmap=True,
		 visual_range=[0, 20], grid3D_width=200, grid3D_depth=80,
         title=title, width=800, height=600, mode='embed', legend_top='bottom')


Heatmap
********************************************************************************

The same bar3d data is plotted as heatmap:

.. pyexcel-code::

    title = 'Example heatmap'
    sheet = pyexcel.get_sheet(file_name='data/bar3d.csv')
    chart = sheet.plot(chart_type='heatmap', file_type='echarts.html',
         is_visualmap=True, visual_range=[0, 20],
		 visual_text_color="#000", visual_orient='horizontal',
         title=title, width=800, height=600, mode='embed', legend_top='bottom')



Scatter 3D chart
********************************************************************************
.. pyexcel-table:: data/scatter_3d.csv
   :width: 250
   :height: 300

Here is the source code using pyexcel

.. pyexcel-code::

    title = 'Example scattered points in 3D'
    sheet = pyexcel.get_sheet(file_name='data/scatter_3d.csv')
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9',
                   '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    chart = sheet.plot(chart_type='scatter3d', file_type='echarts.html',
         visual_range_color=range_color, is_visualmap=True,
         title=title, width=800, height=600, mode='embed', legend_top='bottom')
