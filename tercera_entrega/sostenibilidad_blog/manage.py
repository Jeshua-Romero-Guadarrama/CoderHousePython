"""
Script de administración de Django.
El archivo se utiliza para ejecutar comandos de Django (por ejemplo, runserver, migrate, etc.).
"""
import os
import sys

def main():
    """
    Punto de entrada principal para la utilidad de línea de comandos de Django.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sostenibilidad_blog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y disponible en el PYTHONPATH?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
