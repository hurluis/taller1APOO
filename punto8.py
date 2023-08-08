#Crear una función que invierta el orden de los elementos en una lista dada.

def invertir(lista):
    return lista[::-1]

def main():
        lista_original = input("Ingresa una lista de elementos separados por espacios: ").split()
        lista_invertida = invertir(lista_original)
        print("Lista original:", lista_original)
        print("Lista invertida:", lista_invertida)
main()