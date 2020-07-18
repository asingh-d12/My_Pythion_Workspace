name = "Amrit"
age = 30
print(name, age, "hello", "2020")

print('*' * 50)
# what is sep in print function?
# A: It is a keyword argument that tells what 'sep'arator to use
# between various items printed in a single print statement.
# By default it is ' '
# Check this out
print(name, age, "hello", "2020", sep='; ')
# What will happen? this should print with "; " as a separator
# 1 more example
print(name, age, "hello", "2020", sep=':')

print("*" * 50)

# Next, what is end?
# Also another keyword argument with default value of '\n'
# Check out this code...
# with default value
print(name, age, "hello", "2020")
print(name, age, "hello", "2020")
# Changing end='; '
print(name, age, "hello", "2020", end='; ')
print(name, age, "hello", "2020")
