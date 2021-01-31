# This is how a dictionary is created
fruits = {'orange': "a sweet orange, citrus fruit.",
          'apple': "good for making cider.",
          'lemon': "a sour yellow citrus fruit",
          'grape': "a small, sweet fruit growing in bunches",
          "lime": "a sour green, citrus fruit.",
          "apple": "round and crunchy"}

# Let's print this  dictionary
print(fruits)

# Now to access a particular element, let's use a key
print(fruits['apple'])
print(fruits['lime'])

print("*" * 80)

# Let's add something to this dictionary
fruits['pear'] = "an odd shaped apple."
print("After adding a new key-value pair:\n{}".format(fruits))

print("*" * 80)
# Now let's try updating a key
print("Fruits dictionary before update:\n{}".format(fruits))
fruits['lime'] = 'great with tequila'
print("Fruits dictionary after update:\n{}".format(fruits))

print("*" * 80)
# Now, deleting a key-value pair in dictionary
print("Fruits dictionary before deleting:\n{}".format(fruits))
del fruits["grape"]
print("Fruits dictionary after deleting:\n{}".format(fruits))

# print("*" * 80)
# # Clearing the dictionary completely, but not deleting it
# print("Fruits dictionary before clearing:\n{}".format(fruits))
# fruits.clear()
# print("Fruits dictionary after cleaaring:\n{}".format(fruits))

print("*" * 80)
# Trying to access key-value pair that don't exist - This gives KeyError as tomato is not a key
# print(fruits["tomato"])

print("*" * 80)
# This code from here will ask user to enter the name of the fruit, and print the value present in the dictionary
while True:
    ch = input("Enter the fruit you want to search(0 to exit) : ")
    if ch == '0':
        break

    # # What if they key is not present in the dictionary
    # # This is the first way to handle it
    # if ch in fruits:
    #     print("The fruit you asked for {} = {}".format(ch, fruits[ch]))
    # else:
    #     print("This fruit {} is not present, try again...".format(ch))

    # This is the second way to handle it - use get() method
    # But currently i will only get None as value, if they key is not present
    print(fruits.get(ch, "{} not found in the dictionary".format(ch)))

print("*" * 80)
# This code will iterate over the Dictionary
print("Let's iterate over the dictionary fruits.")
for snack in fruits:
    print("{} -> {}".format(snack, fruits[snack]))

print("*" * 80)
# This code will iterate over the Dictionary, with keys in sorted order
print("Let's iterate over the dictionary fruits in sorted order.")
for fruit in sorted(fruits):
    print("{} -> {}".format(fruit, fruits[fruit]))

print("*" * 80)
# Checking here keys() and values() methods
fruit_keys = fruits.keys()
print("This is keys method -> {}\nThis is of type -> {}\n".format(fruit_keys, type(fruit_keys)))
fruit_values = fruits.values()
print("This is values method -> {}\nThis is of type -> {}".format(fruit_values, type(fruit_values)))

print("\nUpdating the dictionary and then printing keys and values again")
fruits['grape'] = "a small, round, sweet fruit growing in bunches"
print("This is keys method -> {}\nThis is of type -> {}\n".format(fruit_keys, type(fruit_keys)))
print("This is values method -> {}\nThis is of type -> {}".format(fruit_values, type(fruit_values)))

print("*" * 80)
# Checking out items() method now
fruit_items = fruits.items()
print("This is items method -> {}\nThis is of type -> {}\n".format(fruit_items, type(fruit_items)))

# We can do something like this as well since basically this is a list of tuples
for fruit_key, fruit_value in fruit_items:
    print("{} -> {}".format(fruit_key, fruit_value))
