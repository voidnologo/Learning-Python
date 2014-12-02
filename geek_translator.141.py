#Geek Translator
#Demonstrates using dictionaries
#pg 141

geek_dict = {
        "404"                    :"clueless", 
        "Googling"               :"look something up on the internet", 
        "Keyboard plaque"        :"the collection of gunk on and in your keyboard",
        "Link rot"               :"web page link deteriation",
        "Percussive Maintenance" : "hit it to make it work"
        }

choice = None
while choice != "0":
    print(
    """
        0 - Quit
        1 - Look up
        2 - Add
        3 - Redefine
        4 - Delete
    """)

    choice = input("Input: ")
    print()

    #exit
    if choice == "0":
        print ("END")
    
    #look up
    elif choice == "1":
        term = input("Look up: ")
        if term in geek_dict:
            definition = geek_dict[term]
            print("\n", term, "means", definition)
        else:
            print("Term not in dictionary.")

    #Add
    elif choice == "2":
        term = input("Add term: ")
        if term not in geek_dict:
            definition = input("Definition: ")
            geek[term] = definition
            print("\n", term, "has been added.")
        else:
            print(term, "is already in the dictionary.")

    #Redefine
    elif choice == "3":
        term = input("Redefine: ")
        if term in geek_dict:
            definition = input("New definition: ")
            geek[term] = definition
            print(term, "has been redefined.")
        else:
            print (term, "is not in the dictionary.")

    #Delete
    elif choice == "4":
        term = input("Delete: ")
        if term in geek_dict:
            del geek[term]
            print(term, "has been deleted.")
        else:
            print(term, "not in dictionary.")

    #list terms
    elif choice == "5":
    #    for term in geek_dict:
    #        print(term)
        print(geek_dict.keys())

    #default
    else:
        print("Invalid option.")


