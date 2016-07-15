# -*- coding: utf-8 -*-

extensions = [
    'sphinx.ext.ifconfig',
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'pytest-rethinkdb'
copyright = u'2015, Sylvain Bellemare'
author = u'Sylvain Bellemare'

version = '0.1.0'
release = '0.1.0'

language = None

exclude_patterns = ['_build']

pygments_style = 'sphinx'

todo_include_todos = False

html_theme = 'alabaster'

html_static_path = ['_static']

htmlhelp_basename = 'pytest-rethinkdb_namedoc'
