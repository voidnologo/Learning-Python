import games
from bj_game import BJ_Game


def main():
    print('\n\t\tWelcome to Blackjack\n')

    names = []
    number = games.ask_number('How many players? (1-7):', low=1, high=8)
    for i in range(number):
        name = input('Enter player name:')
        names.append(name)

        print()

        game = BJ_Game(names)

        again = None
        while again != 'n':
            game.play()
            again = games.ask_yes_no('\n\nDo you want to play again?:')

main()
