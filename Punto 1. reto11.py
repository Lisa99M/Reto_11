import numpy

filas1 = int(input("Insertar número de filas de la matriz 1: "))  # Declaración de variables
filas2 = int(input("Insertar número de filas de la matriz 2: "))
columnas1 = int(input("Insertar número de columnas de la matriz 1: "))
columnas2 = int(input("Insertar número de columnas de la matriz 2: "))

if filas1 != columnas2:
    print("El número de filas de la primera matriz debe ser igual al número de columnas de la segunda matriz para poder multiplicarlas")
else:
    matriz_1 = []
    matriz_2 = []
    lista = []

    for i in range(filas1):  # Ciclo for para crear la primera matriz
        for j in range(columnas1):
            num = int(input("Insertar valores para la matriz 1: "))
            lista.append(num)
        matriz_1.append(lista)
        lista = []

    for i in range(filas2):  # Ciclo for para crear la segunda matriz
        for j in range(columnas2):
            num = int(input("Insertar valores para la matriz 2: "))
            lista.append(num)
        matriz_2.append(lista)
        lista = []

    Nueva_Matriz = numpy.zeros((filas1, columnas1))  # Añadir numpy.zeros para que la nueva matriz con los resultados de la operación sea inicializada con ceros.

   
    for i in range(filas1):
        for j in range(columnas1):
            Nueva_Matriz[i][j] = matriz_1[i][j] * matriz_2[i][j]
   

    print("El resultado de la multiplicación de las dos matrices ingresadas es: "  + str(Nueva_Matriz))