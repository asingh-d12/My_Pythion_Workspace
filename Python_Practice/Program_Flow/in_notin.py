your_str = "Amritpal Singh"

ch = input("Enter the character to check : ")

if ch in your_str:
    print("Character '{}' is present in {}".format(ch, your_str))
else:
    print("Character '{}' is not present in {}".format(ch, your_str))

print('*' * 100)
print("Checking not in...")

your_input = input("What do you want to do today? : ")
# There is 1 small issue.. what if i entered this
# I WANT TO LEARN PYTHON
# The below condition will pass, but it shouldn't... but due to case sensitivity it passes... what to do?
# Use lower() or better yet(for other country keyboard purposes) use casefold()
if "python" not in your_input.casefold():
    print("But I want to learn python!!")
