import unittest
from Player import Player, HandRank
from Card import Card, CardRank, Suit


class TestPlayer(unittest.TestCase):
    def setUp(self):
        print(f"Running{self.__class__}setup")


    def tearDown(self):
        print(f"Running{self.__class__}teardown")


    def test_pair(self):
        print(f"Running test test_pair")
        player = Player("Name")
        player.receiveCard(Card(CardRank.EIGHT, Suit.SPADES))
        player.receiveCard(Card(CardRank.FIVE,  Suit.SPADES))
        player.receiveCard(Card(CardRank.FOUR,  Suit.HEARTS))
        player.receiveCard(Card(CardRank.ACE,   Suit.CLUBS))
        player.receiveCard(Card(CardRank.NINE,  Suit.CLUBS))
        player.receiveCard(Card(CardRank.SEVEN, Suit.CLUBS))
        player.receiveCard(Card(CardRank.EIGHT, Suit.CLUBS))

        rank = player.getHighestRank()
        self.assertEqual(HandRank.PAIR, rank[0])


    def test_two_pairs(self):
        print(f"Running test test_two_pairs")
        player = Player("Name")
        player.receiveCard(Card(CardRank.FOUR,  Suit.SPADES))
        player.receiveCard(Card(CardRank.ACE,   Suit.CLUBS))
        player.receiveCard(Card(CardRank.EIGHT, Suit.SPADES))
        player.receiveCard(Card(CardRank.SIX,   Suit.CLUBS))
        player.receiveCard(Card(CardRank.FOUR,  Suit.HEARTS))
        player.receiveCard(Card(CardRank.SIX,   Suit.SPADES))
        player.receiveCard(Card(CardRank.SEVEN, Suit.CLUBS))

        rank = player.getHighestRank()
        self.assertEqual(HandRank.TWO_PAIRS, rank[0])
