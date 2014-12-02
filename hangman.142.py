#Hangman game
# The computer picks a random word which the player guesses one letter at a time.
#pg 149

#imports
import random

#constants
HANGMAN = (
"""
------
|    |
|
|
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|   -+-
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-/
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-/
|    |
|
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-/
|    |
|   |
|
|
|
----------
""",
"""
------
|    |
|    0
|  /-+-/
|    |
|   | |
|
|
|
----------
"""
)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")

#initialize variables
word = random.choice(WORDS)  #word to guess
so_far = "-" * len(word)     #dash for each letter in the word to be guessed
wrong = 0                    #number of guesses the player has made
used = []                    #letters already guessed

#main loop
print("Welcome to Hangman.")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("So far the word is: ", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You've already guessed: ", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\n", guess, "is in the word!")

        #create a new so_far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\n", guess, "is NOT in the word")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("You've LOST!")
else:
    print("You guessed it!")
    print("\nThe word was:", word)




