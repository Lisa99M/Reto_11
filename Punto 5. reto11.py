filas = int(input("Insertar número de filas de la matriz: "))  # Declaración de variables
columnas = int(input("Insertar número de columnas de la matriz: "))
matriz = []
n = int(input("Insertar columna de la que deseamos sumar sus elementos: "))
suma = 0

for i in range(filas):  # Ciclo for para crear la matriz
    fila = []
    for j in range(columnas):
        num = int(input("Insertar valor para la posición [{}, {}]: ".format(i, j)))
        fila.append(num)
    matriz.append(fila)

if n >= columnas:
    print("La columna ingresada no es válida")
else:
    for i in range(filas):  # Ciclo for para recorrer los elementos de la columna n de la matriz ingresada
        suma += matriz[i][n]

print("Matriz: " + str(matriz))
print("Suma de los elementos de la columna dada: " + str(suma))