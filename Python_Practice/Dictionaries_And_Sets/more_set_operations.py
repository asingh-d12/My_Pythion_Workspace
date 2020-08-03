# We are going to run the same set operations as we did in previous code, but with 1 difference
# Here the original set on which the method is called will not remain the same
even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

print("*" * 100)

# Difference using difference_update method
print(squares.difference_update(even))
# This will print none
# After .difference_update() is called
print(even)
print(squares)

print("*" * 100)

# What is Symmetric Difference?
# Let's check out
even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

# So, basically symmetric difference is same no matter how you take it
# Basically it is (set_a union set_b) - (set_a intersect set_b)
print(even.symmetric_difference(squares))
print(squares.symmetric_difference(even))
# Symmetric difference can be done with ^ - though no change as compared to use the method
print(even ^ squares)

