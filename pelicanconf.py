#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Casey Marshall'
SITENAME = u'cmars blog'
SITEURL = 'https://cmars.github.com'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

FEED_DOMAIN = 'https://cmars.github.com'

# Blogroll
#MENUITEMS = (('Hockeypuck', 'https://launchpad.net/hockeypuck'),
			#('Conflux', 'https://github.com/cmars/conflux'),
		#)

# Social widget
PROJECTS = (
			('cmars on github', 'https://github.com/cmars'),
			('cmars on launchpad', 'https://launchpad.net/cmars'),
)

CONTACT = (
			('PGP Public Key: 44A2D1DB', 'http://keyserver.gazzang.net/pks/lookup?op=get&search=0x81279eee7ec89fb781702adaf79362da44a2d1db'),
)

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True

#THEME="basic"
THEME="./dirtsimple"
#THEME="tuxlite_tbs"
#THEME="bootstrap2"
