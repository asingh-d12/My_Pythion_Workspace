# Let's check out how to delete from list
# a_list = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
#           170, 183, 185, 187, 188, 191, 350, 360]
# print(a_list)
# print("*" * 100)

# Delete numbers that are not between a min and max value
# min_val = 100
# max_val = 200
#
# for index, val in enumerate(a_list):
#     if not min_val < val < max_val:
#         del a_list[index]
#
# print(a_list)

# This is not correct as seen in the output
# basically whenever you delete on a same mutable data structure that you are iterating over
# you are bound to face issues like these

# print("*" * 100)

# How to correctly do this::
# a_list = [104, 105, 110, 120, 130, 130, 150, 160,
#           170, 183, 185, 187, 188, 191]

a_list = list(range(1, 99, 3)) + list(range(1021, 2000, 100))

# a_list = []

min_val = 100
max_val = 200

i = 0
print(a_list)
while i < len(a_list):
    if not min_val < a_list[i] < max_val:
        del a_list[i]
        i -= 1
    i += 1

print(a_list)
