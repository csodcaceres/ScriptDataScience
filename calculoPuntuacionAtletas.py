# Analizar las notas recibidas por los skaters en algunas competiciones a lo largo del año, 
# necesitas crear un código que calcule la puntuación de los atletas. 
# Para ello, tu código debe recibir 5 notas ingresadas por los jueces

notas = [float(input(f'Ingrese la nota {i + 1}: ')) for i in range(5)]
notas.sort()
media = sum(notas[1:4]) / 3

print(f'Nota media: {media:.2f}')
