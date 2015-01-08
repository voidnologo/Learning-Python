#Write It
# Demonstrates writing to a text file
# pg 197

print('Creating a text file with the write() method')
text_file = open("write_it.197.txt", "w")

text_file.write("Line1\n")
text_file.write("This is line2\n")
text_file.write("That makes this line 3\n")

text_file.close()

print("\nReading the newly created file.")
text_file = open("write_it.197.txt", "r")
print(text_file.read())
text_file.close()

print('\nCreating a text file with the writelines() method.')
text_file = open("write_it.198.txt", "w")

lines = ["Line1\n",
        "This is line2\n",
        "That makes this line 3\n",
]

text_file.writelines(lines)
text_file.close()

print("\nReading the newly created file.")
text_file = open("write_it.198.txt", "r")
print(text_file.read())
text_file.close()
