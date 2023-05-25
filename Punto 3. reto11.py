import numpy

filas = int(input("Insertar número de filas de la matriz: "))  # Declaración de variables
columnas = int(input("Insertar número de columnas de la matriz: "))
matriz = []
lista = []

for i in range(filas):  # Ciclo for para crear la matriz
    for j in range(columnas):
        num = int(input("Insertar valores para la matriz: "))
        lista.append(num)
    matriz.append(lista)
    lista = []

Nueva_Matriz = numpy.zeros((columnas, filas))  # Añadir numpy.zeros para que la nueva matriz sea inicializada con ceros.

for i in range(columnas):  # Ciclo for donde invertiremos el número de filas y columnas para así crear la matriz transpuesta
    for j in range(filas):
        lista.append(matriz[j][i])
    Nueva_Matriz[i] = lista
    lista = []

print("Matriz original:" + str(matriz)) 
print("Matriz transpuesta:" + str(Nueva_Matriz))
