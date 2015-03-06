# pg276

import hand
from bj_card import BJ_Card


class BJ_Hand(hand.Hand):

    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = '{}\t{}'.format(self.name, super(BJ_Hand, self).__str__())
        if self.total:
            rep += '({})'.format(self.total)
        return rep

    @property
    def total(self):
        total = 0
        contains_ace = False
        for card in self.cards:
            if not card.value:
                return None
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
            total += card.value

        if contains_ace and total <= 11:
            total += 10

        return total

    def is_busted(self):
        return self.total > 21
