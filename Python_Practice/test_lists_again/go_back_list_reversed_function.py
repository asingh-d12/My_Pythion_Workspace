data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
min_val = 100
max_val = 200

for index, val in enumerate(reversed(data)):
    print("{} -> {}".format(index, val))

# So basically, it is simply producing a new list that is reversed of original
# So how to delete the items from it

print("*" * 100)

for index, val in enumerate(reversed(data)):
    if val < min_val or val > max_val:
        del data[len(data) - index - 1]

print(data)
