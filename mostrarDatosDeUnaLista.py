# Escribe un código que lee la lista siguiente y realiza:
#     - Mostrar el tamaño de la lista. 
#     - Mostrar el maximo y minimo.
#     - Calcular la suma de los valores de la lista.

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

# - Tamaño de la lista
tamanio = len(lista)

# - Numero minimo y maximo de la lista
mayor = max(lista)
menor = min(lista)

# - Calcular la suma de los valores de la lista
sumaLista = sum(lista)

print(f'La lista tiene {tamanio} numeros, donde el mayor es {mayor} y el menor es {menor}. La suma de los valores es {sumaLista}')
