# The main difference between this program and for_loop_2.py is that here we are going to as user to input number

number = input("Please enter a series of numbers with any separator you like : ")
separators = ""

for a_char in number:
    # We can do something like this as well.
    # if not a_char.isnumeric():
    if a_char not in "1234567890":
        separators += a_char

print(separators)

final_op = ''.join([x if x not in separators else ' ' for x in number]).split()
print(final_op)
print([int(x) for x in final_op])
