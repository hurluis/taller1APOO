#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.

from random import randint

def main():
    vecnum=[randint(1,10) for i in range(0,10)]
    print(vecnum)
main()