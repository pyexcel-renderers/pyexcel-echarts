import uuid

from pyexcel.renderer import Renderer

from pyexcel_echarts.options import MANAGER


SCRIPT = """
<script type="text/javascript">
var myChart = echarts.init(document.getElementById('%s'));
var option = %s;
myChart.setOption(option);
</script>
"""


class Chart(Renderer):

    def render_sheet(self, sheet, chart_type='bar',
                     embed=False, **keywords):
        config = MANAGER.get_a_plugin(chart_type)
        config.configure(sheet, **keywords)
        if not embed:
            self._render_html_header()
        div_id = uuid.uuid4().hex
        self._stream.write(
            '<div id="%s" style="width:600px;height:400px"></div>' % div_id)
        self._stream.write(SCRIPT % (div_id, config.to_json()))
        self._stream.write("</body></html>")

    def _render_html_header(self, js_url=None, **keywords):
        self._stream.write('<html><head>')
        self._stream.write('<script src="echarts.min.js"></script>')
        self._stream.write('</head><body>')
