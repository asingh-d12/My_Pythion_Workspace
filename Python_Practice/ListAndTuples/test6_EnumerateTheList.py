# We are starting using code from test5_listmethods.py only

current_choice = "-"
computer_choice = []
computer_parts = ["computer",
                  "mouse",
                  "keyboard",
                  "Monitor",
                  "mouse mat",
                  "HDMI Cable",
                  "DVD Drive",
                  ]

while current_choice != 0:
    # We can use list comprehension here as well
    if current_choice in [index + 1 for index, _ in enumerate(computer_parts)]:
    # if current_choice in list(range(1, len(computer_parts) + 1)):
        print("Adding {}".format(computer_parts[current_choice - 1]))
        # APPENDING DATA IN A LIST WHICH STARTED EMPTY
        computer_choice.append(computer_parts[current_choice - 1])
    else:
        print("Add options from the list below : ")
        # We are using enumerate here, rather than range and len so as to get a menu with number with part name
        for x, part in enumerate(computer_parts):
            print("{} -> {}".format(x+1, part))
        print("0 -> Exit/Finish!!")
    try:
        current_choice = int(input("Enter your choice : "))
    except ValueError as x:
        print("got {}, Try again".format(x))
        current_choice = '-'

print("Final Computer Choice = {}".format(computer_choice))
