#No Vowels
#Demonstrates createing new strings with a for loop
#pg102

message = input("Enter a message: ")
new_message = ''
VOWELS = "aeiou"

for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("New string:", new_message)

print("\n Your message without vowels is:", new_message)

