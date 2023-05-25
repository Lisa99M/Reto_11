import numpy

filas = int(input("Insertar número de filas de la matriz 1: "))  # Declaración de variables
columnas = int(input("Insertar número de columnas de la matriz 1: "))
matriz = []

for i in range(filas):  # Ciclo for para crear la primera matriz
    for j in range(columnas):
        num = int(input("Insertar valores para la matriz 1: "))
        lista.append(num)
    matriz.append(lista)
    lista = []

Nueva_Matriz = numpy.zeros((columnas, filas))  # Añadir numpy.zeros para que la nueva matriz con los resultados de la operación sea inicializada con ceros.
for i in range(columnas):
    for j in range(filas):
        lista.append(matriz[j][i])
    Nueva_Matriz.append(lista)
    lista = []

print("La matriz transpuesta de la matriz ingresadas es: "  + str(Nueva_Matriz))