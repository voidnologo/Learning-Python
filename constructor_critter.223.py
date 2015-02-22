# Constructor Critter
# demonstrates contructors

#pg 223

class Critter(object):

    def __init__(self):
        print('A new critter has been born.')

    def talk(self):
        print('\nI\'m an instance of class Critter.')

#main
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()
