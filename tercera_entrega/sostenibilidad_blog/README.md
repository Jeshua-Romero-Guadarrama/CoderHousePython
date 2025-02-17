# Proyecto Django: Blog de Sostenibilidad, Fintech e Inclusión

Este proyecto es un ejemplo de una aplicación web en Django que cumple con los siguientes requisitos:
- Utiliza el patrón MVT (Models, Views, Templates).
- Implementa herencia de plantillas HTML (`base.html` como plantilla base).
- Cuenta con 6 modelos (Sostenibilidad, Fintech, Inclusion, Autor, Categoría, Etiqueta).
- Ofrece un formulario para insertar datos para cada uno de los 6 modelos.
- Incluye un formulario para buscar en la base de datos (en este caso, buscamos por título en el modelo `Sostenibilidad`).

## Estructura del proyecto

```
sostenibilidad_blog/
├── manage.py
├── README.md
├── requirements.txt             (listar dependencias)
├── db.sqlite3                  (archivo de base de datos local, se crea tras migración)
│
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py     (archivos de migración generados por Django)
│   │
│   ├── fixtures/
│   │   └── datos_iniciales.json
│   │
│   └── templates/
│       └── blog/
│           ├── base.html
│           ├── inicio.html
│           ├── listar_sostenibilidad.html
│           ├── listar_fintech.html
│           ├── listar_inclusion.html
│           ├── crear_sostenibilidad.html
│           ├── crear_fintech.html
│           ├── crear_inclusion.html
│           ├── crear_autor.html
│           ├── crear_categoria.html
│           ├── crear_etiqueta.html
│           ├── detalle_sostenibilidad.html
│           ├── formulario_busqueda.html
│           ├── resultados_busqueda.html
│           └── registro.html
│
├── sostenibilidad_blog/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── static/
    ├── css/
    │   └── estilo.css          (si tuviera hojas de estilo propias)
    ├── js/
    │   └── funciones.js        (si tuviera scripts propios)
    └── img/
        └── logo.png            (si tuviera imágenes)
```

## Requisitos previos

- Python 3.x instalado.
- Pip (o pipenv, poetry, etc.) para instalar paquetes.
- Virtualenv.

## Instalación y ejecución local

1. **Clonar este repositorio**.

2. **Crear un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

3. **Instalar Django**:
   ```bash
   pip install django
   ```

4. **Migrar la base de datos**:
   ```bash
   cd sostenibilidad_blog
   python manage.py migrate
   ```
   Esto creará el archivo `db.sqlite3` con las tablas correspondientes.

5. **Crear un superusuario** (si deseas acceder al panel de administración de Django):
   ```bash
   python manage.py createsuperuser
   ```
   Seguir las instrucciones que aparecen en la consola para asignar usuario y contraseña.

4. **Cargar datos iniciales (fixtures)**  
   Asegurar que el archivo `datos_iniciales.json` esté dentro de `blog/fixtures/`, luego ejecuta:
   ```bash
   python manage.py makemigrations blog
   python manage.py migrate
   python manage.py loaddata blog/fixtures/datos_iniciales.json
   ```
   Esto insertará los registros de ejemplo en la base de datos (artículos, categorías, entre otros).

6. **Iniciar el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

7. **Abrir el navegador** y acceder a la URL:
   ```
   http://127.0.0.1:8000/
   ```
   Página de inicio del blog.

SuperUsuario ingresar con las siguientes credenciales en http://127.0.0.1:8000/admin/:
Usuario: Romero
COntraseña: Romero

UsuarioNormal ingresar con las siguientes credenciales en http://127.0.0.1:8000/login/:
Usuario: Pedro
COntraseña: Pedro1946@