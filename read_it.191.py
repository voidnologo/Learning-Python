#Read It
# Demonstrates reading from a text file
# pg 191

print('Opening and closing the file.')
text_file = open("read_it.190.txt", "r")
text_file.close()

print('\nReading characters from the file.')
text_file = open("read_it.190.txt", "r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print('\nReading the entire file at once')
text_file = open("read_it.190.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print('\nReading the entire file into a list.')
text_file = open("read_it.190.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print('\nLooping through the file, line by line')
text_file = open("read_it.190.txt", "r")
for line in text_file:
    print(line)
text_file.close()


