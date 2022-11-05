# Librerias
import os
import random
import time

# Funciones Globales
def logica_juego(a,b):
    if a < b:
        print("Digita un numero mas grande")
    else:
        print("Digita un numero mas chico")


def back_menu():
    numero = 3
    print("Regresando al menu en")
    for i in range(numero):
        print(numero)
        time.sleep(1)
        numero -= 1
        if numero == 0:
            os.system("cls")
            menu()


def menu():
    while True:
        print("""
        --- Menu ---
        1. Easy Level
        2. Medium Level
        3. Hard Level
        4. Exit 
        """)
        opc = int(input("Selecciona una opcion: "))

        if opc == 1:
            easy_level()
        elif opc == 2:
            medium_level
        elif opc == 3:
            hard_level
        elif opc == 4:
            break
        else:
            print("Digita una opcion correcta")

# Funciones Logicas
def easy_level():
    print("Adivina el numero del 1 al 100\n")
    random_number = random.randint(1,100)
    user_number = int(input("Digite un numero: "))
    vidas = 0
    while user_number != random_number:
        logica_juego(user_number,random_number)
        user_number = int(input("Digita otro numero: "))
        vidas += 1
    print("Adivinaste el numero!!")
    print(f"Numero de intentos: {vidas}")
    menu()


def medium_level():
    pass


def hard_level():
    pass

# Funcion Main
def main():
    menu()
    print("\nPrograma Finalizado")


if __name__ == '__main__':
    main()