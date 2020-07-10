# So this is one of the examples I used else in loop
# Though Avoid it
# So, what's happening

# We have a list, which is checked for available exits
available_exits = ["north", "east", "south", "west"]
chosen_exit = ""

# This is loop where a user is asked for a direction to exit,
# This direction is then checked against available_exits list,
# If direction is present, then cool.. you are out of loop
# If not, then rinse and repeat...
# But there is 1 more twist
# If user enters "quit" instead of a direction
while chosen_exit not in available_exits:
    print("You are still in the Maze!!! Muahahahahah Muahahahah")
    chosen_exit = input("Enter a direction : ").lower()
    # If user enters "quit" then,
    # User goes out of loop with a break statement
    if chosen_exit == "quit":
        print("I quit!!")
        break
else:
    # So, why use else here and when does it execute
    # Basically, we do not want a user who "quits" the game to see this
    # This message is only for users who played this game completely
    # So, this is in else block
    # When the game is "quitted", break is encountered,
    # due to the break statement, this else block is not executed
    print("I am out!! I am out!! huff huff... or am I")
