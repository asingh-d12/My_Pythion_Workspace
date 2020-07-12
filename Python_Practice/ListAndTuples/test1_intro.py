# 1. Create a very simple list
computer_parts = ["computer",
                  "mouse",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

# 2. Iterate over this list using for loop, and print each item in style
for a_comp_part in computer_parts:
    print("So, I got \"{}\""
          " in my computer".format(a_comp_part))

print("*" * 50)

# 3. Since a List is a "Sequence Type", we can actually use an index as well
print("I am more of a Mechanical {} guy".format(computer_parts[2].title()))

print("*" * 50)
# 4. OfCourse similar to string, and because it is a sequence type,
# you can slice a list as well
print(computer_parts[1:3])
