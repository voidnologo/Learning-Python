# pg 276

import deck
from bj_card import BJ_Card

class BJ_Deck(deck.Deck):

    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))
