# Crear un programa que calcule la suma de los números en una lista dada.

def suma(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

def main():
    lista_numeros = input("Ingresa una lista de números separados por espacios: ").split()
    lista_numeros = [int(i) for i in lista_numeros]
    resultado_suma = suma(lista_numeros)
    print("La suma de los números en la lista es:", resultado_suma)
main()    