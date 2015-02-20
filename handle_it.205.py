# Handle it
# Demonstrates handling exceptions

# pg 206

#try/except
try:
    num = float(input("Enter a number: "))
except:
    print('Something went wrong.')

# specify exception type
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print('That was not a number.')

# multiple exception types
print()
for value in (None, "Hi!"):
    try:
        print('Attempting to convert', value, '-->', end=' ')
        print(float(value))
    except (TypeError, ValueError):
        print('Something went wrong.')

# multiple exception types
print()
for value in (None, "Hi!"):
    try:
        print('Attempting to convert', value, '-->', end=' ')
        print(float(value))
    except TypeError:
        print('Can only convert a string or a number.')
    except ValueError:
        print('Can only convert a string of digits.')

# get an exceptions agument
try:
    num = float(input("\nEnter a number: "))
except ValueError as e:
    print('That was not a number.')
    print(e)

# try/except/else
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print('That was not a number.')
else:
    print('You entered the number', num)

