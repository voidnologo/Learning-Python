
# pg 272

class Hand(object):

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            hand = ''
            for card in self.cards:
                hand += '{}\t'.format(card)
            return hand
        return '<empty>'

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
