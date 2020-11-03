# -*- coding: utf-8 -*-


from assets import assets
from classes.classes import Player, Dealer
import deck, results

from functools import partial
from random import randint


# Settings:
deck_copies = 1
human_player = True
human_player_name = "Miey"


def game():
    """Main function, generates a game of blackjack."""

    """1st stage, setting starting conditions"""
    dealer = Dealer("DEALER")
    if human_player:
        player_1 = Player(human_player_name)
    else:
        player_1 = Player(assets.player_names[randint(0, len(assets.player_names) - 1)])

    print("_" * 40)
    deck = deck.new_deck(deck_copies)
    dealer.draw_card(deck, 2)
    dealer.count_points()
    dealer.display_hidden_hand()
    player_1.draw_card(deck, 2)
    player_1.count_points()


    """2nd stage, players taking turns"""
    print("_" * 40)

    player_1.display_hand()
    if human_player:
        while not player_1.finished_turn:
            entry = input("Choose your action:  Hit[1]  Stand[2]  Double[3]  Split[4]  Surrender[5]  Quit[Q]: ")
            entry = entry.upper()
            moves = {
                "1": partial(player_1.hit, deck),
                "2": partial(player_1.stand),
                "3": partial(player_1.double, deck),
                "4": partial(player_1.split, deck),
                "5": partial(player_1.surrender, deck),
                "Q": exit  #TODO: Sort this out
            }
            moves[entry]()  # TODO: Sort KeyError (try/except or if/else statement)

    else:
        while player_1.total < 17:
            player_1.hit(deck)

    print("_" * 40)
    while dealer.total < 17:
        dealer.hit(deck)


    """3rd stage, calculating and displaying results"""
    print("\n" + "_" * 25 + "RESULTS:" + "_" * 25)
    player_1.display_hand()
    results.winner(player_1, dealer)

    dealer.display_hand()


# game()
