import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Tax Software Help'
author = 'Admin'

extensions = ['myst_parser']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'

html_theme = 'alabaster'
html_title = "TurboTax Help Guide 2026"
