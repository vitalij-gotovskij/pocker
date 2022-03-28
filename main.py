import random
from Deck import Deck
from Card import Card
from Player import Player

from enum import Enum, auto, unique







# card1 = Card(CardRank.FIVE, Suit.SPADES)
# card2 = Card(CardRank.FOUR, Suit.HEARTS)
# card3 = Card(CardRank.ACE, Suit.CLUBS)
# card4 = Card(CardRank.EIGHT, Suit.SPADES)
# card5 = Card(CardRank.EIGHT, Suit.CLUBS)
# card6 = Card(CardRank.NINE, Suit.CLUBS)
# card7 = Card(CardRank.SEVEN, Suit.CLUBS)

deck = Deck()

player = Player("Name")
for i in range(1, 8):
    player.receiveCard(deck.get_card())

rank = player.getHighestRank()
print(f"{rank}")


#

#
# l = [card1, card2, card3, card4, card5, card6, card7]
# # print(l)
# # print(card1 < card3)








