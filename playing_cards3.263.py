
# Playing Cards 3.0
# Demonstrates inheritance -overriding methods

# pg 263

class Card(object):

    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
    SUITS = ['c', 'd', 'h', 's']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '{}{}'.format(self.rank, self.suit)

class UnprintableCard(Card):

    def __str__(self):
        return '<unprintable>'

class PositionableCard(Card):

    def __init__(self, rank, suit, face_up=True):
        super(PositionableCard, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            return super(PositionableCard, self).__str__()
        return 'XX'

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand(object):

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            hand = ''
            for card in self.cards:
                hand += '{} '.format(card)
            return hand
        return '<empty>'

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    self.give(self.cards[0], hand)

# main
card1 = Card('A', 'c')
card2 = UnprintableCard('A', 'd')
card3 = PositionableCard('A', 'h')

print('Card object:', card1)
print('\nUnprintabe Card:', card2)
print('\nPositionable Card:', card3)

card3.flip()
print('Flippin the card:', card3)
