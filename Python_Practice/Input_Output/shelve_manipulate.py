import shelve

# Shelves are opened in read and write mode by default. So no need to specify.
with shelve.open('shelftest') as fruit:
    fruit['orange'] = "a sweet orange citrus fruit."
    fruit['apple'] = "good from making cider."
    fruit['lemon'] = "a sour yellow citrus fruit.."
    fruit['grape'] = "a small, sweet fruit growing in bunches."
    fruit['lime'] = "A sour green citrus fruit."

    for a_key in fruit:
        print("{} -> {}".format(a_key, fruit[a_key]))

    # Changing the value for a key
    fruit['lime'] = "Great with tecquilla"
    print("*" * 100)

    for a_key in sorted(fruit):
        print("{} -> {}".format(a_key, fruit[a_key]))

    print("# " * 40)

    while True:
        f_find = input("Please enter the fruit you want me to find(Press Enter to exit) : ")
        if not f_find:
            break

        # So this is pretty much similar to what we did in dictionary
        # If key exists then return the value, if not then return some default value.
        print(fruit.get(f_find, "This does not exists!!!"))

    print("# " * 40)


print("*" * 100)
print(fruit)
print(type(fruit))
