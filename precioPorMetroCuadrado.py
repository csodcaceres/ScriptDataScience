# Tienda que vende césped para jardines. 
# Esta tienda trabaja con jardines circulares y el precio del metro cuadrado de césped es de $25,00.
# Pide al usuario el radio del área circular y devuelve el valor en pesos de cuánto tendrá que pagar.

import math

precioMetroCuadrado = 25.00
radio = float(input('Ingrese el radio del area circular en metros: '))
area = math.pi * math.pow(radio, 2)
costoTotal = precioMetroCuadrado * area

print(f'El costo total es: $ {round(costoTotal)}')
