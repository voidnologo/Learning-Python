# Critter Caretaker
# a virtual pet to care for

# pg 242

class Critter(object):

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            return "happy"
        elif unhappiness <= 10:
            return "okay"
        elif unhappiness <= 15:
            return "frusterated"
        else:
            return "mad"

    def talk(self):
        print('I am', self.name, 'and I feel', self.mood, 'now.\n')
        self.__pass_time()

    def eat(self, food=4):
        print('Brruppp.  Thank you!')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print('Wheee!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("What do you want to name your critter?:")
    crit = Critter(crit_name)

    choice = None
    while choice != '0':
        print \
        ("""
            Critter Caretaker

            0 = Quit
            1 - Listen to {}
            2 - Feed {}
            3 - Play with {}
        """.format(crit_name, crit_name, crit_name))
        choice = input('Choice:')
        print()

        #exit
        if choice == '0':
            print('Good bye')
        #listen
        elif choice == '1':
            crit.talk()
        #feed
        elif choice == '2':
            crit.eat()
        #play
        elif choice == '3':
            crit.play()
        #other unknown
        else:
            print('Make a valid choice.')

main()
