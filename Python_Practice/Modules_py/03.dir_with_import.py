import shelve

# Let's check what all is present in shelve module
print(dir(shelve))

print("*" * 50)
# We can also go 1 level down...
# Say we want to check what are the methods/variables in Class Shelf inside
# module shelve
print(dir(shelve.Shelf))
