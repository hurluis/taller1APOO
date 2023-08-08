#Crear un programa que genere una matriz de números y la imprima en pantalla

def crearmatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for i in range(columnas):
            numero = int(input(f"Ingrese el número para la posición [{i}][{i}]: "))
            fila.append(numero)
        matriz.append(fila)
    return matriz

def mostrarmatriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    num_filas = int(input("Ingrese el número de filas de la matriz: "))
    num_columnas = int(input("Ingrese el número de columnas de la matriz: "))

    matriz_generada = crearmatriz(num_filas, num_columnas)

    print("La matriz generada es:")
    mostrarmatriz(matriz_generada)
main()