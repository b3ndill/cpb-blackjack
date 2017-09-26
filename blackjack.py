from random import shuffle

class Card(object):
    """docstring for Card."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        suits=("","Hearts", "Spades", "Diamonds", "Clubs")
        ranks = ("","Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
        return("{0} of {1}".format(str(ranks[self.rank]), str(suits[self.suit])))

class Deck(object):
    """docstring for Deck."""
    def __init__(self):
        self.deck = [(x, y) for x in range(1,5) for y in range(1,14)]
        for i in range(0, 5):
            shuffle(self.deck)
    def __iter__(self):
        return iter(self.deck)
    def draw(self):
         return self.deck.pop()

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
