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

def winner_codition(player):
    if player.total>21:
        return too_much
    if player.total==21:
        return blackjack
    if player.total<21:
        return not_enough

def winner(player, dealer):
    dealer_result = winner_condition(dealer)
    player_result = winner_condition(player)

    if player_result