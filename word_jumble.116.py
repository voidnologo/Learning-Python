#Word Jumble
#
#The computer picks a random word and then jumbles it
# the player has to guess the original word
# pg 116

import random

#create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# pick one word at random from the sequence
word = random.choice(WORDS)

#create a variable to use later to see if the guess is right
answer = word

#create a jumbled version of the word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

#start the game
print(
"""
            Welcome to Word Jumble!
"""
)

print("the jumble is: ", jumble)

guess = input("\nYour Guess >>")

while guess != answer and guess != "":
    print("Wrong.")
    guess = input("\nYour Guess >>")

if guess == answer:
    print("Yeah! you win!")




