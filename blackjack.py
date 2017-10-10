from random import shuffle

class Card(object):
    """Takes two integers as input and returns
    a printed description of playing card.

    Attributes:
        suit: Describes the suit of the card, valid integers are 1-4
        rank: Describse the rank of the card, valid integers are 1-13
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        suits=("","Hearts", "Spades", "Diamonds", "Clubs")
        ranks = ("","Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
                 "Eight", "Nine", "Ten", "Jack", "Queen", "King")
        if self.suit not in range(1,5):
            raise RuntimeError("Suit integer out of bounds")
        if self.rank not in range(1,14):
            raise RuntimeError("Rank integer out of bounds")
        return ("{0} of {1}".format(str(ranks[self.rank]),
                str(suits[self.suit])))

class Deck(object):
    """Assembles a suffled deck of cards in the form of a list of
    52 tuples that contain two integers describing rank and sort.
    """
    def __init__(self):
        self.deck = [(x, y) for x in range(1,5) for y in range(1,14)]
        for i in range(0, 5):
            shuffle(self.deck)
    def __iter__(self):
        return iter(self.deck)
    def draw(self):
        """Draws one card from the back of the deck and returns it
        as a tuple containing two integers describing rank and sort.
        """
        return self.deck.pop()

class Player(object):
    """Registers a player with the given bankroll amount.

    Attributes:
        bankroll: An integer that stores the current balance of the
                  players bankroll.
        hand: A list of tuples that represent the cards in the
              players hand.
    """
    def __init__(self, bankroll=100):
        self.bankroll = bankroll
        self.hand = []
    def add_bankroll(self, amount):
        """Adds the specified amount to a players bankroll."""
        self.bankroll += amount
    def withdraw_bankroll(self, amount):
        """Subtracts the specified amount from the players bankroll"""
        if amount > self.bankroll:
            raise RuntimeError("Amount greater than available bankroll.")
        self.bankroll -= amount
        return amount
    def draw_card(self, card):
        """Adds the specified card to a players hand."""
        self.hand.append(card)
    def show_hand(self):
        """Returns a list of tuples representing
        the cards in a players hand.
        """
        return self.hand

class Pot(object):
    """Registers and keeps track of players bets during each game.

    Attributes:
        balance: An integer that stores the current balance of the pot.
    """
    def __init__(self, balance=0):
        self.balance = balance
    def add(amount):
        """Adds the specified amount to the pot."""
        self.balance += amount
        return self.balance
    def payout():
        """Returns the pot balance and zeroes it."""
        payout = self.balance
        self.balance = 0
        return payout
