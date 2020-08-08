"""
So, here we are going to read sample.txt that is present in the current
directory.

3 Steps involved:
1. open the file
2. read the file
3. close the file
"""

# We really don't need to provide 'r', as it is by default
jabber = open("./sample.txt", 'r')
for a_line in jabber:
    print(a_line)

print("*" * 50)

# We can do something like this as well
# Basically processing while reading the file
# Once you are done reading a file, you can read again because pointer is
# reached the end of this file.
# So, using seek() function to go back at the beginning of the file.
jabber.seek(0)
for a_line in jabber:
    if "jabberwock" in a_line.lower():
        # Using strip to remove '\n' at the end of the line
        # Mainly bacause print already provides a '\n' once a line is printed
        print(a_line.strip())

# Close the file, if not closed, it can cause file corruption
jabber.close()
