# Let's start with how to create tuples
# 1. Tuple Literal - Part 1
t = "a", "b", "c"
# This is a tuple
print(t)

# 2. Tuple Literal - with parantheses
t1 = ("a", "b", "c")
print(t1)

# The output from both are basically the same
# But sometimes it is important to use parantheses
# Check out this example
x = 1
y = 2
# This prints x, y and then a tuple that contains (1, 2
print(x, y, (1, 2))  # 1
# What if we print x, y, 1, 2
print(x, y, 1, 2)  # 2

# As you can see
# 1 - prints a tuple
# 2 - does not print tuple, even if we think 1, 2 should be a tuple
