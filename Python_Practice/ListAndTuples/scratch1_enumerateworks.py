# How does enumerate works
# Let's check out the help
# help(enumerate)

computer_parts = ["computer",
                  "mouse",
                  "keyboard",
                  "Monitor",
                  "mouse mat",
                  "HDMI Cable",
                  "DVD Drive"
                  ]

print("Regular List = {}".format(computer_parts))
print("*" * 50)
print("After enumerate is applied = {}".format(enumerate(computer_parts)))
# So Enumerate Returns an Object, let's see if this works
print("converting enumerate object to list = {}".format(list(enumerate(computer_parts))))
# So, as it can be seen... it is (index, part)...

print("*" * 100)
# We can do the same with the String as well... basically any Iterable
a_str = "Hello, World"
for index, character in enumerate(a_str):
    print("{} -> {}".format(index, character))

print("*" * 50)
# Let's try with an unordered iterable - a set
a_set = {1, 2, 3, 4}
for index, num in enumerate(a_set):
    print("{} -> {}".format(index, num))
