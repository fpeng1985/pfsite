#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Theme 
THEME = "themes/Flex"

AUTHOR = '彭斐'
SITEDESCRIPTION = '非文随想'
SITENAME = '非文'
SITEURL = ''
SITELOGO = SITEURL + '/images/profile.jpg'

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

MAIN_MENU = True

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'ch'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PATH = 'content'
STATIC_PATHS=["images"]
PLUGIN_PATHS=["plugins"]
