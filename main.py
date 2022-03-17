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
    ACE   = auto()


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
        return f"{self.__value} of {self.__suit.value}"

    def __eq__(self, card2):
        return self.__value.value == card2.getValue().value

    def __lt__(self, card2):
        return self.__value.value < card2.getValue().value


class Player(Card):
    def __init__(self, name):
        self.__name = name
        self.__hand = []

    def getName(self):
        return self.__name

    def receiveCard(self, new_card):
        if isinstance(new_card, Card):
            self.__hand.append(new_card)

    def showHand(self):
        hand_str = []
        for card in self.__hand:
            hand_str.append(card)
        print(hand_str)

def get_pair(hand):
    # search for any card pair that has a duplicate, sort rest of the cards
    # return pair with largest 3 values of cards left
    seen_cards = []
    pair_cards = []
    for hand_card in hand:
        for seen_card in seen_cards:
            if hand_card == seen_card:
                pair_cards.extend([hand_card, seen_card])
                left_cards = [x for x in hand if x not in pair_cards]
                left_cards.sort()
                return_hand = pair_cards + left_cards
                return return_hand[0:5]
        seen_cards.append(hand_card)
    return None

card1 = Card(CardRank.FIVE, Suit.SPADES)
card2 = Card(CardRank.FOUR, Suit.HEARTS)
card3 = Card(CardRank.ACE, Suit.CLUBS)
card4 = Card(CardRank.EIGHT, Suit.SPADES)
card5 = Card(CardRank.EIGHT, Suit.SPADES)
card6 = Card(CardRank.NINE, Suit.CLUBS)
card7 = Card(CardRank.SEVEN, Suit.CLUBS)

l = [card1, card2, card3, card4, card5, card6, card7]
# print(l)
# print(card1 < card3)
hand = get_pair(l)
for item in hand:
    print(item)







