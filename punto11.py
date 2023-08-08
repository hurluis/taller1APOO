#Crear un programa que genere una lista de números pares entre 1 y 100

def generar_lista_numeros_pares():
    lista_pares = []
    for i in range(2, 101, 2):
        lista_pares.append(i)
    return lista_pares

def main():
    lista_pares = generar_lista_numeros_pares()
    print("Lista de números pares entre 1 y 100:")
    print(lista_pares)
main()