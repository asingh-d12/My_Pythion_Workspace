# Here we create a dictionary
fruit = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": "a sour, green citrus fruit",
    "apple": "round and crunchy"
}

# Printing a dictionary
print(fruit)

# Printing a value in dictionary using a key
print(fruit['orange'])

print("*" * 100)

# Adding an new entry to the dictionary
fruit["pear"] = "an oddly shaped apple"
print(fruit)

print("*" * 100)

# Updating value in a key already present
fruit["lime"] = "great with tequila"
print(fruit)

print("*" * 100)

# Deleting one of key-value pairs using del command
del fruit["lemon"]
print(fruit)

print("*" * 100)

# Deleting whole dictionary by mistake
# del fruit
# print(fruit)

# # Clearing the dictionary
# fruit.clear()
# print(fruit)

# print(fruit['tomato'])

# Creating a code snippet where key is asked from user and then value is displayed if key exists
while True:
    key_enter = input("What is the fruit you want to check(Just Press Enter to exit) : ")
    if not key_enter:
        break
    # There can be several ways actually
    # Method 1:
    # print(fruit.get(key_enter)) # This gives none if key doesn't exist
    # But this will say something if key doesn't exist
    # print(fruit.get(key_enter, "Key doesn't exists!!"))
    # Method 2
    # if key_enter in fruit:
    #     print(fruit[key_enter])
    # else:
    #     print("This key does not exists")
    # Method 3: We can also use this way - Short Circuiting
    (key_enter in fruit) and print(fruit[key_enter])

print("*" * 100)

# Accessing dictionary key-value pairs the pythonic way
for a_key in fruit:
    print("{} -> {}".format(a_key, fruit[a_key]))

print("*" * 100)

# Maintaining the order of the keys
for a_key in sorted(fruit):
    print("{} -> {}".format(a_key, fruit[a_key]))

print("*" * 100)

# Checking methods keys(), values and items()
print(fruit.keys())
print(fruit.values())
print(fruit.items())
