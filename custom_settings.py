# -*- coding: utf-8 -*-

import os, json
envfilepath = os.path.join('/home/dotcloud/environment.json')
environment = json.load(open(envfilepath))

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME='template1'
DATABASE_USER=environment['DOTCLOUD_DB_SQL_LOGIN']
DATABASE_PASSWORD=environment['DOTCLOUD_DB_SQL_PASSWORD']
DATABASE_HOST=environment['DOTCLOUD_DB_SQL_HOST']
DATABASE_PORT=int(environment['DOTCLOUD_DB_SQL_PORT'])

# Make this unique, and don't share it with anybody.
SECRET_KEY='unconfigured-cockpit' # XXX FIXME

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'cockpit',
    'newsletter',
    'emencia_django_admin',
)

AUTHENTICATION_BACKENDS = (
# 'backends.caasauth.CaasBackend',
 'django.contrib.auth.backends.ModelBackend',
 )


# Email sent by the system for passwords, etc. (not NL)
DEFAULT_FROM_EMAIL = "unconfigured-cockpit@dotcloud.com"

# Tag separator
TAG_SEPARATOR = ","

# Specify default tag when create a new contact
DEFAULT_TAGS = ""

# You can chose a title here
TEMPLATE_TITLE = "COCKPIT NON CONFIGUR&Eacute;"
TEMPLATE_TITLE = "<span style='font-size: xx-large;'>%s</span>" % TEMPLATE_TITLE

# Password file configuration
MASTER_PASSWORD_FILE = "/etc/cockpit.users"

#
# Newsletter configuration
#

# Chose one SMTP sender here
# Available are :
# - SMTPMailSender for direct SMTP send
# - MailDropMailSender for sending through maildrop
NL_BACKEND = "SMTPMailSender" 

# For maildrop
NL_MAILDROP_PATH = "/var/spool/maildrop"
# Enable newsletter duplicate filtering ?
NL_FILTER_DUPLICATE = True

# Use VERP ?
NL_VERP_ENABLED = False
# The verp address to use, with %s being replaced by the variable part
NL_VERP_BASE = "cockpitng+%s@pilotsystems.net"

# Pop method to use, can be POP3 or POP3_SSL
NL_VERP_METHOD = "POP3_SSL"
# Pop parameters
NL_VERP_SERVER = "chico.pilotsystems.net"
NL_VERP_USERNAME = "cockpitng@pilotsystems.net"
NL_VERP_PASSWORD = ""

# REST API Parameters
REST_ALLOWED_REMOTE_ADDR = ()
REST_ALLOWED_X_FORWARDED_FOR = ()
