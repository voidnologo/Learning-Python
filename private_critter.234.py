# Private Critter
# demonstrates private variables and methods

# pg 234

class Critter(object):

    def __init__(self, name, mood):
        print('A new critter has been born.')
        self.name = name    #public
        self.__mood = mood  #private

    def talk(self):
        print('\nI am', self.name)
        print('Right now I feel', self.__mood, '\n')

    def __private_method(self):
        print('This is a private method.')

    def public_method(self):
        print('This is a public method.')
        self.__private_method()

#main
crit = Critter(name='Poochie', mood='happy')
crit.talk()
crit.public_method()
