#Crear una función que convierta grados Fahrenheit a grados Celsius

def main():
    fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.2f} grados Fahrenheit son equivalentes a {celsius:.2f} grados Celsius.")
main()