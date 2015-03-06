# pg 275

import card

class BJ_Card(card.Card):

    ACE_VALUE = 1

    @property
    def value(self):
        value = None
        if self.is_face_up:
            value = BJ_Card.RANKS.index(self.rank) + 1
            if value > 10:
                value = 10
        return value
