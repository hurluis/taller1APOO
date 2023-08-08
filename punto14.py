#Escribir una función que calcule la media aritmética de una lista de números

def calcular_media_aritmetica(lista):
    suma = sum(lista)
    media = suma / len(lista)
    return media

def main():
        lista_numeros = input("Ingresa una lista de números separados por espacios: ").split()
        lista_numeros = [float(numero) for numero in lista_numeros]
        media_aritmetica = calcular_media_aritmetica(lista_numeros)
        print("La media aritmética es:", media_aritmetica)
main()