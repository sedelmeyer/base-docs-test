# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

# import sphinx_bootstrap_theme

# -- Project information -----------------------------------------------------

project = 'basedata'
copyright = '2020, mike sedelmeyer'
author = 'mike sedelmeyer'

# The full version, including alpha/beta/rc tags
release = 'v0.2.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_logo = '_static/logo.png'
html_favicon = '_static/favicon.ico'

#-- theme options ------------------------------------------------------------

# html_theme_options = {
#     'navbar_title': ' ',
#     'bootswatch_theme': 'spacelab',
#     'source_link_position': "footer",
#     'navbar_links': [
#         ('Math stuff', 'math'),
#         ('About Mike', 'https://www.sedelmeyer.net/')
#     ],
#     'navbar_sidebarrel': False,
# }

# html theme options for alabaster
html_theme_options = {
    # 'logo': 'logo.png',
    'logo_name': 'true',
    'github_user': 'sedelmeyer',
    'github_repo': 'basedata',
    'fixed_sidebar': 'false',
    'description': 'This is a short description of the project',
    'badge_branch': 'master',
    'github_banner': 'true',
    'github_button': 'true',
    'travis_button': 'true',
    'show_relbars': 'true',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------
html_baseurl = 'https://sedelmeyer.github.io/basedata'
