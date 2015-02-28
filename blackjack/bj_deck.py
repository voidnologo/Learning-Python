# pg 276

import deck
import bj_card


class BJ_Deck(Deck):

    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.appen(BJ_Card(rank, suit))
