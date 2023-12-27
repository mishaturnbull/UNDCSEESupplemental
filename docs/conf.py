# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'UNDCSEESupplemental'
copyright = '2023, UND CS / EE Supplementary Information Team'
author = 'UND CS / EE Supplementary Information Team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'sphinx.ext.todo',
        'sphinx.ext.intersphinx',
        'myst_parser',
        'sphinx_copybutton',
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# set parser based on filetype
source_suffix = {
        '.rst': 'restructuredtext',
        '.md': 'markdown',
    }

nitpicky = True

# -- Options for ToDo extension ----------------------------------------------

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_theme_options = {
        "repository_url": "https://github.com/mishaturnbull/UNDCSEESupplemental",
        "path_to_docs": "docs",
        "use_repository_button": True,
        "use_source_button": True,
        "use_edit_page_button": True,
        "use_issues_button": True,
    }

