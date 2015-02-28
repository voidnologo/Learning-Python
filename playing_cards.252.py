# Playing Cards
# Demonstrates combining objects

# pg 252

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


#main
card1 = Card(rank='A', suit='c')
print('Card1:', end=' ')
print(card1)

card2 = Card(rank='1', suit='c')
card3 = Card(rank='2', suit='c')
card4 = Card(rank='3', suit='c')
card5 = Card(rank='4', suit='c')

print('The rest of the cards:')
print(card1)
print(card2)
print(card3)
print(card4)

my_hand = Hand()
print('\nHand before adding any cards: ', my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print('\nHand after adding cards: ', my_hand)

your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print('Your hand:', your_hand)
print('My hand:', my_hand)

my_hand.clear()
print('My hand cleared:', my_hand)

