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

    def getSuit(self):
        return self.__suit

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
        
    def __get_three(self, hand):
        value_list = []
        for i in hand:
            value_list.append(i.getValue().value)
            res = value_list.count(i.getValue().value)
            if res == 3:
                three_cards = [x for x in value_list if value_list.count(x) == 3]
                other_cards = [x for x in value_list if x not in three_cards]
                new_hand = three_cards+sorted(other_cards, reverse=True)
                return (HandRank.THREE, new_hand[:5])
        return None

    def __get_pair(self, __hand):
        # search for any card pair that has a duplicate, sort rest of the cards
        # return pair with largest 3 values of cards left
        seen_cards = []
        pair_cards = []
        for hand_card in __hand:
            for seen_card in seen_cards:
                if hand_card == seen_card:
                    pair_cards.extend([hand_card, seen_card])
                    left_cards = [x for x in __hand if x not in pair_cards]
                    left_cards.sort()
                    return_hand = pair_cards + left_cards
                    return HandRank.PAIR, return_hand[0:5]
            seen_cards.append(hand_card)
        return None

    def __get_flush(self, l):
        list_of_hearts = [card for card in l if card.getSuit().name == "HEARTS"]
        list_of_diamonds = [card for card in l if card.getSuit().name == "DIAMONDS"]
        list_of_clubs = [card for card in l if card.getSuit().name == "CLUBS"]
        list_of_spades = [card for card in l if card.getSuit().name == "SPADES"]
        checking_list = [list_of_clubs, list_of_diamonds, list_of_spades, list_of_hearts]
        for cards in checking_list:
            if len(cards) == 5:
                return HandRank.FLUSH, cards.sort(reverse=True)
        return None

    def __get_royal_flush(self, l):
        list_of_hearts = [card for card in l if card.getSuit().name == "HEARTS"]
        list_of_diamonds = [card for card in l if card.getSuit().name == "DIAMONDS"]
        list_of_clubs = [card for card in l if card.getSuit().name == "CLUBS"]
        list_of_spades = [card for card in l if card.getSuit().name == "SPADES"]
        checking_list = [list_of_clubs, list_of_diamonds, list_of_spades, list_of_hearts]
        for cards in checking_list:
            if len(cards) == 5:
                suited = sorted(cards, reverse=True)
                cheking = []
                for i in range(5):
                    cheking.append(suited[i].getValue().name)
                if cheking == ["ACE", "KING", "QUEEN", "JACK", "TEN"]:
                    return HandRank.ROYAL_FLUSH, suited
        return None


    def __get_straight_flush(self, cards_on_hand: list):
        cardsBySuit = {}
        if len(cards_on_hand) < 7:
            raise BaseException("There should be 7 cards on hand!")

        for card in cards_on_hand:
            if card.getSuit() not in cardsBySuit:
                cardsBySuit[card.getSuit()] = []
            cardsBySuit[card.getSuit()].append(card)

        cardsBySuitSorted = dict(sorted(cardsBySuit.items(), key=lambda item: len(item[1]), reverse=True))
        longest_list = next(iter(cardsBySuitSorted.items()))[1]
        if not len(longest_list) >= 5:
            return None

        longest_list.sort(reverse=True)
        last_card = None
        for card in longest_list:
            if not last_card:
                last_card = card
                continue
            if(last_card.getValue().value - card.getValue().value != 1):
                return None
            else:
                last_card = card
        else:
            return (HandRank.STRAIGHT_FLUSH, longest_list[:5])

        cardsBySuitSorted = dict(sorted(cardsBySuit.items(), key=lambda item: len(item[1]), reverse=True))
        longest_list = next(iter(cardsBySuitSorted.items()))[1]
        if not len(longest_list) >= 5:
            return None

    def getHighestRank(self):
        ret = None
        ret = self.__get_royal_flush(self.__hand)
        if ret:
            return ret

        ret = self.__get_straight_flush(self.__hand)
        if ret:
            return ret

        # ret = self.__get_four(self.__hand)  # TODO: implement this
        # if ret:
        #     return ret

        # ret = self.__get_full_house(self.__hand)  # TODO: implement this
        # if ret:
        #     return ret

        ret = self.__get_flush(self.__hand)
        if ret:
            return ret

        # ret = self.__get_straight(self.__hand)  # TODO: implement this
        # if ret:
        #     return ret

        ret = self.__get_three(self.__hand)
        if ret:
            return ret

        # ret = self.__get_two_pairs(self.__hand)  # TODO: implement this
        # if ret:
        #     return ret

        ret = self.__get_pair(self.__hand)
        if ret:
            return ret

        return self.__get_highest_card(self.__hand)


card1 = Card(CardRank.FIVE, Suit.SPADES)
card2 = Card(CardRank.FOUR, Suit.HEARTS)
card3 = Card(CardRank.ACE, Suit.CLUBS)
card4 = Card(CardRank.EIGHT, Suit.SPADES)
card5 = Card(CardRank.EIGHT, Suit.CLUBS)
card6 = Card(CardRank.NINE, Suit.CLUBS)
card7 = Card(CardRank.SEVEN, Suit.CLUBS)


player = Player("Name")
player.receiveCard(card1)
player.receiveCard(card2)
player.receiveCard(card3)
player.receiveCard(card4)
player.receiveCard(card5)
player.receiveCard(card6)
player.receiveCard(card7)

rank = player.getHighestRank()
print(rank)


#

#
# l = [card1, card2, card3, card4, card5, card6, card7]
# # print(l)
# # print(card1 < card3)








