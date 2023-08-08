#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada

def encontrarnum(lista):
    maximo = lista[0]
    minimo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
        if i < minimo:
            minimo = i
    return maximo, minimo

def main():
        lista_numeros = input("Ingresa una lista de números separados por espacios: ").split()
        lista_numeros = [int(numero) for numero in lista_numeros]
        maximo, minimo = encontrarnum(lista_numeros)
        print("El número más grande es:", maximo)
        print("El número más pequeño es:", minimo)
main()