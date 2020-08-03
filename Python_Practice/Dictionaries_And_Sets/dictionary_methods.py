fruit = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": "a sour, green citrus fruit",
}

print(fruit)

veg = {"cabbage": "flowery vegetable, does anybody like to eat it",
       "sprouts": "Good for health",
       "spinach": "What can i say, other than ... 'Popeye the sailor man'"
       }

print(veg)

print("*" * 100)

# How is update method used?
# Combine the 2 above mentioned dictionaries together
# call the method on 1 dictionary, while using the other as an argument
print(fruit.update(veg))
# This will add veg contents to fruit... while veg will remain same, but The method returns none
# After update
print(fruit)
print(veg)

# We can also have done veg.update(fruit).. it will just do the opposite

print("*" * 100)

fruit = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": "a sour, green citrus fruit",
}

print(fruit)

veg = {"cabbage": "flowery vegetable, does anybody like to eat it",
       "sprouts": "Good for health",
       "spinach": "What can i say, other than ... 'Popeye the sailor man'"
       }

print(veg)
print("*" * 100)
# How is copy method used?
# So, we don't to update our dictionary but want to create a new dictionary from the dictionaries we have
# First, let's create a copy of 1 dictionary
fruit_and_veg = fruit.copy()
# Now let's update another to this one
fruit_and_veg.update(veg)
print(fruit)
print(veg)
# fruit_and_veg is separate dictionary from fruit and veg dictionaries
print(fruit_and_veg)
