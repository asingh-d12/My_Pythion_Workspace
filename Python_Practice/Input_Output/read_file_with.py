# Reading file using with statement
with open('./sample.txt', 'r') as jabber:
    for a_line in jabber:
        if "jab" in a_line.lower():
            print(a_line.strip())

# The main advantage here, file is closed automatically
# Even if there is an error, and program is going to be terminated,
# with still makes sure to close the file, before program terminates due to
# error.
