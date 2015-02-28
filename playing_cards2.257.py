# Playing Cards 2.0
# Demonstrates inheritance - class extension

# pg 257

class Card(object):

    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
    SUITS = ['c', 'd', 'h', 's']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '{}{}'.format(self.rank, self.suit)

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

#main
deck = Deck()
print('Created a new deck.')
print('DECK:', deck)

deck.populate()
print('Populated deck.')
print('DECK:', deck)

deck.shuffle()
print('Shuffled deck.')
print('DECK:', deck)

my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]

deck.deal(hands, per_hand=5)
print('Dealt 5 cards to each hand.')
print('MY HAND:' , my_hand)
print('YOUR HAND:', your_hand)
print('DECK:', deck)
