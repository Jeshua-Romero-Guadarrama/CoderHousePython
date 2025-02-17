"""
Archivo para el registro de modelos en el panel de administración de Django.
En este archivo se pueden personalizar las columnas y opciones de filtrado.
"""

from django.contrib import admin
from .models import (
    Sostenibilidad,
    Fintech,
    Inclusion,
    Autor,
    Categoria,
    Etiqueta,
    Comentario
)


@admin.register(Sostenibilidad)
class SostenibilidadAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'fecha_publicacion')
    search_fields = ('titulo',)


@admin.register(Fintech)
class FintechAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'fecha_publicacion')
    search_fields = ('titulo',)


@admin.register(Inclusion)
class InclusionAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'fecha_publicacion')
    search_fields = ('titulo',)


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'bio')
    search_fields = ('nombre',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display  = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    """
    Administrador del modelo Comentario.
    Se muestra el autor, parte del contenido y la fecha.
    """
    list_display  = ('autor', 'contenido_corto', 'fecha', 'sostenibilidad')
    search_fields = ('autor__username', 'contenido')

    def contenido_corto(self, obj):
        # Retornar solo los primeros 50 caracteres del comentario.
        return obj.contenido[:50] + "..."
    contenido_corto.short_description = 'Contenido (corto)'
