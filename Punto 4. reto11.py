filas = int(input("Insertar número de filas de la matriz: "))  # Declaración de variables
columnas = int(input("Insertar número de columnas de la matriz: "))
matriz = []
lista = []
n = int(input("Insertar fila de la que deseamos sumar sus elementos: "))
suma = 0

for i in range(filas):  # Ciclo for para crear la matriz
    fila = []
    for j in range(columnas):
        num = int(input("Insertar valor para la posición [{}, {}]: ".format(i, j)))
        fila.append(num)
    matriz.append(fila)

if n >= filas:
    print("La fila ingresada no es válida")
else:
    for elemento in matriz[n]:  # Ciclo for para recorrer los elementos de la fila n de la matriz ingresada
        suma += elemento

print("Matriz: " + str(matriz))
print("Suma de los elementos de la fila dada: " + str(suma))