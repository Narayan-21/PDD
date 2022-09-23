# Creating Card deck iterable.
from collections import namedtuple
Card = namedtuple('Card', 'rank suit')

class CardDeck:
    SUITS = ('Spades', 'Hearts', 'Diamond', 'Clubs')
    RANKS = tuple(range(2,11))+tuple('JQKA')

    def __iter__(self):
        return CardDeck.card_gen()
    def __reversed__(self):
        return CardDeck.rev_card_gen()

    @staticmethod
    def card_gen():
        for suit in CardDeck.SUITS:
            for rank in CardDeck.RANKS:
                yield Card(rank, suit)
    @staticmethod
    def rev_card_gen():
        for suit in reversed(CardDeck.SUITS):
            for rank in reversed(CardDeck.RANKS):
                yield Card(rank, suit)
