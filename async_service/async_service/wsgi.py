"""
WSGI config for dispatcher project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# site_dir = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", site_dir + ".settings")

application = get_wsgi_application()
