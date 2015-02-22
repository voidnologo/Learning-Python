# Attribute Critter
# demonstrates creating and accessing object attributes

# pg 225

class Critter(object):
    def __init__(self, name):
        print('A new critter has been born.')
        self.name = name

    def __str__(self):
        rep = 'Critter Object\n'
        rep += 'name:' + self.name + '\n'
        return rep

    def talk(self):
        print('Hi. I am', self.name, '\n')

#main
crit1 = Critter('Poochie')
crit1.talk()

crit2 = Critter('Randolf')
crit2.talk()

print('Printing crit1')
print(crit1)

print('Printing crit2')
print(crit2)

print('Directly accessing crit1.name')
print(crit1.name)

print('Directly accessing crit2.name')
print(crit2.name)
