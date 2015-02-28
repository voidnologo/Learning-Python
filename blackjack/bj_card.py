# pg 275

import card
import games

class BJ_Card(card.Card):

    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            value = BJ_Card.RANKS.indes(self.rank) + 1
            if value > 10:
                value = 10
        return value or None
