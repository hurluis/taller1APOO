#Escribir una función que calcule el factorial de un número dado

def factorial(numero):
    if numero < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

def main():
        numero = int(input("Ingresa un número entero no negativo: "))
        resultado_factorial = factorial(numero)
        print(f"El factorial de {numero} es: {resultado_factorial}")
main()