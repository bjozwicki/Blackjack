# -*- coding: utf-8 -*-


def new_deck(deck_copies=1):
    """Returns a new, sorted deck [type = list] consisting of n-copies of 52-card deck"""
    deck = []

    for deck_copy in range(deck_copies):
        for i in range(0, 52):
            rank_id = i // 4
            suit_id = i % 4
            deck.append((assets.rank[rank_id], assets.suit[suit_id]))

    return deck