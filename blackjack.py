import random

class Deck(object):
    """docstring for Deck."""
    def __init__(self, arg):
        self.arg = arg

class Player(object):
    """docstring for Player."""
    def __init__(self, bankroll=100):
        self.bankroll = bankroll

    def add_bankroll(self, amount):
        self.bankroll += amount

class Hand(object):
    """docstring for Hand."""
    def __init__(self, arg):
        self.arg = arg
