# Crea una lista de numeros cuadrados de los números de la siguiente lista.
# Recuerda utilizar las funciones lambda y map() para calcular el cuadrado de cada elemento 
# de la lista.

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaCuadrado = list(map(lambda x: x ** 2, listaNumeros))

print(listaCuadrado)
