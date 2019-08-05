#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Chris Coutinho"
SITENAME = "Chris Coutinho"
SITEURL = ""

PATH = "content"
STATIC_PATHS = ["files", "images"]
EXTRA_PATH_METADATA = {"files/keybase.txt": {"path": "keybase.txt"}}

TIMEZONE = "Europe/Amsterdam"

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

ABOUT = {
    "mail": "chrisbcoutinho@gmail.com",
    "address": "Amsterdam, The Netherlands",
    "link": "contact.html",
    "text": "Feel free to drop a message",
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
