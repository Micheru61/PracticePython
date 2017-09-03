#!usr/bin/python3.4

import random


nb_tentatives = 0
range_nombre = range(1,10)

def choix_player(nombre):
    global nb_tentatives

    try:
        nb_player = int(input("Please, guess the number (between 1 and 9 both included)\n:"))
    except TypeError:
        print("Please enter a valid whole number")
        return choix_player(nombre)

    if nb_player < 0 or nb_player > 9:
        print("Please enter a whole number between 1 and 9 both included")
        return choix_player(nombre)
    else:
        nb_tentatives += 1
        return check_number(nb_player, nombre)

def check_number(nb_player, nombre):
    if nb_player == nombre:
        print("Congratulations, you found the right number in {} attempts".format(nb_tentatives))
    elif nb_player < nombre:
        print("Too low")
    else:
        print("Too high")
    return nb_player

continuer = 'y'

while continuer != "exit":
    nb_tentatives = 0
    nombre = random.randint(1,10)
    nb_choisi = 0
    print("\n====================================")
    while nb_choisi != nombre:
        nb_choisi = choix_player(nombre)

    continuer = input("\nAnother turn ? (type 'exit' to quit)\n:")
    continuer = continuer.lower()