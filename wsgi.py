import os
import sys
sys.path.append('/home/dotcloud/data')
sys.path.append('/home/dotcloud/data/Cockpit')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Cockpit.settings'
import django.core.handlers.wsgi
djangoapplication = django.core.handlers.wsgi.WSGIHandler()
def application(environ, start_response):
    if 'SCRIPT_NAME' in environ:
        del environ['SCRIPT_NAME']
    return djangoapplication(environ, start_response)

