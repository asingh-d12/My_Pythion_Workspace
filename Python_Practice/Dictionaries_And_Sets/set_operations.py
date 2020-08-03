# So, since we have sets, we also have a couple of set operations.
# Let's take a look

even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

print("*" * 100)

# Now let's run UNION
# .union() method returns the union set, without affecting the original sets
print(even.union(squares))
print(len(even.union(squares)))
# The result will be same if we call method on squares
print(squares.union(even))
print(len(squares.union(even)))
# After union
print(even)
print(squares)

print("*" * 100)

# Let's talk about intersect now
print(even.intersection(squares))
print(squares.intersection(even))
# Oh and to intersect we can use & as well
print(squares & even)
# Same as .union(), .intersection() method returns the intersected set, without affecting the original
print(even)
print(squares)

print("*" * 100)

# Set Subtraction
# Subtracting set_b from set_a will remove any items that are in set_b from set_a
# Basically means set_a - set_a.intersection(set_b)
# Same is true for vice versa, if we subtract set_a from set_b
# this uses .difference() method
print(even.difference(squares))
# As you can see in output, 4 and 16 are missing
# If we do opposite way
print(squares.difference(even))
# We can do difference using - as well
print(squares - even)
print(even - squares)
# As, like in .union() and intersection() method, it doesn't affect original sets
print(even)
print(squares)

print("*" * 100)

# Next, subset and superset
# Let's check if a set is subset or superset of another set
even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 16, 36)
squares = set(squares_tuple)
print(squares)
print(len(squares))

# Here, I am checking if squares is subset of even, it will print true or false
print(squares.issubset(even))
# Here, I am checking if even is subset of squares, it will print true or false
print(even.issubset(squares))

# We can also do something like this
if even.issuperset(squares):
    print("Even is superset to squares!!")
else:
    print("Even is not superset to squares!!")
