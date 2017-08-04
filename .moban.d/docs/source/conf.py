{% extends 'docs/source/conf.py.jj2'%}

{%block additional_imports%}
import os
import sys
sys.path.append(os.path.abspath('.'))
{%endblock%}

{%block SPHINX_EXTENSIONS%}
    'sphinx.ext.autosummary',
    'sphinxcontrib.excel',
    'sphinxcontrib.spelling',
    'pyexcel_sphinx_integration'
{%endblock%}

{%block custom_doc_theme%}
html_theme = 'default'


def setup(app):
    app.add_stylesheet('theme_overrides.css')


{%endblock%}

