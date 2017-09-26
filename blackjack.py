import random

class Card(object):
    """docstring for Card."""
    suits=("Hearts", "Spades", "Diamonds", "Clubs")
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        labels = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
        return("{0} of {1}".format(str(labels[self.number]), self.suit))

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

x = Card(11, "Hearts")
print(x)
