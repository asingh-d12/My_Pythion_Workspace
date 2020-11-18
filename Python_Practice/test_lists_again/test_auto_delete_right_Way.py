# Remember this will work if values are sorted
# data = [4, 5, 103, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 186, 187, 191, 201, 320, 350, 360, 400]
# data = [4, 5, 103, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 186, 187, 191]
data = [4, 5, 201, 320, 350, 360, 400]

min_val = 100
max_val = 200

# This will contain the value where value is greater or equal to(in case of inclusive) min_val
stop = 0

for i, val in enumerate(data):
    if val >= min_val:
        stop = i
        break

# Now we know where the values that are smaller than min_val end at the beginning
# delete data from iterable outside of the list
del data[:stop]
print(data)

# Now working on removing values greater than max_val
# but let's not work through all the items till the end... in fact let's work from the end
start = 0
for i, val in enumerate(data[::-1]):
    if val < max_val:
        start = len(data) - i
        break


# Now we have index from which value in the list is greater than max_val
# Let's delete it as well
del data[start:]
print(data)
