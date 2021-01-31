locations = {0: "You are sitting in front of computer, learning Python",
             1: "You are standing at the end of the road, before a small brick building",
             2: "You are at the top of the hill",
             3: "You are inside a building, a well house for small stream",
             4: "You are in a valley, besides a stream",
             5: "You are in a forest"}

exits = [{"Q": 0},
         {"Q": 0, "E": 3, "N": 5, "S": 4, "W": 2},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

current_loc = 1
print(locations[current_loc])

err_msg = "This is not an available exit from here, Please Try again!!"

while current_loc != 0:
    available_exits = exits[current_loc].keys()
    print("You can go in following directions = {}".format(",".join(available_exits).upper()))
    direction = input("In which direction do you want to go : ").upper()
    if direction not in available_exits:
        print("-" * len(err_msg))
        print(err_msg)
        print("-" * len(err_msg))
        continue
    current_loc = exits[current_loc][direction]
    print("*" * 80)
    print(locations[current_loc])
