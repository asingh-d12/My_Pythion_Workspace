import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

# First, let's store all these recipes in a shelve
with shelve.open("recipes.shelve", writeback=True) as recipes:
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

    # There are 2 ways to solve this, method 1 discussed in previous py file
    # 2. Enable writeback to true
    # recipes["pasta"].append("tomato")

    # Let's iterate over recipes after updating using method to overcome the
    # side affect
    # for snack in recipes:
    #     print("{} -> {}".format(snack, recipes[snack]))

    # Now this is updated fine when iterating over
    # How is this happening
    # Basically, if we use writeback=True. Python caches the shelf, and does
    # not write until either we close the shelve or call sync method on shelve

    # Basically, the iterating over... it is happening from the memory itself
    # and not the persistent shelve

    # Check this out, it might work
    # print("*" * 50)
    # another_recipes = shelve.open("recipes.shelve")
    # for snack in another_recipes:
    #     print("{} -> {}".format(snack, another_recipes[snack]))

    # So, the writeback actually does not update the shelf file
    # Hence comes the sync method
    # But when sync method is called, it causes all the entries in
    # cache written to disk but it clears out the cache

    # sync is actually called automatically when a shelve is closed

