# Script que solicita al usuario ingresar dos numeros enteros
# y calcular la potencia del primer numero elevado al segundo
import math

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

resultado = math.pow(num1, num2)
print(format(resultado, '.2f'))
print(resultado)

