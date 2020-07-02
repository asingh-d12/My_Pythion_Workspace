available_exits = ["north", "east", "south", "west"]
chosen_exit = ""

while chosen_exit not in available_exits:
    print("You are still in the Maze!!! Muahahahahah Muahahahah")
    chosen_exit = input("Enter a direction : ").lower()
    if chosen_exit == "quit":
        print("I quit!!")
        break
else:
    print("I am out!! I am out!! huff huff... or am I")
