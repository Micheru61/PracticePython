#!usr/bin/python3.4

"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""

hands = ['Rock', 'Paper', 'Scissors']

beat_hands = {
    'Rock': 'Scissors',
    'Scissors': 'Paper',
    'Paper': 'Rock',
}

def enter_name(player):
    name = input("{}, please enter your name\n: ".format(player))
    name = name.capitalize()
    if not name.isalpha():
        print("Name is not valid !")
        return enter_name()
    else:
        return name

def choisir_tour_a_jouer(nom):
    jeu = input("{}, please enter your move ('Rock', 'Paper' or 'Scissors')\n: ".format(nom))
    jeu = jeu.capitalize()
    if jeu not in hands:
        print("Please, choose a valid move !")
        return choisir_tour_a_jouer(nom)
    else:
        return jeu

def check_winner(player1_move, player2_move):
    global score_player1
    global score_player2

    if player1_move == player2_move:
        print("Draw")
    else:
        if beat_hands[player1_move] == player2_move:
            print("{} beats {}".format(player1_move, player2_move))
            print("{} win\n".format(player1))
            score_player1 += 1
        else:
            print("{} beats {}".format(player2_move, player1_move))
            print("{} win\n".format(player2))
            score_player2 += 1

player1 = enter_name("player1")
player2 = enter_name("player2")

score_player1, score_player2= 0, 0

continuer = 'y'
reponse = ['y','n','yes','no']

def continuer_partie():
    question = input("Another turn ? (yes/no)\n:")
    question = question.lower()
    global continuer

    if question not in reponse:
        print("Please, answer by 'yes' or 'no'")
        return continuer_partie()
    elif question == 'n':
        print("End of game, {}: {} - {}: {}".format(player1, score_player1, player2, score_player2))
        continuer = 'n'

def print_leader():
    if score_player1 == score_player2:
        print("The 2 players are ex-aequo, {} points each".format(score_player1))
    elif score_player1 > score_player2:
        print("{} leads by {} - {}".format(player1, score_player1, score_player2))
    else:
        print("{} leads by {} - {}".format(player2, score_player2, score_player1))

while continuer == 'y':
    print("=======================================================")
    player1_move = choisir_tour_a_jouer(player1)
    player2_move = choisir_tour_a_jouer(player2)

    print("{} plays {}".format(player1, player1_move))
    print("{} plays {}".format(player2, player2_move))

    check_winner(player1_move, player2_move)

    print_leader()

    continuer_partie()