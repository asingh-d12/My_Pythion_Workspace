numbers = (1, 2, 3, 4, 5)

print("This is a simple tuple = {}".format(numbers))
print("This is a simple tuple, but let's add * before it")
print(*numbers)

# What did print function actually gets when we call *numbers
# something like this
print(1, 2, 3, 4, 5)

print("*" * 100)

# Let's try one more thing
print("Let's change the separator in print function from default ' ' to ';'")
print("Directly printing numbers")
print(numbers, sep=';')
print("This is a simple tuple, but let's add * before it")
print(*numbers, sep=';')

# What did print function actually gets when we call *numbers
# something like this
print(1, 2, 3, 4, 5, sep=';')

print("*" * 100)

# So as we understand it *numbers or *args is actually used to unpack the iterable
numbers = [1, 2, 3, 4, 5, 6]
print(*numbers, sep=',')

print("*" * 100)

# but we usually don't use * this way, in fact we use it in completely opposite way
# i.e. we tell that what we are getting is an unpacked sequence and then we pack it back to become an iterable
# Let's check this out


def test_star_args(*args):
    print(args)
    for i in args:
        print(i)


test_star_args(1, 2, 3, 4, 5, 6, 7, 8)
# So basically all the values we are giving in this function are packed in a single tuple
# No matter how many values we give
test_star_args(1, 2, 3, 4)
test_star_args()

# Basically, if *args represents an unpacked tuple, then args represent a tuple
