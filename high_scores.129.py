#High Scores
#Demonstrates list methods
# pg 129

scores = []
choice = None

while choice != "0":
    print(
"""
    High Scores

    0 - Exit
    1 - Show Scores
    2 - Add a score
    3 - Delete a score
    4 - Sort scores
    ***
"""
            )

    choice = input("Choice: ")
    print()

    #exit
    if choice == "0":
        print("END")

    #list high-scores table
    elif choice == "1":
        print("High Scores")
        for score in scores:
            print(score)

    #add a score
    elif choice == "2":
        score = int(input("What score did you get?: "))
        scores.append(score)

    #remove a score
    elif choice == "3":
        score = int(input("Remove which score?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, " can't be found in the list.")

    #sort scores
    elif choice == "4":
        scores.sort(reverse=True)

    #default
    else:
        print("Invalid choice.")

