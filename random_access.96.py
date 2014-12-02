#Random Access
#Demonstrates string indexing
#pg96

import random

word = input("Your word:")

print("Your word is", word)

high = len(word)
low = -len(word)

print("high:", high, "\tlow:", low)

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])

