pi = 22/7
print("Value of pi without formatting = {}".format(pi))
print("Value of pi adding width of 50 = {:50}".format(pi))
print("Value of pi adding width of 50 with 0 = {:050}".format(pi))
print("Value of pi adding width of 50 left aligned = {:<50}".format(pi))
# So adding .<num>f after the width will provide us with the precision
# 50.3f means width of 50 with 3 precision
print("Value of pi adding width of 50 and precision of 3 = {:50.3f}".format(pi))
print("Value of pi adding width of 50 and precision of 30 = {:50.30f}".format(pi))
# remember if precision is higher than width, precision always trumps width, example being :12.50f
# Also, as can be seen the in the example :55.54f, the precision is 54 but pi has precision of
# 51 only and so it adds 0 instead of space for remaining precision values
print("Value of pi adding width of 55 and precision of 54 = {:55.54f}".format(pi))
print("Value of pi adding width of 52 and precision of 50 = {:52.50f}".format(pi))
print("Value of pi adding width of 12 and precision of 50 = {:12.50f}".format(pi))
print("Value of pi adding width of 70 and precision of 50 = {:72.50f}".format(pi))

# To Conclude:
# If the width provided is more than what the actual printed variable can use, it prints ' ' by default.
# If the precision provided is more than what the actual printed variable can use, it prints '0' by default.