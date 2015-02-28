# Alien Blaster
# Demonstrates object interaction

# pg 250

class Player(object):

    def blast(self, enemy):
        print('The player blasts the enemy.')
        enemy.die()

class Enemy(object):

    def die(self):
        print('Death message.')

#main

hero = Player()
enemy = Enemy()

hero.blast(enemy)
