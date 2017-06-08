import os
import uuid

from pyexcel.renderer import Renderer
from jinja2 import Environment, FileSystemLoader

from pyexcel_echarts.options import MANAGER

JS_URL = 'https://cdnjs.cloudflare.com/ajax/libs/echarts/3.6.1/echarts.min.js'  # flake8: noqa


class Chart(Renderer):
    def __init__(self, file_type):
        Renderer.__init__(self, file_type)
        loader = FileSystemLoader(_get_resource_dir('templates'))
        self._env = Environment(loader=loader,
                                keep_trailing_newline=True,
                                trim_blocks=True,
                                lstrip_blocks=True)

    def render_sheet(self, sheet, chart_type='bar',
                     js_url=JS_URL, width=600, height=400,
                     embed=False, **keywords):
        config = MANAGER.get_a_plugin(chart_type)
        config.configure(sheet, **keywords)
        chart_data = {
            "uid": uuid.uuid4().hex,
            "option": config.to_json(),
            "js_url": JS_URL,
            "width": width,
            "height": height
        }
        if embed:
            template = self._env.get_template('embed.html')
        else:
            template = self._env.get_template('full.html')
        self._stream.write(template.render(**chart_data))


def _get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path
