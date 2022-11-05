# Librerias
import os
import random
import time

# Funciones Globales
def back_menu():
    pass


def menu():
    while True:
        print("""
        --- Guess the number ---
        1. Easy
        2. Medium
        3. Hard
        4. Exit
        """)
        opc = int(input("Selec an option: "))

        if opc == 1:
            easy_level()
        elif opc == 2:
            medium_level
        elif opc == 3:
            hard_level
        elif opc == 4:
            break
        else:
            print("Select a correct option2")

# Funciones Logicas
def easy_level():
    pass


def medium_level():
    pass


def hard_level():
    pass

# Funcion Main
def main():
    menu()
    print("Programa Finalizado")


if __name__ == '__main__':
    main()