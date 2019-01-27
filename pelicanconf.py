#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Theo Windebank'
SITENAME = 'Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'GMT'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# THEME
MAIN_MENU = False

LINKS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

SITETITLE = "THEO WINDEBANK"
SITESUBTITLE = "An experimental blog..."
SITELOGO = "images/me.jpg"

SOCIAL = (('linkedin', 'https://linkedin.com/in/twindebank'),
          ('github', 'https://github.com/twindebank'))

DEFAULT_PAGINATION = 5

THEME = "themes/Flex"

FAVICON = 'images/favicon.png'

RELATIVE_URLS = True

COPYRIGHT_YEAR = 2019

# ADD_THIS_ID = 'ra-77hh6723hhjd'
# DISQUS_SITENAME = 'yoursite'
GOOGLE_ANALYTICS = 'UA-23081119-2'
PYGMENTS_STYLE = 'monokai'

STATIC_PATHS = [
    'css/customstyles.css',
]

CUSTOM_CSS = 'css/customstyles.css'
