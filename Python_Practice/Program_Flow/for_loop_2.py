number = "9,223;372:036 854,775;807"
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
