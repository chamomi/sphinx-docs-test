# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import pathlib
import sys
import os
import shutil
sys.path.insert(0, os.path.abspath('./source-code'))
shutil.copytree('../../source-code', 'source-code', dirs_exist_ok=True)

project = 'Sphinx Test'
copyright = '2024, me'
author = 'me'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.autosummary'
]

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = [
	'snippets/*',
	'*.sub'
]

rst_epilog = """
.. include:: /substitutions.sub
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
