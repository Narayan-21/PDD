from collections import namedtuple

_Suits = ('spades','hearts','clubs','diamonds')
_Ranks = tuple(range(2,11))+tuple('JQKA')

Card = namedtuple('Card', 'rank suit')

class CardDeck:
    def __init__(self):
        self.length = len(_Suits)*len(_Ranks)
    def __len__(self):
        return self.length
    def __iter__(self):
        return self.CardDeckIterator(self.length)
    def __reversed__(self):
        return self.CardDeckIterator(self.length, reverse=True)
    class CardDeckIterator:
        def __init__(self, length, reverse = False):
            self.length = length
            self.reverse = reverse
            self.i = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                if self.reverse:
                    index = self.length - 1 - self.i
                else:
                    index = self.i
                suit = _Suits[index // len(_Ranks)]
                rank = _Ranks[index % len(_Ranks)]
                self.i += 1
                return Card(rank, suit)
