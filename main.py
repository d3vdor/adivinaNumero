'''
    Adivina el numero.
    1. Easy Level
    2. Medium Level
    3. Hard Level
'''


# Librerias
import os
import random
import time

# Funciones Globales
def header(mensaje):
    print(f"\n  {mensaje}\nAdivina el numero del 1 al 100\n")


def logica(n_random,n_user,n_lifes):
    while n_user != n_random:
        logica_juego(n_user,n_random)
        n_user = int(input("\nDigite otro numero: "))
        print(f"Vidas restantes: {n_lifes - 1}")
        n_lifes -= 1
        if n_lifes == 0:
            print(f"Perdiste!!\nEl numero era: {n_random}")
            back_menu()
    back_menu()
    return n_random,n_user


def logica_juego(a,b):
    if a < b:
        print("Digita un numero mas grande")
    else:
        print("Digita un numero mas chico")


def back_menu():
    numero = 5
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
            medium_level()
        elif opc == 3:
            hard_level()
        elif opc == 4:
            break
        else:
            print("Digita una opcion correcta")

# Funciones Logicas
def easy_level():
    header("Easy Level")
    random_number = random.randint(1,100)
    print("vidas totales: 20")
    user_number = int(input("Digite un numero: "))
    logica(random_number,user_number,20)


def medium_level():
    header("Medium Level")
    random_number = random.randint(1,100)
    print("vidas totales: 10")
    user_number = int(input("Digite un numero: "))
    logica(random_number,user_number,10)


def hard_level():
    header("Medium Level")
    random_number = random.randint(1,100)
    print("vidas totales: 5")
    user_number = int(input("Digite un numero: "))
    logica(random_number,user_number,5)

# Funcion Main
def main():
    print("\nBienvenio\n")
    menu()
    print("\nPrograma Finalizado")


if __name__ == '__main__':
    main()
