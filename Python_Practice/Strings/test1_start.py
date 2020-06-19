# Position goes something like this
# 				   1
# 		 01234567890123456
a_str = "Python is Awesome"
#               1		 -
# 		 76543210987654321
#  or something like this in -ve from right to left
print("Here the string mentioned above is formed by sequence of characters")
print(a_str)

print('*' * 50)
print("We can iterate over it")
for a_char in a_str:
    print(a_char)

print('*' * 50)

print("It is subscriptable, either is +ve way from left to right")
print(a_str[2])
print(a_str[3])
print()
print("or in -ve way from right to left")
print(a_str[-10])  # should print i
print(a_str[-6])   # should print w