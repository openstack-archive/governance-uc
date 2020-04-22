#!/usr/bin/env python

#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Build a table of the current teams"""

import yaml

from docutils import nodes
from docutils.parsers.rst.directives.tables import Table
from docutils.parsers.rst import directives
from sphinx.util import logging

LOG = logging.getLogger(__name__)


class TeamTable(Table):
    """Insert the members table using the referenced file as source.
    """
    HEADERS = ('Name', 'Chairs', 'Mission')

    option_spec = {'class': directives.class_option,
                   'name': directives.unchanged,
                   'datafile': directives.unchanged,
                   'headers': directives.unchanged,
                   }
    def run(self):
        env = self.state.document.settings.env

        if self.options.get('headers') is not None:
            self.HEADERS = self.options.get('headers').split(",")
        # The required argument to the directive is the name of the
        # file to parse.
        datafile = self.options.get('datafile')
        if not datafile:
            error = self.state_machine.reporter.error(
                'No filename in teamtable directive',
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno)
            return [error]

        # Handle the width settings and title
        try:
            # Since docutils 0.13, get_column_widths returns a (widths,
            # colwidths) tuple, where widths is a string (i.e. 'auto').
            # See https://sourceforge.net/p/docutils/patches/120/.
            col_widths = self.get_column_widths(len(self.HEADERS))
            title, messages = self.make_title()
        except SystemMessagePropagation as detail:
            return [detail.args[0]]
        except Exception as err:
            error = self.state_machine.reporter.error(
                'Error processing memberstable directive:\n%s' % err,
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno,
                )
            return [error]

        # Now find the real path to the file, relative to where we are.
        rel_filename, filename = env.relfn2path(datafile)

        LOG.info('loading teamtable')
        LOG.info('reading %s' % filename)
        with open(filename, 'r') as f:
            _teams_yaml = yaml.safe_load(f.read())

        table = nodes.table()

        # Set up the column specifications
        # based on the widths.
        tgroup = nodes.tgroup(cols=len(self.HEADERS))
        table += tgroup
        tgroup.extend(nodes.colspec(colwidth=col_width)
                      for col_width in col_widths)

        # Set the headers
        thead = nodes.thead()
        tgroup += thead
        row_node = nodes.row()
        thead += row_node
        row_node.extend(
            nodes.entry(h, nodes.paragraph(text=h))
            for h in self.HEADERS
        )

        # The body of the table is made up of rows.
        # Each row contains a series of entries,
        # and each entry contains a paragraph of text.
        tbody = nodes.tbody()
        tgroup += tbody
        rows = []

        all_teams = _teams_yaml
        for team in sorted(all_teams.keys()):
            trow = nodes.row()
            # Iterate over the headers in the same order every time.
            for h in self.HEADERS:
                if h.lower() == "name":
                    cell = "<a href=\"%s\">%s</a>" % (all_teams[team]['url'], team)
                    entry = nodes.entry()
                    para = nodes.raw('', cell, format='html')
                elif h.lower() == "chairs":
                    chairs = []
                    for chair in all_teams[team]['chairs']:
                        chairs.append("%s<br />" % (chair['name']))
                    cell = "".join(chairs)
                    entry = nodes.entry()
                    para = nodes.raw('', cell, format='html')
                else:
                    # Get the cell value from the row data, replacing None
                    # in re match group with empty string.
                    cell = all_teams[team][h.lower()] or ''
                    entry = nodes.entry()
                    para = nodes.paragraph(text=str(cell))
                entry += para
                trow += entry
            rows.append(trow)
        tbody.extend(rows)

        # Build the table node
        table['classes'] += self.options.get('class', [])
        self.add_name(table)

        if title:
            table.insert(0, title)

        return [table] + messages


def setup(app):
    app.add_directive('teamtable', TeamTable)
