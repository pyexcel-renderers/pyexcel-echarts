# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.abspath('.'))
DESCRIPTION = (
    'draw echarts using pyexcel data via pyecharts' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinxcontrib.excel',
    'sphinxcontrib.spelling',
    'pyexcel_sphinx_integration'
]

intersphinx_mapping = {
    'pyexcel': ('http://pyexcel.readthedocs.io/en/latest/', None),
}
spelling_word_list_filename = 'spelling_wordlist.txt'
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'pyexcel-echarts'
copyright = u'2015-2017 Onni Software Ltd.'
version = '0.0.1'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'


def setup(app):
    app.add_stylesheet('theme_overrides.css')


html_static_path = ['_static']
htmlhelp_basename = 'pyexcel-echartsdoc'
latex_elements = {}
latex_documents = [
    ('index', 'pyexcel-echarts.tex',
     'pyexcel-echarts Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'pyexcel-echarts',
     'pyexcel-echarts Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'pyexcel-echarts',
     'pyexcel-echarts Documentation',
     'Onni Software Ltd.', 'pyexcel-echarts',
     DESCRIPTION,
     'Miscellaneous'),
]
