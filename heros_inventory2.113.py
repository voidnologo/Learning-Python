#Hero's Inventory 2.0
#Demonstrates tuples
#pg 113

# create a tuple with some items and display them in a for loop
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

print ("Your items: ")
for item in inventory:
    print (item)

input("\n>>")

#get the length of a tuple
print("You have", len(inventory), "items in your possession.")

input("\n>>")

#test for membership with in
if "healing potion" in inventory:
    print("You have a healing potion in your inventory.")

#display on item through an index
index = int(input("\nEnter the index number for an item in the inventory.: "))
print("At index", index, "is", inventory[index])

#display a slice
start = int(input("\nEnter the index number to begin the slice."))
end = int(input("Enter the index number to end the slice."))
print("Inventory[", start, ":", end, "] is", end=" ")
print(inventory[start:end])

input("\n>>")


#concatenate two tuples
chest = ("gold", "gems")
print("You find a chest.  It contains: ")
print(chest)

print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\n>>")

