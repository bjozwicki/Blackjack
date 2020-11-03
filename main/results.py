def winner(player, dealer):
    """Prints in a console result of a game and returns winner (type = str)"""
    if player.total > 21:
        print("Player busted. Dealer won.")
        return "dealer"
    elif dealer.total > 21:
        print("Dealer busted. Player won.")
        return "player"

    elif dealer.total == 21 and len(dealer.hand) == 2:
        print("Blackjack. Dealer won.")
        return "dealer"
    elif player.total == 21 and len(player.hand) == 2:
        print("Blackjack. Player won.")
        return "player"

    elif dealer.total >= player.total:
        print("Player didn't get more points than dealer. Dealer won.")
        return "dealer"
    elif dealer.total < player.total:
        print("Player got more points than dealer. Player won.")
        return "player"