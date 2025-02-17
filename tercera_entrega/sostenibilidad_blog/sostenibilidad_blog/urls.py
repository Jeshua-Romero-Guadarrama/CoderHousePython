"""
URLs principales del proyecto sostenibilidad_blog.

El archivo enruta las peticiones a las URLs de la aplicación 'blog'.
"""

from django.contrib import admin
from django.urls import path, include
# Importamos la vista de registro desde el módulo blog.views
from blog.views import registrar_usuario, user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    # Se incluyen las URLs de la app 'blog'
    path('', include('blog.urls')),
    # URL para registro de usuarios
    path('registro/', registrar_usuario, name = 'registro'),

    # Rutas para login y logout de usuarios normales
    path('login/',  user_login,  name='login'),
    path('logout/', user_logout, name='logout'),
]
