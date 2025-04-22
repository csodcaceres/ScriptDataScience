# Has recibido una solicitud para generar números de token para acceder a la aplicacion 
# de una empresa.
# El token debe ser par y variar de 1000 a 9998.
# Escribir un codigo que solicite el nombre de la persona usuaria y muestre un mensaje
# junto a este token generado aleatoriamente.

import random

nombreUsuario = input('Ingrese nombre de usuario: ')
tokenGenerado = random.randrange(1000, 9998, 2)

print(f'Hola {nombreUsuario}, tu token de acceso es {tokenGenerado}, ¡Bienvedino!.')

