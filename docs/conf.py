"""Sphinx configuration."""
from __future__ import annotations

import sys
from pathlib import Path

import urllib3
from dotenv import load_dotenv

from src.__metadata__ import __project__ as project
from src.__metadata__ import __version__ as version

# -- Environmental Data ------------------------------------------------------
path = Path("..").resolve()
tls_verify = False
urllib3.disable_warnings()
sys.path.insert(0, path.as_posix())
load_dotenv()

# -- Project information -----------------------------------------------------
project = project
version = version
release = version
copyright = "2023, Jacob Coffee"
author = "Jacob Coffee"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_click",
    "sphinx_toolbox.collapse",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "anyio": ("https://anyio.readthedocs.io/en/stable/", None),
    "click": ("https://click.palletsprojects.com/en/8.1.x/", None),
    "structlog": ("https://www.structlog.org/en/stable/", None),
    "opentelemetry": ("https://opentelemetry-python.readthedocs.io/en/latest/", None),
    "litestar": ("https://docs.litestar.dev/2/", None),
    "msgspec": ("https://jcristharif.com/msgspec/", None),
}

napoleon_google_docstring = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_attr_annotations = True

autoclass_content = "both"
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "exclude-members": "__weakref__",
    "show-inheritance": True,
    "class-signature": "separated",
    "typehints-format": "short",
}

nitpicky = False  # This is too much of a headache right now
nitpick_ignore = []
nitpick_ignore_regex = []

# with Path("nitpick-exceptions").open() as file:
#     for line in file:
#         if line.strip() == "" or line.startswith("#"):
#             continue
#         dtype, target = line.split(None, 1)
#         target = target.strip()
#         nitpick_ignore.append((dtype, target))
#
# with Path("nitpick-exceptions-regex").open() as file:
#     for line in file:
#         if line.strip() == "" or line.startswith("#"):
#             continue
#         dtype, target = line.split(None, 1)
#         target = target.strip()
#         nitpick_ignore_regex.append((dtype, target))

autosectionlabel_prefix_document = True
suppress_warnings = [
    "autosectionlabel.*",
    "ref.python",  # TODO: remove when https://github.com/sphinx-doc/sphinx/issues/4961 is fixed
]
todo_include_todos = True

# -- Style configuration -----------------------------------------------------
html_theme = "shibuya"
html_static_path = ["_static"]
# html_css_files = [
#     "custom.css",
# ]
html_show_sourcelink = True
html_title = "Docs"
html_favicon = "_static/badge.svg"
html_logo = "_static/badge.svg"
html_context = {
    "source_type": "github",
    "source_user": "JacobCoffee",
    "source_repo": "litestar-template",
}

brand_colors = {
    "--litestar-blue": "32, 34, 53",
    "--litestar-gold": "237, 182, 65",
}

html_theme_options = {
    "logo_target": "/",
    "announcement": "This documentation is currently under development.",
    "github_url": "https://github.com/JacobCoffee/litestar-template",
    "discord_url": "https://discord.gg/MmcwxztmQb/",
    "twitter_url": "https://twitter.com/_scriptr",
    "youtube_url": "https://youtube.com/@monorepo",
    "nav_links": [
        {
            "title": "Sponsor me",
            "url": "https://github.com/sponsors/JacobCoffee",
            "icon": "accessibility",
        },
    ],
    "light_css_variables": {
        "--sy-rc-theme": "32, 34, 53",
        # "--sy-c-foot-bg": "255, 0, 0",
        "--sy-c-foot-divider": brand_colors["--litestar-blue"],
        # "--sy-c-foot-text": "255, 0, 0",
        # "--sy-c-bold": "255, 0, 0",
        "--sy-c-heading": brand_colors["--litestar-blue"],
        # "--sy-c-text-weak": "255, 0, 0",
        # "--sy-c-text": "255, 0, 0",
        "--sy-rc-text": brand_colors["--litestar-blue"],
        # "--sy-rc-invert": "255, 0, 0",
        # "--sy-rc-bg": "255, 0, 0",
        "--sy-c-link": brand_colors["--litestar-blue"],
    },
    "dark_css_variables": {
        "--sy-rc-theme": "32, 34, 53",
        "--sy-c-foot-bg": brand_colors["--litestar-blue"],
        "--sy-c-foot-divider": brand_colors["--litestar-blue"],
        # "--sy-c-foot-text": "255, 0, 0",
        # "--sy-c-bold": "255, 0, 0",
        "--sy-c-heading": brand_colors["--litestar-blue"],
        # "--sy-c-text-weak": "255, 0, 0",
        # "--sy-c-text": "255, 0, 0",
        "--sy-rc-text": brand_colors["--litestar-blue"],
        # "--sy-rc-invert": "255, 0, 0",
        # "--sy-rc-bg": "255, 0, 0",
        "--sy-c-link": brand_colors["--litestar-blue"],
    },
}
