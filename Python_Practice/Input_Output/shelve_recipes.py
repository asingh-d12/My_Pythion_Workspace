import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

# First, let's store all these recipes in a shelve
with shelve.open("recipes.shelve") as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta

    # After recipes are saved in a shelve file, commenting out all the
    # recipes now

    # Let's iterate over recipes now
    for snack in recipes:
        print("{} -> {}".format(snack, recipes[snack]))

    print("*" * 50)

    # Let's update some items
    # recipes['blt'].append("butter")
    # recipes['pasta'].append("tomato")

    # Let's iterate over recipes after updating the lists only
    # for snack in recipes:
    #     print("{} -> {}".format(snack, recipes[snack]))

    # Ok, so if you look at this, it is not updated when we iterated over them
    # Not exactly... lists are appended, but shelve do not know that yet
    # What exactly is happening?
    # The shelve that is in memory is updated... but the iterating over is
    # from persistent location... where it is not updated.

    # This happens to keep disk writes minimum, but this is 1 side affect

    # There are 2 ways to solve this
    # 1. assign the copy of a list to the key completely
    temp_list = recipes["blt"]
    temp_list.append("butter")
    recipes["blt"] = temp_list

    temp_list = recipes["pasta"]
    temp_list.append("tomato")
    recipes["pasta"] = temp_list

    # Let's iterate over recipes after updating using method to overcome the
    # side affect
    for snack in recipes:
        print("{} -> {}".format(snack, recipes[snack]))

    # Now this is updated fine when iterating over

