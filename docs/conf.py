import os
import sys

from django import setup as django_setup
from django.conf import settings

sys.path.insert(0, os.path.abspath("../src/django_listview_filters/"))
print("Path: {}".format(sys.path[0]))
settings.configure()

django_setup()

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Django ListView Filters"
copyright = "2022, Karl Wooster"
author = "Karl Wooster"
release = "0.0.1b0.dev1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
