with open("binary_file", 'wb') as bin_file:
    for i in range(17):
        # bytes() function actually takes an iterable to do what we want
        # If it takes an int, it will create a byte array of length i,
        # and all characters as 0
        # That's why we are first converting our i to a list and then
        # converting to bytes
        bin_file.write(bytes([i]))

with open("binary_file", 'rb') as bin_file_1:
    for b in bin_file_1:
        print(b)
