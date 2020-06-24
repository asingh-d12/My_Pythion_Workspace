alphabets = "abcdefghijklmnopqrstuvwxyz"
print("All the alphabets = {}".format(alphabets))
print("All the alphabets printed backwards using slicing = {}".format(alphabets[25::-1]))

print("*" * 100)
print("Awesome!!, this can easily reverse the String...")
my_name = "Amritpal Singh"
print("'{}' reverses to '{}'".format(my_name, my_name[::-1]))

print("*" * 100)
print("Let's check this out, as this should not print anything")
print(alphabets[20:-1:-1])
print("Why not print anything??")
print("Because here 20 is to the left of -1, and with -1 as step, we are trying to move from right to left... so this is not possible")
print("This on the other hand...")
print(alphabets[-1:20:-1])
print("...should work")