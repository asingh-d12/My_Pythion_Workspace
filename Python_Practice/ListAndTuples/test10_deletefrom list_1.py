# Let's check out how to delete from list
a_list = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
          170, 183, 185, 187, 188, 191, 350, 360]
print(a_list)
print("*" * 100)

# Delete first 2 values from the list
print("Delete first 2 values from the list")
del a_list[0:2]
print(a_list)

print("*" * 100)
# Delete last 2 items as well
print("Delete last 2 items as well")
del a_list[-2:]
print(a_list)
