#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican_jupyter import markup as nb_markup

AUTHOR = "Chris Coutinho"
SITENAME = "Chris Coutinho"
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
}

PLUGIN_PATHS = [
    # "/home/chris/Software/pelican-plugins",
    # "/home/chris/Software"
]

MARKUP = ("md", "ipynb")
PLUGIN = [nb_markup]
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
    # ("Pelican", "http://getpelican.com/"),
    # ("Python.org", "http://python.org/"),
    # ("Jinja2", "http://jinja.pocoo.org/"),
    # ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("Github", "https://www.github.com/cbcoutinho"),
    ("LinkedIn", "https://www.linkedin.com/in/cbcoutinho/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
