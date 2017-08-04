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
    svg = sheet.plot(chart_type='pie', file_type='echarts.html',
         title=title, width=600, height=400, embed=True, legend_top='bottom')
