#Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división

def main():
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))

        suma = numero1 + numero2
        resta = numero1 - numero2
        multiplicacion = numero1 * numero2

        if numero2 != 0:
            division = numero1 / numero2
        else:
            division = "No se puede dividir entre cero."

        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        print(f"División: {division}")
main()