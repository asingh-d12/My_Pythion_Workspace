# what if i actually WANT to change the global variable from inside local scope
# 1. NOT RECOMMENDED
# 2. In case of no choice, pass as value to function
# 3. Still we are gonna try, FOR THE SCIENCE... or something

x = "I am Global"


def report():
    # This is how I will access x in global scope
    global x

    print("Before upper in function = {}".format(x))
    # Now if i change x, it will affect the global x
    x = x.upper()

    print("After upper in function = {}".format(x))


print("In global scope before report function = {}".format(x))
report()
# If i print x in global scope
print("In global scope after report function = {}".format(x))
