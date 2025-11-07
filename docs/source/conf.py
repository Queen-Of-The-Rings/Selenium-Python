import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Simple Multiply Documentation'
copyright = '2024, Christy Henitha'
author = 'Christy Henitha'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

html_theme = 'sphinx_rtd_theme'
exclude_patterns = []
html_static_path = ['_static']