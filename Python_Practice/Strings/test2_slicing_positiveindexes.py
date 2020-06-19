a_str = "Python is awesome!!"
# the syntax is something like this
# This is most basic one
print("1. Most Basic -> <string>[start:end] --> end char is not included")
print(a_str[3:5])
print(a_str[0:8])
print(a_str[1:9])
print(a_str[10:17])

print()
print('*' * 50)
print("2. No Start Value Provided -> <string>[:end]")
print(a_str[:5])
print(a_str[:8])
print(a_str[:9])
print("Basically means start from 'start' or 0")

print()
print('*' * 50)
print("3. No End Value Provided -> <string>[start:]")
print(a_str[5:])
print(a_str[8:])
print(a_str[1:])
print(a_str[0:])
print("Basically means go till last character")

print()
print('*' * 50)
print("We can do something like this as well to print the whole string.. i know it's waste, but hold on!!")
print(a_str[:6] + a_str[6:])
print("or do this")
print(a_str[:])