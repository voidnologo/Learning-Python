# pg276

import hand


class BJ_Hand(hand.Hand):

    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = '{}\t{}'.format(self.name, super(BJ_Hand, self).__str__())
        if self.total:
            rep += '({})'.format(self.total)
        return rep
