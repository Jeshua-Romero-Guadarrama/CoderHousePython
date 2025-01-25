'''
Módulo con funciones auxiliares para la gestión de clientes en la página de compras.
'''

def calcular_descuento(puntos):
    '''
    Calcula un porcentaje de descuento basado en la cantidad de puntos.
    
    Parámetros:
        puntos (int): Puntos acumulados de un cliente.
    
    Retorna:
        float: Porcentaje de descuento (0.05 para 5%).
    '''
    if puntos < 50:
        return 0.0
    elif 50   <= puntos < 200:
        return 0.05
    elif 200  <= puntos < 500:
        return 0.1
    else:
        return 0.2

def aplicar_descuento(precio_original, descuento):
    '''
    Aplica un porcentaje de descuento a un precio original.
    
    Parámetros:
        precio_original (float): Precio sin descuento.
        descuento       (float): Porcentaje en decimal (0.1 = 10%)
    
    Retorna:
        float: Precio final con descuento.
    '''
    return precio_original * (1 - descuento)

def info_cliente(cliente):
    '''
    Muestra información adicional del objeto "Cliente".
    
    Parámetros:
        cliente (Cliente): Objeto de la clase Cliente.
    '''
    desc = calcular_descuento(cliente.puntos)
    print("================ Información Sobre Cliente ================")
    print(f"Nombre :          {cliente.nombre}")
    print(f"Email  :          {cliente.email}")
    print(f"Edad   :          {cliente.edad}")
    print(f"Nivel  :          {cliente.nivel}")
    print(f"Puntos :          {cliente.puntos}")
    print(f"Intereses:        {cliente.intereses}")
    print(f"Descuento actual: {desc*100}%")
    print("============================================================")