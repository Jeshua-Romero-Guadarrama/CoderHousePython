"""
En este archivo se definen los formularios para cada modelo, incluyendo el modelo Comentario.
Esto facilita la inserción de datos en la base de datos.
"""

from django import forms
from .models import (
    Sostenibilidad,
    Fintech,
    Inclusion,
    Autor,
    Categoria,
    Etiqueta,
    Comentario
)

class SostenibilidadForm(forms.ModelForm):
    """
    Formulario para crear y editar instancias de Sostenibilidad.
    Incluye widgets para mejorar la usabilidad.
    """
    class Meta:
        model = Sostenibilidad
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'categorias', 'etiquetas']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa el título del artículo...'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe el contenido del artículo...',
                'rows': 5
            }),
            'fecha_publicacion': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'categorias': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'etiquetas': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
        }

class FintechForm(forms.ModelForm):
    """
    Formulario para crear y editar instancias de Fintech.
    """
    class Meta:
        model = Fintech
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'categorias', 'etiquetas']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del artículo de Fintech...'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Contenido detallado...',
                'rows': 5
            }),
            'fecha_publicacion': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'categorias': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'etiquetas': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
        }

class InclusionForm(forms.ModelForm):
    """
    Formulario para crear y editar instancias de Inclusion.
    """
    class Meta:
        model = Inclusion
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'categorias', 'etiquetas']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del artículo de Inclusión...'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Contenido detallado...',
                'rows': 5
            }),
            'fecha_publicacion': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'categorias': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'etiquetas': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
        }

class AutorForm(forms.ModelForm):
    """
    Formulario para crear y editar instancias de Autor.
    """
    class Meta:
        model = Autor
        fields = ['nombre', 'bio']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del autor'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Breve biografía...',
                'rows': 3
            }),
        }

class CategoriaForm(forms.ModelForm):
    """
    Formulario para crear y editar instancias de Categoria.
    """
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la categoría'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción de la categoría...',
                'rows': 3
            }),
        }

class EtiquetaForm(forms.ModelForm):
    """
    Formulario para crear y editar instancias de Etiqueta.
    """
    class Meta:
        model = Etiqueta
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la etiqueta'
            }),
        }

class ComentarioForm(forms.ModelForm):
    """
    Formulario para crear comentarios.
    El campo 'autor' y 'sostenibilidad' se asignan en la vista,
    por lo que aquí no los incluimos.
    """
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu comentario...',
                'rows': 3
            }),
        }
