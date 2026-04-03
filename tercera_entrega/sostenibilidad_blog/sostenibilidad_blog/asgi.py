"""
ASGI config para el proyecto 'sostenibilidad_blog'.

Provee una interfaz ASGI para servidores web asíncronos.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sostenibilidad_blog.settings')

application = get_asgi_application()