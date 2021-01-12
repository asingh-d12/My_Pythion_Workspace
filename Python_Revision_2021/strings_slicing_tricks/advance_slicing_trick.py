# This is an advanced slicing trick that can help us extracting numbers from any sort of delimiter separated numbers
# in form of a String

# Check this out, this is string containing numbers
numbers = "1, 2,    3,    4,   512,;;.?   625"

# Step 1: Extract all the delimiters
delimiters = ""
for x in numbers:
    if not x.isnumeric():
        delimiters += x

print("All the delimiters in a single string = {}".format(delimiters))

# Step 2: get the numbers separated by delimiters
final_numbers = ''.join([x if x not in delimiters else ' ' for x in numbers]).split()
final_numbers = [int(num) for num in final_numbers]
print("Final numbers in the form of a list = {}".format(final_numbers))

# This is very robust, and the main trick is the fact that
# 1 or more spaces are considered as white string for split function to split
