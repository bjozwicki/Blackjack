# -*- coding: utf-8 -*-

from assets import assets
from random import randint


class Participant(object):

    def __init__(self, name):
        self.name = name
        self.hand   = []    # List of drawn cards
        self.points = []    # List of respective cards' values
        self.total = 0
        self.finished_turn = False  # True if participant has finished turn (busted or chose to stand)


    def draw_card(self, deck, n_cards=1):
        """Draws n random cards from deck to the hand."""
        for card in range(n_cards):
            card = deck[randint(0, len(deck) - 1)]  # Pop method?
            self.hand.append(card)
            self.points.append(assets.rank_value[card[0]])
            deck.remove(card)


    def count_points(self):
        """Sums total points of a hand"""
        self.total = 0
        for point in self.points:
            self.total += point


    def calculate_points(self):
        """Calculates points of a hand. If hand is over 21 points, revalues ace to 1 point.
           If participant is still over 21 total, sets the flag finished_turn."""
        Participant.count_points(self)

        if self.total > 21 and self.points.count(11) > 0:
            ace_index = self.points.index(11)
            self.points[ace_index] = 1
            Participant.count_points(self)

        if self.total > 21:
            self.finished_turn = True  # Bust a player


    def display_hand(self):
        """Displays participant's info in a console: hand, card values, total points."""
        print("< %s >" % self.name)

        print("HAND:"),
        for card in self.hand:
            print("%3s%s" % (card[0], card[1])),

        print("\nPTS: "),
        for point in self.points:
            print("%4d" % point),

        print("\nTOTAL: %3d" % self.total)


    # All participants' common moves
    def hit(self, deck):
        """Take the card"""
        Participant.draw_card(self, deck)
        Participant.calculate_points(self)
        Participant.display_hand(self)

    def stand(self):
        """Finish the turn"""
        self.finished_turn = True



class Dealer(Participant):
    
    def display_hidden_hand(self):
        """Displays dealer's hand with hidden ("hole") card"""
        print("< %s >" % self.name)
        print("HAND:   Xx  %3s%s" % (self.hand[1][0], self.hand[1][1]))
        print("PTS:     ?  %4d" % self.points[1])



class Player(Participant):

    # Additional player moves
    def double(self, deck):
        """Double wager, take a single card and finish"""
        # Double the bet
        Participant.draw_card(self, deck)
        Participant.calculate_points(self)
        Participant.display_hand(self)
        self.finished_turn = True

    def split(self, deck):
        """If the two cards have the same value, separate them to make two hands"""
        pass

    def surrender(self, deck):
        """Give up a half-bet and retire from the game"""
        pass
