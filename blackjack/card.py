
# pg 271

class Card(object):

    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
    SUITS = ['c', 'd', 'h', 's']

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            return '{}{}'.format(self.rank, self.suit)
        else:
            return 'XX'

    def flip(self):
        self.is_face_up = not self.is_face_up
