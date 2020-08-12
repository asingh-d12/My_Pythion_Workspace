import shelve

# Shelves are opened in read and write mode by default. So no need to specify.
with shelve.open('shelftest') as fruit:
    fruit['orange'] = "a sweet orange citrus fruit."
    fruit['apple'] = "good from making cider."
    fruit['lemon'] = "a sour yellow citrus fruit.."
    fruit['grape'] = "a small, sweet fruit growing in bunches."
    fruit['lime'] = "A sour green citrus fruit."

    print(fruit["lemon"])
    print(fruit["grape"])

    # Once a Shelve is opened, it can be pretty much be used like a dictionary.
    # Though there is no Shelve Literal, so we can not create a shelve like we create a dictionary
print(fruit)
print(type(fruit))
