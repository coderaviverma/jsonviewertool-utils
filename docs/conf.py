# docs/conf.py
# Sphinx config for JSONViewerTool Utils (Java library) using MyST Markdown.
# Works on Read the Docs with .readthedocs.yaml pointing to docs/conf.py

import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------

project = "JSONViewerTool Utils"
author = "Avinash Verma"
copyright = f"{datetime.now().year}, {author}"

# If you want, you can hardcode this; otherwise RTD will still build fine.
release = os.environ.get("READTHEDOCS_VERSION_NAME", "0.1.0")

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",                 # Markdown support
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",         # Google/Numpy style docstrings (optional)
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.autosectionlabel", # Stable anchors for headings
    "sphinx_copybutton",           # Copy button on code blocks (nice UX)
    "sphinx_sitemap",              # SEO sitemap for docs site
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Source files: Markdown + (optional) reStructuredText
source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

# -- MyST (Markdown) configuration ------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "linkify",
    "substitution",
    "tasklist",
]
myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_title = project

# Put your logo here if you have one:
# docs/_static/logo.png
html_logo = None

html_static_path = ["_static"]
html_favicon = None  # e.g. "_static/favicon.ico"

# Better SEO + nicer meta
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")
html_theme_options = {
    "navigation_with_keys": True,
}

# Sitemap config (requires html_baseurl to be set on RTD)
sitemap_url_scheme = "{link}"

# -- Intersphinx -------------------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", {}),
}

# -- External links shortcuts ------------------------------------------------
extlinks = {
    "gh": ("https://github.com/coderaviverma/jsonviewertool-utils/%s", "%s"),
    "mvn": ("https://repo1.maven.org/maven2/com/jsonviewertool/jsonviewertool-utils/%s", "%s"),
}

# -- Autosectionlabel --------------------------------------------------------
autosectionlabel_prefix_document = True
