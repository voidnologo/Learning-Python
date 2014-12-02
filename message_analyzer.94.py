#Message Analyzer
#Demonstrates the len() function and the <in> operator
#pg94

message = input("Enter Message:")

print("\nThe length of your message is:", len(message))
print("\nThe most common letter in the english language 'e',")

if "e" in message:
    print("is in your message.")
else:
    print("is not in your mesage.")


