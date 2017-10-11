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
    def show_score(self):
        """Returns the score from the players hand. It assumes that
        the ace is valued at 11 if the sum of the other cards is
        below 11.
        """
        score = 0
        hand_rank = [card[1] for card in self.hand]
        for i in hand_rank:
            if i > 10:
                score += 10
            else:
                score += i
        if 1 in hand_rank and score < 12:
            return score + 10
        else:
            return score

class Pot(object):
    """Registers and keeps track of players bets during each game.

    Attributes:
        balance: An integer that stores the current balance of the pot.
    """
    def __init__(self, balance=0):
        self.balance = balance
    def add(self, amount):
        """Adds the specified amount to the pot."""
        self.balance += amount
        return self.balance
    def payout():
        """Returns the pot balance and zeroes it."""
        payout = self.balance
        self.balance = 0
        return payout

def check_bust(score):
    if score > 21:
        return True
    else:
        return False

def main():
    while True:
        #Starting the game
        print("Welcome to Blackjack!")
        print("It's just you and the dealer! Your bankroll is 100 credits.\n")
        dealer1 = Player(bankroll=500000000)
        player1 = Player(bankroll=100)
        pot1 = Pot()
        while True:
            #Betting
            while True:
                player1_bet = int(input("Please enter a bet. Minimum bet is 5 credits, maximum is 100: "))
                if player1_bet in range(5, 101):
                    pot1.add(player1.withdraw_bankroll(player1_bet))
                    pot1.add(dealer1.withdraw_bankroll(player1_bet))
                    break
                print("Invalid input, please try again")
            #The Deal
            print("The dealer shuffles the cards and starts dealing...")
            deck1 = Deck()
            for i in range(0,2):
                player1.draw_card(deck1.draw())
                dealer1.draw_card(deck1.draw())
            #The Play
            while True:
                print("Your hand is:")
                for card in player1.show_hand():
                    print(Card(*card))
                print("Your score is: {0}".format(player1.show_score()))
                hitstay = str(input("Would you like to hit or stay?: "))
                while True:
                    if hitstay in ("hit", "stay"):
                        break
                    print("Invalid input, please try again")
                if hitstay == "hit":
                    player1.draw_card(deck1.draw())
                    continue
                else:
                    break
            #The Dealer's Play
            while True:
                print("The dealer's hand is:")
                for card in dealer1.show_hand():
                    print(Card(*card))
                while dealer1.show_score() < 17:
                    print("The dealer draws another card.")
                    dealer1.draw_card(deck1.draw())
                break
            print("The dealer's score is: {0}".format(dealer1.show_score()))
            break
        break

if __name__ == "__main__":
    main()
