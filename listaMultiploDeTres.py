# Función que lee lista de numeros enteros y devuelva una nueva lista con los múltiplos de 3

def multiplosDeTres(lista):
    return [num for num in lista if num % 3 == 0]

# Lista
listaDeNumeros = [97, 80, 76, 54, 89, 23, 31, 7, 32, 15, 72, 18]

multiplos_tres = multiplosDeTres(listaDeNumeros)
print(multiplos_tres)