from pyexcel.renderer import Renderer
from pyexcel_echarts.options import MANAGER


DEFAULT_TITLE = 'pyexcel via pyechars'


class Chart(Renderer):
    def render_sheet(self, sheet, chart_type='bar', mode='embed',
                     title=DEFAULT_TITLE,
                     subtitle="",
                     width=800,
                     height=400,
                     title_pos="auto",
                     title_top="auto",
                     title_color="#000",
                     subtitle_color="#aaa",
                     title_text_size=18,
                     subtitle_text_size=12,
                     background_color="#fff",
                     **keywords):
        charter = MANAGER.get_a_plugin(
            chart_type,
            mode=mode,
            title=title, subtitle=subtitle,
            width=width, height=height,
            title_pos=title_pos, title_top=title_top,
            title_color=title_color, title_text_size=title_text_size,
            subtitle_color=subtitle_color,
            subtitle_text_size=subtitle_text_size,
            background_color=background_color)
        charter.render_sheet(
            sheet, **keywords)

        self._stream.write(str(charter))

    def render_book(self, book, chart_type='bar', mode='embed',
                    title=DEFAULT_TITLE,
                    subtitle="",
                    width=800,
                    height=400,
                    title_pos="auto",
                    title_top="auto",
                    title_color="#000",
                    subtitle_color="#aaa",
                    title_text_size=18,
                    subtitle_text_size=12,
                    background_color="#fff",
                    **keywords):
        charter = MANAGER.get_a_plugin(
            chart_type,
            mode=mode,
            title=title, subtitle=subtitle,
            width=width, height=height,
            title_pos=title_pos, title_top=title_top,
            title_color=title_color, title_text_size=title_text_size,
            subtitle_color=subtitle_color,
            subtitle_text_size=subtitle_text_size,
            background_color=background_color)
        charter.render_book(book,
                            **keywords)
        self._stream.write(str(charter))
