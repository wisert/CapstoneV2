"""
WSGI config for CapstoneV2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CapstoneV2.settings")

"""Added this based on a tutorial on pythonanywhere.com - 1/29/2016"""
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
