greetings = ["Hello", "Hi", "Hola", "Namaste", "Sat Sri Akal", "Good Day"]
print(greetings)
print(id(greetings))

# No let's alter 1 greeting
greetings[5] = "Good Day Sir"
print(greetings)
print(id(greetings))

# CONCLUSION: SO, EVEN AFTER CHANGING AN ELEMENT OF THE LIST... THE ADDRESS REMAINED THE SAME
print("*" * 100)
print("Check this out")
print("1. Create a List, or take from previous code...")
computer_parts = ["computer",
                  "mouse",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)
print("Address of computer_parts = {}".format(id(computer_parts)))
print("2. Now bind another variable to this list...")
my_computer_parts = computer_parts
print("Printing second variable.. my_computer_parts")
print(my_computer_parts)
print("Address of my_computer_parts = {}".format(id(my_computer_parts)))
print("3. Now changing list binded to computer_parts variable, adding a printer in it...")
computer_parts.append("Printer")
print("4. Print computer_parts and my_computer_parts list again..")
print("computer_parts = {}".format(computer_parts))
print("my_computer_parts = {}".format(my_computer_parts))
print("Address of computer_parts = {}".format(id(computer_parts)))
print("Address of my_computer_parts = {}".format(id(my_computer_parts)))
