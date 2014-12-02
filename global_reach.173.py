#Global Reach
#Demonstrates global variables
#pg 173

def read_global():
    print("From inside the local scope of read_global(), value is: ", value)

def shadow_global():
    value = -10
    print("From inside the local scope of shadow_global(), value is: ", value)

def change_global():
    global value
    value = -10
    print("From inside the local scope of change_global(), value is: ", value)


#main
#value is a global variable because we are in the global scope here
value = 10
print("In global scope, value has been set to: ", value)

read_global()
print("Global: ", value)

shadow_global()
print("Global: ", value)

change_global()
print("Global: ", value)

