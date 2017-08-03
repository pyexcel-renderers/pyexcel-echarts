import tempfile

from pyexcel._compact import PY2
from pyexcel.renderer import Renderer
from pyexcel_echarts.options import MANAGER


class Chart(Renderer):
    def render_sheet(self, sheet, chart_type='bar',
                     embed=False, **keywords):
        charter = MANAGER.get_a_plugin(chart_type)
        chart_instance = charter.render_sheet(
            sheet, **keywords)

        self._write_content(chart_instance)

        with tempfile.NamedTemporaryFile(suffix=".html") as fout:
            chart_instance.render(path=fout.name)
            fout.seek(0)
            self._stream.write(fout.read())

    def render_book(self, book, chart_type='bar', embed=False, **keywords):
        charter = MANAGER.get_a_plugin(chart_type)
        chart_instance = charter.render_book(book,
                                             **keywords)
        self._write_content(chart_instance)

    def _write_content(self, instance):
        with tempfile.NamedTemporaryFile(suffix=".html") as fout:
            instance.render(path=fout.name)
            fout.seek(0)
            if PY2:
                self._stream.write(fout.read())
            else:
                self._stream.write(fout.read().decode('utf-8'))
