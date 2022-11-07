# Librerias
import os
import random
import time

# Funciones Globales
def header(mensaje,n_lifes): # Nivel del Juego
    print(f"\n  {mensaje}\nAdivina el numero del 1 al 100\n")
    print(f"Vidas Totales: {n_lifes}")


def entrada(vidas): # Entrada de Numeros
    random_number = random.randint(1,100)
    user_number = int(input("Digite un numero: "))
    salida(random_number,user_number,vidas)


def salida(n_random,n_user,n_lifes): # Bucle de comparacion
    while n_user != n_random:
        if n_user < n_random:
            print("Digita un numero mas grande")
        else:
            print("Digita un numero mas chico")
        n_user = int(input("\nDigite otro numero: "))
        print(f"Vidas restantes: {n_lifes - 1}")
        n_lifes -= 1
        if n_lifes == 0:
            print(f"Perdiste!!\nEl numero era: {n_random}")
            back_menu()
    print(f"\nGanaste!!\nVidas restantes: {n_lifes}\n")
    back_menu()
    return n_random,n_user


def back_menu(): # Cuenta regresiva
    time.sleep(1)
    numero = 5
    print("Regresando al menu en")
    for i in range(numero):
        print(numero)
        time.sleep(1)
        numero -= 1
        if numero == 0:
            os.system("cls")
            menu()


def menu(): # Menu
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
def easy_level(): # Nivel Facil
    header("Easy Level",20)
    entrada(20) # Cantidad de vidas del nivel


def medium_level(): # Nivel medio
    header("Medium Level",10)
    entrada(10)


def hard_level(): # Nivel dificil
    header("Hard Level",5)
    entrada(5)

# Funcion Main
def main():
    print("\nBienvenio\n")
    menu()
    print("\nPrograma Finalizado")


if __name__ == '__main__':
    main()