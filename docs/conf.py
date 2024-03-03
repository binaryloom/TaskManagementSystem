import os
import sys

import django

project = "Task MS"
copyright = "2024, Sabbir Ahmed Shourov"
author = "Sabbir Ahmed Shourov"
release = "1.0"


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


html_theme = "furo"
html_static_path = ["_static"]


os.environ["DJANGO_SETTINGS_MODULE"] = "tms.settings"
django.setup()
