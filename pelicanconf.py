#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import pathlib

AUTHOR = "Chris Coutinho"
SITENAME = "Chris' blog"
# SITESUBTITLE = ""

THEME = "./themes/future-imperfect"

# NOTE: This must stay empty to allow for local development. It's reset in
# publishconf.py during deployment
SITEURL = ""
TIMEZONE = "Europe/Amsterdam"

PATH = "content"
STATIC_PATHS = ["files", "images"]

# This moves the keybase.io proof from a subdirectory to the site root
#   http://docs.getpelican.com/en/stable/settings.html#metadata
EXTRA_PATH_METADATA = {
    "files/keybase.txt": {"path": "keybase.txt"},
    "files/CNAME": {"path": "CNAME"},
    "files/favicon.ico": {"path": "favicon.ico"},
    "files/.nojekyll": {"path": ".nojekyll"},
}

PLUGIN_PATHS = [
    # "/home/chris/Software/pelican-plugins",
    # "/home/chris/Software"
]

MARKUP = ("md", "ipynb")
PLUGIN = []
IGNORE_FILES = [".ipynb_checkpoints", "*draft*"]

DEFAULT_LANG = "en"
DEFAULT_DATE = "fs"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Rotaract Amsterdam", "https://rotaractamsterdam.nl/"),
    ("DataChef", "https://datachef.co"),
)

# Social widget
SOCIAL = (
    ("Github", "github", "https://www.github.com/cbcoutinho"),
    ("LinkedIn", "linkedin", "https://www.linkedin.com/in/cbcoutinho/"),
    ("Instagram", "instagram", "https://www.instagram.com/chrisbcoutinho"),
)

DEFAULT_PAGINATION = 3

# github.com/pelican-plugins/liquid-tags
LIQUID_TAGS = ["img", "notebook"]

# EXTRA_HEADER = pathlib.Path("_nb_header.html").read_text(encoding="utf-8")

MARKDOWN = {
    "extension_configs": {
        # Needed for code syntax highlighting
        # NOTE: To create the css for a particular style, check docs
        #
        # pygmentize -S default -f html -a .highlight > themes/future-imperfect/static/css/default.css
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        # This is for enabling the TOC generation
        "markdown.extensions.toc": {"title": "Table of Contents"},
    },
    "output_format": "html5",
}

# pelican-sitemap plugin
SITEMAP = {
    "format": "xml",
    "exclude": [
        "^/noindex/",  # starts with "/noindex/"
        "/tag/",  # contains "/tag/"
        r"\.json$",  # ends with ".json"
    ],
}

# ARTICLE_URL = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/"
# ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html"
# PAGE_URL = "pages/{slug}/"
# PAGE_SAVE_AS = "pages/{slug}/index.html"
