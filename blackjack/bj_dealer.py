#pg 279

import bj_hand

class BJ_Dealer(bj_hand.BJ_Hand):

    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print('{} busts.'.format(self.name))

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()
