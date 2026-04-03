"""
Archivo de configuración de la aplicación 'blog'.

Define la clase de configuración de la app para que Django la reconozca.
"""
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name               = 'blog'
    verbose_name       = "Blog de Sostenibilidad, Fintech e Inclusión"