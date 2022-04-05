from Deck import Deck
from Player import Player


deck = Deck()

player = Player("Name")
player2 = Player("Name2")
for i in range(1, 8):
    player.receiveCard(deck.get_card())
    player2.receiveCard(deck.get_card())

rank = player.getHighestRank()
print(f"{rank}")

rank2 = player2.getHighestRank()
print(f"{rank2}")








