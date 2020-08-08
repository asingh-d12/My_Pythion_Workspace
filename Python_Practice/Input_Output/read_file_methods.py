# Now, we are going to use methods to read a text file
# Let's check these methods out

with open("./sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line.strip())
        line = jabber.readline()

# So, basically readline().. reads a single line at a time
# Once at the end line, will be empty and loop will break

print("*" * 50)

# We can not only readline() we can also readlines()... to read all lines at
# once... check it out
with open("./sample.txt", 'r') as jabber:
    lines = jabber.readlines()
    # Lines is an object of type list
    print(type(lines))
    for a_line in lines:
        print(a_line.strip())


print("*" * 50)
# Finally, let's talk about just read()
# It reads whole file as a string, and that is it
with open("./sample.txt", 'r') as jabber:
    whole_file_as_string = jabber.read()
    print(type(whole_file_as_string))
    print(len(whole_file_as_string))
    print(whole_file_as_string)
