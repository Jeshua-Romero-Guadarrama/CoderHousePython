# ModeloClientesJeshuaRomeroGuadarrama

Este proyecto ofrece un **modelo de clientes** para una página de compras en línea, implementado en Python mediante un enfoque de **Programación Orientada a Objetos**. Permite crear y gestionar distintos perfiles de clientes, con atributos y métodos que cubren escenarios habituales (compras, historial, puntos de fidelidad, entre otros).

# Características principales

- **Clases con herencia**: Incluye una clase base (`Persona`) y la clase derivada (`Cliente`).
- **Atributos avanzados**: Cada cliente puede tener múltiples intereses, un nivel (Plata, Oro, Platino), un historial de compras y puntos acumulados.
- **Métodos de utilidad**: Para agregar intereses, registrar compras, cambiar de nivel, saludar, entre otros.
- **Módulos auxiliares**: Funciones que calculan descuentos, aplican rebajas y muestran información detallada del cliente.
- **Fácil de extender**: El diseño modular permite agregar más métodos o ajustes según necesidades específicas.

# Requerimientos

- **Python 3.6** o superior.
- Se recomienda crear y activar un entorno virtual para aislar dependencias.

# Estructura del proyecto

```text
segunda_entrega/
├── ModeloClientesJeshuaRomeroGuadarrama.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
├── dist
│   └── ModeloClientesJeshuaRomeroGuadarrama-0.1.0.tar.gz
├── paquete
│   ├── __init__.py
│   ├── primer_modulo.py
│   └── segundo_modulo.py
├── README.md
├── main.py
└── setup.py
```

- **`main.py`**: Script principal de ejemplo para usar las clases y métodos del paquete.
- **`paquete`**: Carpeta que contiene los módulos:
  - **`primer_modulo.py`**: Define las clases `Persona` y `Cliente`.
  - **`segundo_modulo.py`**: Incluye funciones auxiliares para cálculo de descuentos, etc.
- **`setup.py`**: Archivo de instalación para generar el paquete.
- **`README.md`**: Documento explicativo (este archivo).

# Generar el paquete distribuible

Para crear la **distribución** del proyecto y permitir que se instale en otras computadoras:

1. Abrir una terminal en la carpeta raíz del proyecto (donde se encuentra `setup.py`).
2. Ejecutar el siguiente comando:

   ```bash
   python setup.py sdist
   ```

   Lo anterior generará una carpeta `dist/` que contendrá un archivo comprimido (en formato `.tar.gz`).  
   En este caso es `ModeloClientesJeshuaRomeroGuadarrama-0.1.0.tar.gz`

# Instalar en otra computadora

Para instalar el proyecto en otro entorno o máquina:

1. Copiar el archivo comprimido (`ModeloClientesJeshuaRomeroGuadarrama-0.1.0.tar.gz`) a la computadora de destino.
2. En esa computadora, abrir una terminal y ejecutar:

   ```bash
   pip install ModeloClientesJeshuaRomeroGuadarrama-0.1.0.tar.gz
   ```

   Con ello, se instalará el paquete en el entorno de Python actual.

# Uso del paquete

Una vez instalado, se pueden **importar** las clases y funciones en cualquier script Python:

**Ejemplo rápido:**

```python
from paquete.primer_modulo import Cliente

clientePrueba = Cliente("Test", "test@example.com", 25, ["deportes", "moda"])
clientePrueba.comprar("Libro de Python", "Librería Online", 120)
print(clientePrueba)
```

Si se prefiere **ejecutar directamente el archivo `main.py`**, se puede:

1. Copiar todo el proyecto a la computadora de destino (o clonar el repositorio).
2. Entrar a la carpeta y asegurar que el paquete esté instalado (por ejemplo, con `pip install .`).
3. Ejecutar:

   ```bash
   python main.py
   ```

Así podrá ver en acción la creación de varios clientes, compras, historial, cambios de nivel y más.

**Ejemplo rápido:**

```python
from paquete.primer_modulo import Cliente
from paquete.segundo_modulo import info_cliente

# Crear cliente e interactuar
c = Cliente("Ana", "ana@example.com", 28, nivel="Gold")
c.comprar("Smartphone", "TechStore", 350)
info_cliente(c)
```

Este código demostrará el funcionamiento básico de la clase `Cliente` y de las funciones auxiliares para presentar el estado del cliente.

# Notas finales

- El proyecto se basa completamente en la **Programación Orientada a Objetos**, con uso de **herencia**, **métodos especializados** y **docstrings** para mantener un código claro y reutilizable.

¡Gracias por usar **ModeloClientesJeshuaRomeroGuadarrama**!