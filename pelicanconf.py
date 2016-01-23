#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'zz'
SITENAME = "zz\'s Blog"
SITEURL = ''

PATH = 'content'



TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

LINKS = []

# Social widget
# SOCIAL = (('You can add links in your config file', 'http://github.com/littlezz'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True



MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', ]

THEME = 'pelican-themes/theme'





SITETITLE = 'zz'
SITESUBTITLE = '当我被狗日时， 我在想些什么'
SITEDESCRIPTION = 'zz\'s Thoughts and Writings'
SITELOGO = '/images/logo.jpg'

# FAVICON = SITEURL + '/images/favicon.ico'
# ROBOTS = 'index, follow'

COPYRIGHT_YEAR = 2015
# CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa' }

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'



MAIN_MENU = True
MENUITEMS = [
	('Category', '/categories'),
	('Tags', '/tags'),
]

STATUSCAKE=False

# SOCIAL = (('linkedin', 'https://br.linkedin.com/in/alexandrevicenzi/en'),
#           ('github', 'https://github.com/alexandrevicenzi'),)
# ADD_THIS_ID = 'ra-77hh6723hhjd'
# DISQUS_SITENAME = 'yoursite'
# GOOGLE_ANALYTICS = 'UA-1234-5678'
# GOOGLE_TAG_MANAGER = 'GTM-ABCDEF'
# STATUSCAKE = { 'trackid': 'your-id', 'days': 7 }
