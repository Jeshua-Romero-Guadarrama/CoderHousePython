"""
Archivo de vistas (controladores) de la aplicación 'blog'.
Define la lógica para manejar las solicitudes y responder con las plantillas adecuadas.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Importamos nuestros modelos
from .models import (
    Sostenibilidad,
    Fintech,
    Inclusion,
    Comentario
)

# Importamos los formularios
from .forms import (
    SostenibilidadForm,
    FintechForm,
    InclusionForm,
    AutorForm,
    CategoriaForm,
    EtiquetaForm,
    ComentarioForm
)


# ---------------------------------------------------------------------
# DECORADOR para restringir el acceso SOLO a superusuarios
# ---------------------------------------------------------------------
def super_usuario(view_func):
    """
    Decorador que permite el acceso a una vista solamente a usuarios superusuarios.
    Si el usuario no es superusuario, se lanza un error 403 (Forbidden).
    """
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("No tienes permisos para acceder a esta funcionalidad.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# ---------------------------------------------------------------------
# VISTAS DE LISTADO (para ver los artículos como blog)
# ---------------------------------------------------------------------
def listar_sostenibilidades(request):
    """
    Muestra la lista de todos los artículos de Sostenibilidad.
    Cualquiera puede acceder.
    """
    sostenibilidades = Sostenibilidad.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/listar_sostenibilidad.html', {
        'sostenibilidades': sostenibilidades
    })


def listar_fintech(request):
    """
    Muestra la lista de todos los artículos de Fintech.
    Cualquiera puede acceder.
    """
    fintechs = Fintech.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/listar_fintech.html', {
        'fintechs': fintechs
    })


def listar_inclusion(request):
    """
    Muestra la lista de todos los artículos de Inclusión.
    Cualquiera puede acceder.
    """
    inclusiones = Inclusion.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/listar_inclusion.html', {
        'inclusiones': inclusiones
    })


# ---------------------------------------------------------------------
# VISTA PRINCIPAL (Portada / Inicio)
# ---------------------------------------------------------------------
def inicio(request):
    """
    Vista para la página de inicio.
    Si el usuario no está autenticado, se le invita a registrarse o iniciar sesión.
    Si sí está autenticado, se le da la bienvenida y se muestra el enlace a las distintas secciones.
    """
    return render(request, 'blog/inicio.html')


# ---------------------------------------------------------------------
# VISTAS DE CREACIÓN (solo superusuario)
# ---------------------------------------------------------------------
@super_usuario
def crear_sostenibilidad(request):
    """
    Vista para crear un nuevo objeto de Sostenibilidad.
    Solo superusuarios pueden crear.
    Utiliza el formulario SostenibilidadForm.
    """
    if request.method == 'POST':
        form = SostenibilidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Artículo de Sostenibilidad creado con éxito.")
            return redirect('listar_sostenibilidades')
    else:
        form = SostenibilidadForm()
    return render(request, 'blog/crear_sostenibilidad.html', {'form': form})


@super_usuario
def crear_fintech(request):
    """
    Vista para crear un nuevo objeto de Fintech.
    Solo superusuarios pueden crear.
    Utiliza el formulario FintechForm.
    """
    if request.method == 'POST':
        form = FintechForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Artículo de Fintech creado con éxito.")
            return redirect('listar_fintech')
    else:
        form = FintechForm()
    return render(request, 'blog/crear_fintech.html', {'form': form})


@super_usuario
def crear_inclusion(request):
    """
    Vista para crear un nuevo objeto de Inclusión.
    Solo superusuarios pueden crear.
    Utiliza el formulario InclusionForm.
    """
    if request.method == 'POST':
        form = InclusionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Artículo de Inclusión creado con éxito.")
            return redirect('listar_inclusion')
    else:
        form = InclusionForm()
    return render(request, 'blog/crear_inclusion.html', {'form': form})


@super_usuario
def crear_autor(request):
    """
    Vista para crear un nuevo objeto de Autor.
    Solo superusuarios pueden crear.
    Utiliza el formulario AutorForm.
    """
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor creado con éxito.")
            return redirect('inicio')
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})


@super_usuario
def crear_categoria(request):
    """
    Vista para crear un nuevo objeto de Categoria.
    Solo superusuarios pueden crear.
    Utiliza el formulario CategoriaForm.
    """
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría creada con éxito.")
            return redirect('inicio')
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})


@super_usuario
def crear_etiqueta(request):
    """
    Vista para crear un nuevo objeto de Etiqueta.
    Solo superusuarios pueden crear.
    Utiliza el formulario EtiquetaForm.
    """
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Etiqueta creada con éxito.")
            return redirect('inicio')
    else:
        form = EtiquetaForm()
    return render(request, 'blog/crear_etiqueta.html', {'form': form})


# ---------------------------------------------------------------------
# VISTAS DE BÚSQUEDA
# ---------------------------------------------------------------------
def formulario_busqueda(request):
    """
    Vista que muestra el formulario de búsqueda.
    Renderiza la plantilla 'formulario_busqueda.html'.
    """
    return render(request, 'blog/formulario_busqueda.html')


def resultados_busqueda(request):
    """
    Vista para mostrar los resultados de la búsqueda sobre el modelo 'Sostenibilidad'.
    Hace una búsqueda simple por el título del artículo.
    """
    query = request.GET.get('q', '')
    results = []
    if query:
        # Buscamos en el título de Sostenibilidad (icontains = búsqueda parcial/insensible a mayúsculas)
        results = Sostenibilidad.objects.filter(Q(titulo__icontains=query))
    return render(request, 'blog/resultados_busqueda.html', {
        'query': query,
        'results': results
    })


# ---------------------------------------------------------------------
# VISTA DE DETALLE PARA Sostenibilidad (mostrar y agregar comentarios)
# ---------------------------------------------------------------------
def detalle_sostenibilidad(request, pk):
    """
    Vista para mostrar el detalle de un artículo de Sostenibilidad (incluyendo sus comentarios).
    Permitir que cualquier usuario autenticado pueda comentar.
    """
    sostenibilidad_obj = get_object_or_404(Sostenibilidad, pk=pk)
    # Obtenemos todos los comentarios relacionados, ordenados por fecha descendente
    comentarios = Comentario.objects.filter(
        sostenibilidad=sostenibilidad_obj
    ).order_by('-fecha')

    if request.method == 'POST':
        # Para poder comentar se requiere estar autenticado
        if request.user.is_authenticated:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                nuevo_comentario = form.save(commit=False)
                nuevo_comentario.autor = request.user
                nuevo_comentario.sostenibilidad = sostenibilidad_obj
                nuevo_comentario.save()
                messages.success(request, "Comentario agregado con éxito.")
                return redirect('detalle_sostenibilidad', pk=pk)
        else:
            # Si no está autenticado, podrías redirigir al login
            return redirect('admin:login')  # Ajusta según tu URL de login
    else:
        form = ComentarioForm()

    context = {
        'sostenibilidad': sostenibilidad_obj,
        'comentarios': comentarios,
        'form': form,
    }
    return render(request, 'blog/detalle_sostenibilidad.html', context)


# ---------------------------------------------------------------------
# VISTA PARA REGISTRO DE USUARIOS (no superusuarios)
# ---------------------------------------------------------------------
def registrar_usuario(request):
    """
    Vista para registrar un nuevo usuario en el sistema.
    Utiliza el formulario de Django 'UserCreationForm'.
    El usuario resultante NO será superusuario ni staff por defecto.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()  # Crea el usuario en la base de datos
            # Iniciar sesión automáticamente (opcional)
            login(request, usuario)
            messages.success(request, "¡Tu cuenta ha sido creada exitosamente! Ahora puedes comentar.")
            return redirect('inicio')
    else:
        form = UserCreationForm()

    return render(request, 'blog/registro.html', {'form': form})

def user_login(request):
    """
    Vista para que un usuario normal (no staff) inicie sesión sin pasar por el admin.
    Autentica las credenciales y, si son válidas, inicia sesión.
    """
    if request.user.is_authenticated:
        # Si ya está logueado, lo redirigimos para evitar que vea de nuevo el formulario
        return redirect('inicio')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verifica credenciales
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Si las credenciales son correctas, inicia sesión
            login(request, user)
            messages.success(request, "¡Has iniciado sesión correctamente!")
            return redirect('inicio')  # Ajusta a la vista que desees
        else:
            # Si son inválidas, recarga el formulario con un mensaje de error
            messages.error(request, "Usuario o contraseña incorrectos.")
            return redirect('login')

    # Si es GET, mostrar el formulario de login
    return render(request, 'blog/login.html')


def user_logout(request):
    """
    Vista para cerrar sesión de un usuario.
    Termina la sesión y redirige a la página de inicio (o donde se prefiera).
    """
    logout(request)
    messages.info(request, "Te has desconectado correctamente.")
    return redirect('inicio')
