# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import importlib.util
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def get_py_config(path: Path | str):
    """Get dynimic values from python code.

    Uses importlib.util tricks to import without the problems of edit sys.path
    and python lint missing imports

    .. note::
        This function will execute the input file

    from:
    https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
    """
    module_name = Path(path).name

    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)

    # sys.mod is good to set
    sys.modules[module_name] = module

    # Execte the imported file
    spec.loader.exec_module(module)

    return module


# -- Path setup --------------------------------------------------------------
docs_path = Path(__file__).absolute().parent
project_path = docs_path.parent

# extract out the repo name from git
repo_name = Path(
    subprocess.check_output(["git", "config", "--get", "remote.origin.url"])  # noqa: S603, S607
    .decode("utf-8")
    .strip(),
).stem

# per python standard you "can't" use import names with dash
repo_name = repo_name.replace("-", "_")

source_path = project_path / repo_name

# Add path for sphinx to find
sys.path.extend([str(docs_path), str(project_path), str(source_path)])

# -- Project information -----------------------------------------------------

project = repo_name

author = "Viktor Freiman"
copyright = f"{datetime.now().year}, {author}"  # noqa: A001, DTZ005

# The full version, including alpha/beta/rc tags
# https://pdm.fming.dev/latest/pyproject/build/#dynamic-version-from-file
release = get_py_config(source_path / "__init__.py").__version__

# set version to display it in the sidebar
version = release

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "sphinx.ext.graphviz",
    "sphinx.ext.ifconfig",
    "sphinx.ext.imgmath",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxcontrib.kroki",
]


try:
    # PDF output is a bit special in sphinx
    # rinotype don't have super good support with all sphinx extensions
    if sys.argv[2] == "rinoh":
        # https://github.com/sphinx-contrib/kroki
        # formats = ("png", "svg", "jpeg", "base64", "txt", "utxt")
        # Only png is supported by rinohtype(PDF) output
        kroki_output_format = "png"
except IndexError:
    pass

# --- Autodoc ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
# https://stackoverflow.com/a/61732050
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}
# To not inclued undoc-members
# You can use a negated form, 'no-flag', as an option of autodoc directive,
# to disable it temporarily. For example:
# .. automodule:: foo
#    :no-undoc-members:

# --- Intersphinx ----------------------------------------
# Use docs-helper to help with linking
# http://docs-helper.rtfd.io/
# https://docs.readthedocs.io/en/stable/guides/intersphinx.html
# check with https://github.com/bskinn/sphobjinv

intersphinx_mapping = {
    "py3": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {"display_version": True}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If this is not None, a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime() format.
# The empty string is equivalent to '%b %d, %Y' (or a locale-dependent equivalent).
html_last_updated_fmt = ""

manpages_url = "https://manpages.debian.org/{path}"

# --- Options for rinohtype (PDF output) -----------------------------------
# http://www.mos6581.org/rinohtype/master/sphinx.html#confval-rinoh_template

# rinoh --list-templates
rinoh_documents = [
    dict(doc="index", target="manual", template="article"),  # noqa: C408
]

# replace in all rst files
rst_prolog = f"""
.. |project| replace:: {project}
"""
