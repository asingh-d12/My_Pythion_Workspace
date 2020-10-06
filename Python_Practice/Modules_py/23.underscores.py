# A single underscore as a variable
details = ("Amrit", 29, "India")
# Now we are doing tuple unpacking, but we don't need middle value
name, _, age = details
print(name, age)
