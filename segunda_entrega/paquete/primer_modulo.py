'''
Módulo que define clases relacionadas con clientes en una página de compras.
Incluye ejemplo de herencia (Persona -> Cliente).
'''

class Persona:
    '''
    Clase base que modela a una persona genérica.
    
    Atributos:
        nombre (str): Nombre de la persona.
        email  (str): Email de la persona.
        edad   (int): Edad de la persona.
    '''
    
    def __init__(self, nombre, email, edad):
        '''
        Constructor de la clase Persona.
        
        Parámetros:
            nombre (str): Nombre de la persona.
            email  (str): Email de la persona.
            edad   (int): Edad de la persona.
        '''
        self.nombre = nombre
        self.email  = email
        self.edad   = edad
    
    def __str__(self):
        '''
        Representación en cadena (string) de la persona.
        '''
        return f"{self.nombre} ({self.email}), {self.edad} años"
    
    def saludar(self):
        '''
        Imprime un saludo genérico.
        '''
        print(f"Hola, soy {self.nombre}, un gusto conocerte.")

class Cliente(Persona):
    '''
    Clase que modela a un Cliente de una página de compras, heredando de Persona e incorporando atributos adicionales.
    
    Atributos heredados de Persona:
        nombre (str)
        email  (str)
        edad   (int)
    
    Atributos adicionales:
        intereses         (list): Lista de categorías de interés del cliente.
        puntos            (int):  Puntos acumulados en el sistema de fidelidad.
        historial_compras (list): Historial de compras del cliente.
        nivel             (str):  Nivel de cliente (por ejemplo, 'Plata', 'Oro', 'Platino').
    '''
    NIVELES_PERMITIDOS = ["Plata", "Oro", "Platino"]
    
    def __init__(self, nombre, email, edad, intereses = None, nivel = "Plata"):
        '''
        Constructor de Cliente, que llama al constructor de Persona y define atributos adicionales.
        
        Parámetros:
            nombre    (str):            Nombre del cliente.
            email     (str):            Email del cliente.
            edad      (int):            Edad del cliente.
            intereses (list, opcional): Categorías de interés.
            nivel     (str, opcional):  Nivel de cliente (default 'Plata').
        '''
        # Invoca al init de Persona
        super().__init__(nombre, email, edad)
        self.intereses         = intereses if intereses is not None else []
        self.puntos            = 0
        self.historial_compras = []
        # Verifica si el nivel ingresado es válido
        if nivel not in self.NIVELES_PERMITIDOS:
            # Por defecto en 'Plata'
            nivel  = "Plata"
        self.nivel = nivel
    
    def __str__(self):
        '''
        Sobrescribimos la representación en cadena para Cliente.
        '''
        return (f"Cliente: {self.nombre}, Email: {self.email}, "
                f"Edad: {self.edad}, Nivel: {self.nivel}, "
                f"Puntos: {self.puntos}")
    
    def agregar_interes(self, interes):
        '''
        Agrega un nuevo interés al cliente si no está repetido.
        
        Parámetros:
            interes (str): Nombre de la categoría de interés (p. ej. 'tecnología').
        '''
        if interes not in self.intereses:
            self.intereses.append(interes)
            print(f"Interés '{interes}' agregado a {self.nombre}.")
        else:
            print(f"El cliente {self.nombre} ya tiene el interés '{interes}'.")
    
    def comprar(self, producto, tienda, valor = 0):
        '''
        Simula la compra de un producto y actualiza historial de compras.
        
        Parámetros:
            producto (str):                 Nombre del producto.
            tienda   (str):                 Nombre de la tienda o proveedor.
            valor    (float/int, opcional): Precio del producto.
        '''
        compra = {
            "producto": producto,
            "tienda":   tienda,
            "valor":    valor
        }
        self.historial_compras.append(compra)
        # Sumar puntos (1 punto por cada 10 de 'valor')
        puntos_ganados =  int(valor // 10)
        self.puntos    += puntos_ganados
        print(f"{self.nombre} ha comprado '{producto}' en '{tienda}'. "
              f"Valor: {valor} MXN. Puntos ganados: {puntos_ganados}.")
    
    def mostrar_historial(self):
        '''
        Muestra todas las compras realizadas por el cliente.
        '''
        if not self.historial_compras:
            print(f"{self.nombre} aún no ha realizado ninguna compra.")
        else:
            print(f"Historial de compras de {self.nombre}:")
            for idx, compra in enumerate(self.historial_compras, start=1):
                producto = compra["producto"]
                tienda   = compra["tienda"]
                valor    = compra["valor"]
                print(f"  {idx}. {producto} - {tienda} - ${valor}")

    def cambiar_nivel(self, nuevo_nivel):
        '''
        Cambia el nivel del cliente (si es válido).
        
        Parámetros:
            nuevo_nivel (str): El nuevo nivel deseado ('Plata', 'Oro', 'Platino').
        '''
        if nuevo_nivel in self.NIVELES_PERMITIDOS:
            self.nivel = nuevo_nivel
            print(f"Nivel del cliente {self.nombre} actualizado a '{nuevo_nivel}'.")
        else:
            print(f"Nivel inválido. Opciones: {self.NIVELES_PERMITIDOS}")