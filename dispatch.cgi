#!${HOME}/.local/bin/python
'''
This is a comment,
If you see this, CGI is not working
'''
import sys, os
sys.path += ['%s/.local/lib/python2.7/site-packages'%os.environ['HOME']]
sys.path += ['%/Path_To/mysite/'%os.environ['HOME']]
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


import django
django.setup()

from flup.server.fcgi import WSGIServer
from django.core.handlers.wsgi import WSGIHandler
WSGIServer(WSGIHandler()).run()
