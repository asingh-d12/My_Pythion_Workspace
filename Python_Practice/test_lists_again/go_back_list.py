data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
min_val = 100
max_val = 200

for index in range(len(data) - 1, -1, -1):
    # This will print range backwards
    if data[index] < min_val or data[index] > max_val:
        print(index)
        del data[index]

# Why would this work?
# Let's say we delete index 10 in list of 12 items
# This won't affect our iterating over it... why?
# Because we have already iterated over list that is after index 10... since we are iterating backwards
# index before index 10... remains the same if we delete index 10

# Therefore an awesome technique
# Not to mention... NO SORT REQUIRED

print(data)

