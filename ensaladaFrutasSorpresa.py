# Para diversificar y atraer a nuevos clientes, un restore creo un item misterioso en su menu
# llamado 'ensalada de frutas sorpresa'.
# En este ítem, se eligen aleatoriamente 3 frutas de una lista de 12 para componer la ensalada 
# de frutas del cliente. 
# Crea el código que realice esta selección aleatoria según la lista dada.

import random

frustas = ['Manzana', 'Banana', 'Uva', 'Pera', 'Mango', 'Coco', 'Sandia'
           'Fresa', 'Naranja', 'Maracuya', 'Kiwi', 'Cereza']

seleccecionDeFruta = random.sample(frustas, 3)
print(f'Ensalada de fruta sorpresa: {seleccecionDeFruta}')
