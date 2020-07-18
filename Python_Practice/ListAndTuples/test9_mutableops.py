# Starting with what we can do with lists
a_list = ["Amrit",
          "Lucky",
          "Ravi",
          "Singh"
          ]

# 1. replacing a single item
print(a_list)
a_list[1] = "Jupnit"
print(a_list)

print("*" * 50)

# 2. Replacing multiple items through slices
# Remember, here an iterable is required
# Basically anything you bind the values to needs to be iterable, whether it be string or a list
a_list[1:3] = ["Lucky", "Ravinder"]
print(a_list)
print("*" * 50)
# An odd example
a_list[2:3] = "Lucky"
print(a_list)
