# -*- coding: utf-8 -*-

# Blackjack

import main_game


print "Welcome to the game of blackjack!"


while True:  # Always rebound to the menu
    print ""
    entry = raw_input("New game[1]  Instructions[2]  Quit[Q]: ")

    if entry == "1":
        main_game.game()
    elif entry == "2":
        instructions = open("instructions.txt", "r")
        print instructions.read()
    elif entry.upper() == "Q":
        print "Thank you for playing!"
        quit()
    else:
        print "Sorry, you have to specify what do you want to do."
