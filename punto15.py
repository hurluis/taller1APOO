#Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no

def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]

def main():
    cadena_ingresada = input("Ingresa una cadena de texto: ")

    if es_palindromo(cadena_ingresada):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")
main()