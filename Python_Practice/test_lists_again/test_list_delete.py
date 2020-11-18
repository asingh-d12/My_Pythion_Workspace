# How to remove from list using slices
data = [4, 5, 103, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 188, 187, 191, 350, 360]
# So we are seeing that in the data observed above 1st 2 elements in the list are outliers
# so, how to delete them at once
print("Data before deletion of 1st 2 elements = {}".format(data))
del data[0:2]
print("Data after deletion of 1st 2 elements = {}".format(data))

# Last 2 also looks somewhat out of range
# it won't work if we use index from 0 to len-1.. because of the elements we already deleted
# instead let's use reverse index
del data[-2:]
print("Data after deletion of last 2 elements = {}".format(data))
