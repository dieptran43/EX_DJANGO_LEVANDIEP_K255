"""
ASGI config for Ex_Django_K255_LeVanDiep project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ex_Django_K255_LeVanDiep.settings')

application = get_asgi_application()
