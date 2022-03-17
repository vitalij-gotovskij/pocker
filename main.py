# import random
#
# deck = list()
# for suit in ["♦", "♥", "♠", "♣"]:
#     for value in ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]:
#         deck.append((value, suit))
# r_sample = random.sample(deck, 7)
# print(r_sample)


from enum import Enum, auto, unique

class Suit(Enum):
    HEARTS   = "♥"
    DIAMONDS = "♦"
    CLUBS    = "♣"
    SPADES   = "♠"

class CardRank(Enum):
    TWO   = auto()
    THREE = auto()
    FOUR  = auto()
    FIVE  = auto()
    SIX   = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE  = auto()
    TEN   = auto()
    JACK  = auto()
    QUEEN = auto()
    KING  = auto()
    AXE   = auto()


class HandRank(Enum):
    HIGHEST_CARD   = auto()
    PAIR           = auto()
    TWO_PAIRS      = auto()
    THREE          = auto()
    STRAIGHT       = auto()
    FLUSH          = auto()
    FULL_HOUSE     = auto()
    FOUR           = auto()
    STRAIGHT_FLUSH = auto()
    ROYAL_FLUSH    = auto()


class Card():
    def __init__(self, value, suit):
        self.__value = value
        self.__suit = suit

    def getValue(self):
        return self.__value

    def __str__(self):
        pass

    def __eq__(self, card2):
        return self.__value.value == card2.getValue().value

    def __lt__(self, card2):
        return self.__value.value < card2.getValue().value


card1 = Card(CardRank.FIVE,  Suit.SPADES)
card2 = Card(CardRank.SEVEN, Suit.CLUBS)
card3 = Card(CardRank.AXE,   Suit.CLUBS)
card4 = Card(CardRank.FIVE,  Suit.SPADES)
card5 = Card(CardRank.SEVEN, Suit.CLUBS)
card6 = Card(CardRank.AXE,   Suit.CLUBS)
card7 = Card(CardRank.AXE,   Suit.CLUBS)

l = [card1, card2, card3, card4, card5, card6, card7]

get_pair(l)      -> None or (PAIR, [card1, card2, 9, 10, A])
get_two_pairs(l) -> None or (TWO_PAIRS, [K, K, 8, 8, 3])
get_staight(l) ->   None or (HandRank.STRAIGHT, [5, 4, 3, 2, A])

print(card1 < card3)






