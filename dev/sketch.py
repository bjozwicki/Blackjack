TODO: create correct references in files after creating catalog structure

Punktowanie wygranych:

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

"""
TODO:
    Add human player options
    Add skeleton options for 4 and 5th move (ins./surrender)
    Add random/semi-random/standard strategy ai (as difficulty options)
    Add betting and payouts
    Add catalog structure
    Rewrite win function into separate functions, one setting win_prio, other comparing results of dealer and player
    Separate functions in main_game -> game()
    Create function rendering menu in text format
    main_game -> exiting to main menu from current game (2 errors)
"""

Catalog structure:
    0 Main catalog
        Blackjack.py
        .git
        .gitignore
        Readme.txt

        1 main
            main_game.py

        2 classes
            classes.py

        3 assets
            Assets.py
            Instructions.txt

        4 dev
            Sketch.py