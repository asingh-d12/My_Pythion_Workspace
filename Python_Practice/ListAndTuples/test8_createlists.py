# All the ways to create lists
# 1. list literal
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
empty_list = []

print("*" * 100)

# 2. Concatenating to create a list
numbers = even + odd
# or
still_even = even + empty_list
print(numbers)
print(still_even)
print(id(still_even) == id(even))

print("*" * 100)

# 3. function to create a list
# 3a. sorted() function - it will take any iterable object, and
# new list will be created after sorted is done with
# that iterable
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
digits = sorted("4321569780")
print(digits)
print("*" * 100)

# 3b. list() - another function that can help creating the list
# requires an iterable
# check it out
# Main reason to use list() -> to create a copy of the list
a_list = [1, 4, 1, 5, 1, 4]
b_list = list(a_list)
print(b_list)
print(id(a_list) == id(b_list))
a_str = "Amrit"
amrit_list = list(a_str)
print(a_str)

print("*" * 100)

# 4. Use Slices
# This also can be used to create copy of a list
a_list = [1, 4, 1, 5, 1, 4]
b_list = a_list[:]
print(b_list)
print("Are the contents equal = {}".format(a_list == b_list))
print("Are both the same list = {}".format(a_list is b_list))

# 5. .copy() method in list
a_list = [1, 4, 1, 5, 1, 4]
b_list = a_list.copy()
