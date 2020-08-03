# Created a set containing farm animals, using set literal
farm_animals = {"sheep", "cow", "hen"}

print(farm_animals)

# Sets are iterable, so let's iterate over it using for
for animal in farm_animals:
    print(animal)

print("*" * 100)

# Second way to create set, from an iterable
wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

print("*" * 100)

# But this not an empty set
not_an_empty_set = {}
print(type(not_an_empty_set))
# Yup, you guessed it ... it is a dictionary
# So, what if we want to create an empty set
empty_set = set()
print(type(empty_set))

print("*" * 100)
# Adding elements to set
farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)
