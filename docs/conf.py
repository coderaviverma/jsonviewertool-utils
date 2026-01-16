# docs/conf.py
from __future__ import annotations

import datetime

project = "JSONViewerTool Utils"
author = "Avinash Verma"
copyright = f"{datetime.datetime.now().year}, {author}"

# Version shown in docs (optional: keep simple)
release = "0.1.0"
version = release

# --- Extensions ---
extensions = [
    "myst_parser",             # Markdown support
    "sphinx_copybutton",       # Copy button on code blocks
    "sphinx_sitemap",          # sitemap.xml for docs site
]

# Markdown settings
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "linkify",
    "substitution",
]
myst_heading_anchors = 3

# --- Paths / files ---
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The main toctree document
master_doc = "index"

# --- HTML output ---
html_theme = "furo"
html_title = project
html_static_path = ["_static"]

# Sitemap (Read the Docs sets canonical URL automatically)
# If you later add a custom domain for docs, you can set:
# html_baseurl = "https://<your-docs-domain>/"
sitemap_url_scheme = "{link}"

# Better code highlighting defaults
pygments_style = "default"
pygments_dark_style = "native"

# Optional: If you keep API docs later
# autodoc_default_options = {"members": True, "undoc-members": True, "show-inheritance": True}

html_theme_options = {
  "source_repository": "https://github.com/coderaviverma/jsonviewertool-utils/",
  "source_branch": "main",
  "source_directory": "docs/",
}

html_favicon = "_static/favicon.png"   # optional
html_logo = "_static/logo.png"         # optional

