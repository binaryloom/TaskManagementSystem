# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

import django

project = "Task MS"
copyright = "2024, Sabbir Ahmed Shourov"
author = "Sabbir Ahmed Shourov"
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
sys.path.insert(0, os.path.abspath("../src"))

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    #  new
    # "sphinx.ext.autosectionlabel",
    # "sphinx.ext.autosummary",
    # "myst_parser",
]

django_settings = "tms.settings"
django_show_db_tables = True
django_show_db_tables_abstract = True


templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]


os.environ["DJANGO_SETTINGS_MODULE"] = "tms.settings"
django.setup()
