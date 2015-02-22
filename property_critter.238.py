# Property Critter
# demonstrates properties

# pg 238

class Critter(object):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name:
            self.__name = new_name
            print('Name change successful.')
        else:
            print('Provide a valid name.')

    def talk(self):
        print('My name:', self.name)

#main
crit = Critter('Poochie')
crit.talk()

print('\nCritters name is:', end=' ')
print(crit.name)

print('\nChanging name.')
crit.name = 'Randolph'

print('\nCritters name is:', end=' ')
print(crit.name)

print('\nChange name ot empty string.')
crit.name = ''

print('\nCritters name is:', end=' ')
print(crit.name)
