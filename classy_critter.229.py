# Classy Critter
# demonstrates class attributes and static methods

# pg 229

class Critter(object):

    total = 0

    @staticmethod
    def status():
        print('\nThe total number of critters is', Critter.total)

    def __init__(self, name):
        print('A critter has been born.')
        self.name = name
        Critter.total += 1

#main
print('Accessing the class attribute Critter.total:', end=' ')
print(Critter.total)

print('\nCreating critters.')
crit1 = Critter('critter 1')
crit2 = Critter('critter 2')
crit3 = Critter('critter 3')

Critter.status()

print('\nAccessing the class attribute through an object:', end=' ')
print(crit1.total)
