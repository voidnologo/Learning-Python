#High Scores 2.0
# demonstrates nested sequences
# pg 136

scores = []

choice = None
while choice != "0":
    print(
"""
    High Scores 2.0

    0 - Quit
    1 - List
    2 - Add
""")

    choice = input("Choice:")
    print()

    #exit
    if choice == "0":
        print("END")

    #display high scores
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    #add a score
    elif choice == "2":
        name = input("Name: ")
        score = int(input("Score: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] #keep only the top 5

    #default
    else:
        print("Invalid choice")


