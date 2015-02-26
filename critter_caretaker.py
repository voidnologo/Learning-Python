
# Critter Caretaker
# a virtual pet to care for

class Critter(object):

    MAX_FOOD = 20
    MAX_FUN = 20

    def __init__(self, name, fullness=MAX_FOOD, happiness=MAX_FUN):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.alive = True

    def __pass_time(self, fullness_time=1, happiness_time=1):
        self.fullness -= fullness_time
        self.happiness -= happiness_time

    def __str__(self):
        return '{} - fullness: {}\thappiness: {}'.format(self.name, self.fullness, self.happiness)

    @property
    def mood(self):
        if self.fullness < 5:
            hungry = "famished"
        elif self.fullness <= 10:
            hungry = "hungry"
        elif self.fullness <= 15:
            hungry = "ok"
        else:
            hungry = "full"

        if self.happiness < 5:
            bored = "unloved"
        elif self.happiness <= 10:
            bored = "bored"
        elif self.happiness <= 15:
            bored = "ok"
        else:
            bored = "happy"

        return '{} and {}'.format(hungry, bored)

    def living(self):
        cause1 = ''
        cause2 = ''
        conjunction = ''
        if self.fullness <=0:
            cause1 = 'starvation'
            self.alive = False
        if self.happiness <= 0:
            cause2 = 'boredom'
            self.alive = False
        if cause1 and cause2:
            conjunction = ' and '
        return self.alive, '{}{}{}'.format(cause1, conjunction, cause2)

    def talk(self):
        print('I am', self.name, 'and I feel', self.mood, 'now.\n')
        print('Fullness : {}'.format('*' * self.fullness))
        print('Happiness: {}'.format('*' * self.happiness))
        self.__pass_time()

    def eat(self, food=4):
        print('Brruppp.  Thank you!')
        self.fullness += food
        if self.fullness > self.MAX_FOOD:
            self.fullness = self.MAX_FOOD
        happiness_time = int(food / 3) or 1
        self.__pass_time(happiness_time=happiness_time)

    def play(self, fun=4):
        print('Wheee!')
        self.happiness += fun
        if self.happiness > self.MAX_FUN:
            self.happiness = self.MAX_FUN
        fullness_time = int(fun * 0.5) or 1
        self.__pass_time(fullness_time=fullness_time)

    def ignore(self):
        self.__pass_time()
        self.happiness -= int(self.happiness * 0.5)
        self.fullness -= int(self.fullness * 0.5)


def menu(crit_name):
    return \
    ("""
        0 = Quit
        1 - Listen to {name}
        2 - Feed {name}
        3 - Play with {name}
        4 - Ignore {name}
    """.format(name=crit_name))
    print()

def get_choice(crit_name):
    print(menu(crit_name))
    choice = True
    while choice:
        choice = input("\nChoice:")
        if choice in ['0', '1', '2', '3', '4'] or choice == 'values':
            return choice
        else:
            print('Make a valid choice.')
            choice = False

def handle_choice(crit, choice=1):
        #exit
        if choice == '0':
            print('Good bye')
            return False  # don't keep playing
        #listen
        elif choice == '1':
            crit.talk()
        #feed
        elif choice == '2':
            amount = int(input('How much food?:'))
            crit.eat(food=amount)
        #play
        elif choice == '3':
            amount = int(input('How long?:'))
            crit.play(fun=amount)
        #ignore
        elif choice == '4':
            crit.ignore()
        #values
        elif choice == 'values':
            print(crit)

        return True  # keep playing

def main():
    print('\t\tCRITTER CARETAKER')
    print('\n\tTake care of your critter!')
    print('\tMake sure your critter is well fed and loved,\n\tor they might die!\n\n')
    crit_name = input("What do you want to name your critter?:")
    crit = Critter(crit_name)

    play = True
    choice = ''
    while play:
        choice = get_choice(crit.name)
        play = handle_choice(crit, choice=choice)

        living, cause = crit.living()
        if not living:
            print('{} has died from {}!'.format(crit.name, cause))
            break

main()
