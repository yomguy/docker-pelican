#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = "Foo Bar"
SITEURL = 'http://foobar.com'
RELATIVE_URLS = True
# AUTHOR = 'me'
# Uncomment following line if you want document-relative URLs when developing
# THEME = '/srv/lib/pelican-themes/pelican-bootstrap3'
# BOOTSTRAP_THEME = 'united'
# CUSTOM_CSS = 'themes/bootswatch/slate/slate/bootstrap.css'

PATH = '/var/in'
OUTPUT_PATH = '/var/out'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

SUMMARY_MAX_LENGTH = 127
SLUGIFY_SOURCE = 'title'
# DEFAULT_PAGINATION = 5

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('blablablabla', 'http://www.blablablabla.com'),
          )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/foobar/'),
          ('GitHub', 'https://github.com/foobar/'),
          )

DISQUS_SITENAME='foobar'
GITHUB_USER = 'foobar'
TWITTER_CARDS = True
TWITTER_USERNAME = 'foobar'
TWITTER_WIDGET_ID = '516222345451888640'

PLUGIN_PATHS = ['/srv/lib/pelican-plugins']
PLUGINS = ['assets', 'i18n_subsites', 'jinja2content', 'sitemap', 'gallery',
        #     'render_math',
        #     'liquid_tags.img', 'liquid_tags.video',
        #    'liquid_tags.youtube', 'liquid_tags.vimeo',
        #    'liquid_tags.include_code',
        #    'liquid_tags.notebook',
           ]

SITEMAP = {

    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

CC_LICENSE = "CC-BY"

# GOOGLE_ANALYTICS = 'UA-6573030-16'

GALLERY_PATH = '/var/in/img/gallery/'

PELICANGIT_SOURCE_REPO=PATH
PELICANGIT_SOURCE_REMOTE="origin"
PELICANGIT_SOURCE_BRANCH="master"
PELICANGIT_SOURCE_BRANCHES=["master",]

PELICANGIT_DEPLOY_REPO=OUTPUT_PATH
PELICANGIT_DEPLOY_REMOTE="origin"
PELICANGIT_DEPLOY_BRANCH="master"
PELICANGIT_DEPLOY_IS_LOCAL_DIR = True

PELICANGIT_USER = "root"
PELICANGIT_WHITELISTED_FILES = [
    "README.md"
]

PELICANGIT_PORT=8888

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n',]}
MARKDOWN = {'extensions': ['markdown.extensions.meta',]}

I18N_SUBSITES = {
    'fr': {
        'SITENAME': 'Fou Bar',
        }
    }
