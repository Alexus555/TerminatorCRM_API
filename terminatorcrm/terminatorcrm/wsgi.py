"""
WSGI config for terminatorcrm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.auth.handlers.modwsgi import check_password


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'terminatorcrm.settings')

application = get_wsgi_application()

