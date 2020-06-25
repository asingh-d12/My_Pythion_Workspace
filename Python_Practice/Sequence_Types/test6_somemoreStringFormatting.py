import math

for i in range(1,  13):
    # :2, :3 and :4 refers to the number of spaces the output will take
    # We can simply add 0 infront of number of spaces for 0 formatting
    # :02, :03 and :04
    # We can also use symbol '<' to do left alignment, instead of default right alignment
    # lastly, we can use symbol '^' for center alignment as well
    # This is mainly in case of string formatting integer values
    print("Number = {:2}, Squared = {:<3}, Cubed = {:^4}".format(i, i**2, i**3))

print('*' * 100)

pi = 22/7
print("Value of pi without formatting = {}".format(pi))
print("Value of pi adding width of 50 = {:50}".format(pi))
print("Value of pi adding width of 50 with 0 = {:050}".format(pi))
print("Value of pi adding width of 50 left aligned = {:<50}".format(pi))
# So adding .<num>f after the width will provide us with the precision
# 50.3f means width of 50 with 3 precision
print("Value of pi adding width of 50 and precision of 3 = {:50.3f}".format(pi))
print("Value of pi adding width of 50 and precision of 3 = {:52.50f}".format(pi))
print("Value of pi adding width of 50 and precision of 3 = {:12.50f}".format(pi))
print("Value of pi adding width of 50 and precision of 3 = {:72.50f}".format(pi))
