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
         title=title, width=800, height=600, embed=True, legend_top='bottom')


Radar chart
********************************************************************************

.. pyexcel-table:: data/radar.csv
   :width: 500

Here is the source code using pyexcel

.. pyexcel-code::

    title = 'Browser usage in February 2012 (in %)'
    sheet = pyexcel.get_sheet(file_name='data/radar.csv')
    chart = sheet.plot(chart_type='radar', file_type='echarts.html',
         title=title, width=800, height=600, embed=True, legend_top='bottom')

Bar chart
********************************************************************************

.. pyexcel-table:: data/bar.csv
   :width: 800

Here is the source code using pyexcel

.. pyexcel-code::

    title = 'Water precipitation vs evaporation in a year'
    sheet = pyexcel.get_sheet(file_name='data/bar.csv')
    chart = sheet.plot(chart_type='bar', file_type='echarts.html',
         title=title, width=800, height=600, embed=True, legend_top='bottom')


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
         title=title, width=800, height=600, embed=True, legend_top='bottom')




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
         title=title, width=800, height=600, embed=True, legend_top='bottom')
