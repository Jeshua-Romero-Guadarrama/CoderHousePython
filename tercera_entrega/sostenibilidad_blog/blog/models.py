"""
En este archivo se definen los modelos de base de datos para la aplicación 'blog'.
Existen 6 modelos principales: 
- Sostenibilidad.
- Fintech.
- Inclusion. 
- Autor.
- Categoria. 
- Etiqueta.
Además, se agrega el modelo Comentario para gestionar comentarios de los usuarios.
Se han añadido campos ManyToMany en Sostenibilidad, Fintech e Inclusion para enlazar con Categoría y Etiqueta.
"""

from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    """
    Modelo que representa un autor de artículos.
    Contiene el nombre y una biografía breve.
    """
    nombre = models.CharField(max_length = 100, help_text = "Nombre del autor")
    bio    = models.TextField(help_text = "Breve biografía del autor", null = False, blank = True)
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    """
    Modelo que representa una categoría para clasificar artículos.
    Contiene el nombre de la categoría y su descripción.
    """
    nombre      = models.CharField(max_length = 100, help_text = "Nombre de la categoría")
    descripcion = models.TextField(help_text = "Descripción de la categoría", null = False, blank = True)
    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    """
    Modelo que representa una etiqueta para clasificar artículos.
    Contiene el nombre de la etiqueta.
    """
    nombre = models.CharField(max_length = 50, help_text = "Nombre de la etiqueta")
    def __str__(self):
        return self.nombre

class Sostenibilidad(models.Model):
    """
    Modelo que representa un artículo de Sostenibilidad.
    Contiene un título, el contenido y la fecha de publicación, más relaciones con categorías y etiquetas.
    """
    titulo            = models.CharField(max_length = 200, help_text = "Título del artículo de sostenibilidad")
    contenido         = models.TextField(help_text = "Contenido detallado del artículo de sostenibilidad")
    fecha_publicacion = models.DateField(help_text = "Fecha de publicación", null = True, blank = True)
    categorias        = models.ManyToManyField(Categoria, blank = True)
    etiquetas         = models.ManyToManyField(Etiqueta, blank = True)
    autor             = models.ForeignKey(Autor, on_delete = models.SET_NULL, null = True, blank = True)
    def __str__(self):
        return self.titulo

class Fintech(models.Model):
    """
    Modelo que representa un artículo sobre Fintech.
    Contiene un título, el contenido y la fecha de publicación, más relaciones con categorías y etiquetas.
    """
    titulo            = models.CharField(max_length = 200, help_text = "Título del artículo de fintech")
    contenido         = models.TextField(help_text = "Contenido detallado del artículo de fintech")
    fecha_publicacion = models.DateField(help_text = "Fecha de publicación", null = True, blank = True)
    categorias        = models.ManyToManyField(Categoria, blank = True)
    etiquetas         = models.ManyToManyField(Etiqueta, blank = True)
    autor             = models.ForeignKey(Autor, on_delete = models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return self.titulo

class Inclusion(models.Model):
    """
    Modelo que representa un artículo sobre Inclusión Financiera.
    Contiene un título, el contenido y la fecha de publicación, más relaciones con categorías y etiquetas.
    """
    titulo            = models.CharField(max_length = 200, help_text = "Título del artículo de inclusión financiera")
    contenido         = models.TextField(help_text = "Contenido detallado del artículo de inclusión financiera")
    fecha_publicacion = models.DateField(help_text = "Fecha de publicación", null = True, blank = True)
    categorias        = models.ManyToManyField(Categoria, blank=True)
    etiquetas         = models.ManyToManyField(Etiqueta, blank=True)
    autor             = models.ForeignKey(Autor, on_delete = models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    """
    Modelo que representa un comentario realizado por un usuario.
    Se asocia al usuario (autor del comentario) y a un artículo de Sostenibilidad.
    """
    autor          = models.ForeignKey(User, on_delete = models.CASCADE, help_text = "Usuario autor del comentario")
    contenido      = models.TextField(help_text = "Texto del comentario")
    fecha          = models.DateTimeField(auto_now_add = True, help_text = "Fecha y hora de creación del comentario")
    sostenibilidad = models.ForeignKey(Sostenibilidad, on_delete = models.CASCADE, null = True, blank = True, help_text = "Artículo de Sostenibilidad al que pertenece este comentario")

    def __str__(self):
        fecha_formateada = self.fecha.strftime('%d/%m/%Y %H:%M')
        return f"Comentario de {self.autor} el {fecha_formateada}"
