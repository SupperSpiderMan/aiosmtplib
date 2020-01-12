#!/usr/bin/env python3
#
# aiosmtplib documentation build configuration file, created by
# sphinx-quickstart on Wed Dec  7 11:17:39 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import datetime
import os
import pathlib
import re
import sys
from typing import Dict, List


sys.path.insert(0, os.path.abspath("../src"))
sys.path.insert(0, os.path.abspath("."))


VERSION_REGEX = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "aiosmtplib"
author = "Cole Maclean"
year = datetime.date.today().year
copyright = "{year}, {author}".format(year=year, author=author)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

init = pathlib.Path("../aiosmtplib/__init__.py")
version_match = re.search(VERSION_REGEX, init.read_text("utf8"), re.MULTILINE)
if not version_match:
    raise RuntimeError("Cannot find version information")

# The short X.Y version.
version = version_match.group(1)

# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "show_powered_by": False,
    "github_user": "cole",
    "github_repo": "aiosmtplib",
    "github_banner": False,
    "show_related": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []  # type: List[str]


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "aiosmtplibdoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}  # type: Dict[str, str]

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "aiosmtplib.tex", "aiosmtplib Documentation", "Cole Maclean", "manual")
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "aiosmtplib", "aiosmtplib Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "aiosmtplib",
        "aiosmtplib Documentation",
        author,
        "aiosmtplib",
        "asyncio SMTP client",
        "Miscellaneous",
    )
]

intersphinx_mapping = {"python": ("https://docs.python.org/3.8", None)}

html_sidebars = {
    "**": ["globaltoc.html", "relations.html", "sourcelink.html", "searchbox.html"]
}

nitpick_ignore = [
    ("py:class", "typing.Tuple"),
    ("py:class", "concurrent.futures._base.TimeoutError"),
]

doctest_global_setup = """
import asyncio
import logging

from aiosmtpd.controller import Controller


aiosmtpd_logger = logging.getLogger("mail.log")
aiosmtpd_logger.setLevel(logging.ERROR)

controller = Controller(object(), hostname="127.0.0.1", port=1025)
controller.start()
"""

doctest_global_cleanup = """
controller.stop()
"""
