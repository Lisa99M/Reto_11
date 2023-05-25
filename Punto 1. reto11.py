import numpy

n = int(input("Insertar tamaño de la matriz 1: "))  # Declaración de variables
nn = int(input("Insertar tamaño de la matriz 2: "))

operador = input("Insertar operación (suma o resta): ") # El usuario debe seleccionar qué operación desea realizar con las matrices

if n != nn:
    print("Las matrices deben ser de igual tamaño para efectuar la operación")
else:
    matriz_1 = []
    matriz_2 = []
    lista = []

    for i in range(n):  # Ciclo for para crear la primera matriz
        for j in range(n):
            num = int(input("Insertar valores para la matriz 1: "))
            lista.append(num)
        matriz_1.append(lista)
        lista = []

    for i in range(nn):  # Ciclo for para crear la segunda matriz
        for j in range(nn):
            num = int(input("Insertar valores para la matriz 2: "))
            lista.append(num)
        matriz_2.append(lista)
        lista = []

    Nueva_Matriz = numpy.zeros((n, n))  # Añadir numpy.zeros para que la nueva matriz con los resultados de la operación sea inicializada con ceros.

    if operador == "suma":
        for i in range(n):
            for j in range(n):
                Nueva_Matriz[i][j] = matriz_1[i][j] + matriz_2[i][j]
    elif operador == "resta":
        for i in range(n):
            for j in range(n):
                Nueva_Matriz[i][j] = matriz_1[i][j] - matriz_2[i][j]
    else:
        print("Operador inválido. Debe ser 'suma' o 'resta'")

    print("El resultado de la suma de las dos matrices ingresadas es: "  + str(Nueva_Matriz))