even_set = set(range(0, 40, 2))
print(even_set)

# 2 main methods to remove elements from the set
# 1. discard() method
print(even_set.discard(2))
# getting None as discard method returns None
# After removing 2
print(even_set)
# 2 is removed
# Trying to remove 2 again
print(even_set.discard(2))

print("*" * 100)

# 2. remove() method
print(even_set.remove(8))
# remove() method returns None as well
# printing set after removing
print(even_set)
# Trying to remove same element again
# print(even_set.remove(8))
# Here we will see error, when we try to remove same element again

print("*" * 100)

# Moral of the story, always check if an element is present before trying to remove it.. whether use discard or
# remove...
elem = int(input("What is it you want to remove? : "))
print("You asked to remove {}.".format(elem))
print("Checking if this element is present first...")
if elem in even_set:
    print("Found and Removing {}".format(4))
    even_set.remove(elem)
else:
    print("{} is not present in the set.".format(elem))
print(even_set)
