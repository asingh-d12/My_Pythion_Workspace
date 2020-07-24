num = int(input("Enter the number you want to convert to binary : "))
the_bin_num = 0
BIN_B = 2
OCT_B = 8
i = 0

divider = BIN_B

while num != 0:
    rem = num % divider
    the_bin_num = (10**i) * rem + the_bin_num
    num = num // divider
    i += 1

print(the_bin_num)
