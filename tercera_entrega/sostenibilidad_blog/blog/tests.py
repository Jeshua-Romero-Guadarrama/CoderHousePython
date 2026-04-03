"""
Archivo para pruebas unitarias de la aplicación 'blog'.
"""
from django.test import TestCase
from .models import Sostenibilidad

class BlogTestCase(TestCase):
    """Pruebas para la aplicación blog."""
    def test_crear_Sostenibilidad(self):
        """
        Verifica que se pueda crear un objeto de tipo Sostenibilidad 
        y se guarde correctamente en la base de datos.
        """
        obj = Sostenibilidad.objects.create(
            titulo="Prueba de Sostenibilidad",
            contenido="Contenido de prueba para sostenibilidad",
        )
        self.assertEqual(obj.titulo, "Prueba de Sostenibilidad")
        self.assertTrue(Sostenibilidad.objects.filter(titulo="Prueba de Sostenibilidad").exists())