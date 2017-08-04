# -*- coding: utf-8 -*-
# This file is part of pygal_sphinx_directives
#
# Pygal sphinx integration
# Copyright © 2012-2016 Florian Mounier
#
# Pyexcel sphinx integration
# Copyright © 2017 Onni Software Ltd.
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.


from docutils.parsers.rst import Directive
from traceback import format_exc, print_exc
from sphinx.directives.code import CodeBlock
from sphinx.util.i18n import search_image_for_language

import docutils.core
import pyexcel
import sys
import os

PY2 = sys.version_info[0] == 2


if PY2:
    from StringIO import StringIO
else:
    from io import StringIO


class PyechartsDirective(Directive):
    """Execute the given python file and puts its result in the document."""
    required_arguments = 0
    final_argument_whitespace = True
    has_content = True

    def run(self):
        env = self.state.document.settings.env
        fn = search_image_for_language('pie.csv', env)
        relfn, excel_file = env.relfn2path(fn)
        working_path = os.path.dirname(excel_file)
        content = ["import os", "os.chdir('%s')" % working_path]
        content += list(self.content)
        code = '\n'.join(content)
        scope = {'pyexcel': pyexcel}
        try:
            exec(code, scope)
        except Exception:
            print(code)
            print_exc()
            return [docutils.nodes.system_message(
                'An exception as occured during code parsing:'
                ' \n %s' % format_exc(), type='ERROR', source='/',
                level=3)]
        chart = None
        for key, value in scope.items():
            if isinstance(value, StringIO):
                chart = value
                break
        if chart is None:
            return [docutils.nodes.system_message(
                'No instance of graph found', level=3,
                type='ERROR', source='/')]

        try:
            svg = "%s" % chart.getvalue().decode('utf-8')
        except Exception:
            return [docutils.nodes.system_message(
                'An exception as occured during graph generation:'
                ' \n %s' % format_exc(), type='ERROR', source='/',
                level=3)]
        return [docutils.nodes.raw('', svg, format='html')]


class PyechartsWithCode(PyechartsDirective):

    def run(self):
        node_list = CodeBlock(
            self.name,
            ['python'],
            self.options,
            self.content,
            self.lineno,
            self.content_offset,
            self.block_text,
            self.state,
            self.state_machine).run()
        node_list.extend(super(PyechartsWithCode, self).run())

        return [docutils.nodes.compound('', *node_list)]


def setup(app):
    app.add_directive('pyexcel-chart', PyechartsDirective)
    app.add_directive('pyexcel-code', PyechartsWithCode)

    return {'version': '1.0.1'}
