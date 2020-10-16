# -*- coding: utf-8 -*-


import assets
from classes import Player, Dealer
from functools import partial 
from random import randint


# Settings:
deck_copies = 1
human_player = True
human_player_name = "Miey"


def new_deck(deck_copies=1):
    """Returns a new, sorted deck [type = list] consisting of n-copies of 52-card deck"""
    deck = []

    for deck_copy in range(deck_copies):
        for i in range(0, 52):
            rank_id = i // 4
            suit_id = i % 4
            deck.append((assets.rank[rank_id], assets.suit[suit_id]))

    return deck


def winner(player, dealer):
    """Prints in a console result of a game and returns winner (type = str)"""
    if player.total > 21:
        print "Player busted. Dealer won."
        return "dealer"
    elif dealer.total > 21:
        print "Dealer busted. Player won."
        return "player"

    elif dealer.total == 21 and len(dealer.hand) == 2:
        print "Blackjack. Dealer won."
        return "dealer"
    elif player.total == 21 and len(player.hand) == 2:
        print "Blackjack. Player won."
        return "player"

    elif dealer.total >= player.total:
        print "Player didn't get more points than dealer. Dealer won."
        return "dealer"
    elif dealer.total < player.total:
        print "Player got more points than dealer. Player won."
        return "player"


def game():
    """Main function, generates a game of blackjack."""

    """1st stage, setting starting conditions"""
    dealer = Dealer("DEALER")
    if human_player:
        player_1 = Player(human_player_name)
    else:
        player_1 = Player(assets.player_names[randint(0, len(assets.player_names) - 1)])

    print "_" * 40
    deck = new_deck(deck_copies)
    dealer.draw_card(deck, 2)
    dealer.count_points()
    dealer.display_hidden_hand()
    player_1.draw_card(deck, 2)
    player_1.count_points()


    """2nd stage, players taking turns"""
    print "_" * 40

    player_1.display_hand()
    if human_player:
        while not player_1.finished_turn:
            entry = raw_input("Choose your action:  Hit[1]  Stand[2]  Double[3]  Split[4]  Surrender[5]  Quit[Q]: ")
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

    print "_" * 40
    while dealer.total < 17:
        dealer.hit(deck)


    """3rd stage, calculating and displaying results"""
    print "\n" + "_" * 25 + "RESULTS:" + "_" * 25
    player_1.display_hand()
    winner(player_1, dealer)

    dealer.display_hand()


# game()
