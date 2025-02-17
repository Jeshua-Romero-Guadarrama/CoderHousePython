"""
Archivo de URLs de la aplicación 'blog'.
Enruta las diferentes vistas a sus URLs.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Portada / Inicio
    path('',                         views.inicio, name='inicio'),
    
    # Listados de artículos (cualquiera puede verlos)
    path('sostenibilidad/',          views.listar_sostenibilidades, name='listar_sostenibilidades'),
    path('fintech/',                 views.listar_fintech, name='listar_fintech'),
    path('inclusion/',               views.listar_inclusion, name='listar_inclusion'),

    # Vistas de detalle para Sostenibilidad (comentarios)
    path('sostenibilidad/<int:pk>/', views.detalle_sostenibilidad, name='detalle_sostenibilidad'),

    # Vistas de creación (solo superuser)
    path('crear_sostenibilidad/',    views.crear_sostenibilidad, name='crear_sostenibilidad'),
    path('crear_fintech/',           views.crear_fintech,        name='crear_fintech'),
    path('crear_inclusion/',         views.crear_inclusion,      name='crear_inclusion'),
    path('crear_autor/',             views.crear_autor,          name='crear_autor'),
    path('crear_categoria/',         views.crear_categoria,      name='crear_categoria'),
    path('crear_etiqueta/',          views.crear_etiqueta,       name='crear_etiqueta'),

    # Vistas de búsqueda
    path('formulario_busqueda/',     views.formulario_busqueda,  name='formulario_busqueda'),
    path('resultados_busqueda/',     views.resultados_busqueda,  name='resultados_busqueda'),
]
