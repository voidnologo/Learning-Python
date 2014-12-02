#Hero's Inventory
#Demonstrates Tuple Creation
#pg 109

# create an empty tuple
inventory = ()

# treat the tuple as a creation
if not inventory:
    print("You are empty handed.")

input("\nPress the enter key to continue.")

# create a tuple with some items
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

# print the tuple
print("\nThe tuple inventory is: ")
print(inventory)

# print each element in the tuple
print ("\nYour Items: ")
for item in inventory:
    print (item)


