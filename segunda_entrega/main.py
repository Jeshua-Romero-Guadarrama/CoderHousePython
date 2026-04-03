'''
Archivo principal:
- Importar la clase cliente y métodos de segundo_modulo.
- Se crean instancias de cliente, se realizan operaciones y se muestran resultados.
'''

from paquete.primer_modulo import Cliente
from paquete.segundo_modulo import (
    calcular_descuento,
    aplicar_descuento,
    info_cliente
)

def main():
    '''
    Función principal para demostrar la funcionalidad de la clase Cliente y los métodos auxiliares de segundo_modulo.
    '''
    # Se crea un cliente con 4 atributos: nombre, email, edad, intereses
    primer_cliente = Cliente("Juan", "profe@coder.com", 30, ["tecnología", "moda", "farmacia"])
    print(primer_cliente)  # Esto ejecuta el __str__ de Cliente
    
    # Se agrega un interés
    primer_cliente.agregar_interes("deportes")
    
    # Se realiza una compra
    primer_cliente.comprar("Laptop", "Walmart", valor = 500)
    primer_cliente.comprar("Camiseta", "Nike Store", valor = 45)
    
    # Se muestra el historial
    primer_cliente.mostrar_historial()
    
    # Se verifica el descuento basado en puntos
    descuento_actual = calcular_descuento(primer_cliente.puntos)
    print(f"Descuento actual para {primer_cliente.nombre}: {descuento_actual*100}%")
    
    # Ejemplo de aplicar descuento a un futuro precio
    precio_inicial = 100
    precio_final = aplicar_descuento(precio_inicial, descuento_actual)
    print(f"Aplicando descuento a un producto de ${precio_inicial} => ${precio_final}")
    
    # Se cambia de nivel
    primer_cliente.cambiar_nivel("Gold")
    print(primer_cliente)
    
    # Se usa la función info_cliente para un resumen
    info_cliente(primer_cliente)
    
    # Se crea un segundo cliente, con un nivel distinto y sin intereses
    segundo_cliente = Cliente("María", "maria@shop.com", 40, nivel = "Platinum")
    print(segundo_cliente)
    segundo_cliente.saludar()  # Método heredado de Persona

if __name__ == "__main__":
    main()