#pg 278

import games
import bj_hand

class BJ_Player(bj_hand.BJ_Hand):

    def is_hitting(self):
        response = games.ask_yes_no('\n {} do you want to hit? (Y/N):'.format(self.name))
        return response == 'y'

    def bust(self):
        print('{} busts.'.format(self.name))

    def win(self):
        print('{} wins.'.format(self.name))

    def lose(self):
        print('{} loses.'.format(self.name))

    def push(self):
        print('{} pushes.'.format(self.name))
