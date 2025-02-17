"""
WSGI config para el proyecto 'sostenibilidad_blog'.

Provee la interfaz WSGI para servidores web que usan este protocolo.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sostenibilidad_blog.settings')

application = get_wsgi_application()