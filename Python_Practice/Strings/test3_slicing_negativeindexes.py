a_str = "Python is awesome!!"
# the syntax is something like this
# This is most basic one
print("1. Most Basic -> <string>[-start:end] or <string>[start:-end] or <string>[-start:-end]--> end char is not included")
print("Everything is same as positive indexes, except making sure -ve index are provided properly as we are going from left to right '-->' ")
print(a_str[-9:-2])
print(a_str[-4:18])
print(a_str[:-1])

print()
print('*' * 50)
print("2. No Start Value Provided")
print(a_str[:-5])
print(a_str[:-1])
print(a_str[:-15])
print("Basically means start from 'start' or 0")

print()
print('*' * 50)
print("3. No End Value Provided -> <string>[start:]")
print(a_str[-5:])
print(a_str[-9:])
print(a_str[-1:])
print(a_str[-17:])
print("Basically means go till end")

print()
print('*' * 50)
print("We can do something like this as well to print the whole string.. i know it's waste, but hold on!!")
print(a_str[:-8] + a_str[-8:])
print("or do this")
print(a_str[:])