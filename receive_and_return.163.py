#Recieve and Return
#Demonstrates paramenters and return values
#pg 163

def display(message):
    print(message)

def give_me_a_five():
    five = 5
    return five

def ask_yes_no_question(question):
    """Ask a yes/no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


# main

display ("Displaying a message.\n")

number = give_me_a_five()
print("give_me_a_five() returned: ", number)

answer = ask_yes_no_question("\nPlease enter 'y' or 'n': ")
print("Entered: ", answer)
