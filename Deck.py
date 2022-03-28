from Card import *
import random


class Deck():

    def __init__(self):
        self.cards = []
        self.flop = []
        values = list(CardRank)
        suits = list(Suit)   # ♠ ♣ ♥ ♦
        for value in values:
            for suit in suits:
                card = Card(value, suit)
                self.cards.append(card)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        card = self.cards.pop()
        return card

    def flop_cards(self):
        print(f"Flop is: ")
        for i in range(5):
            card = deck.get_card()
            self.flop.append(card)
            card.print_card()
