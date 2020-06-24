the_str = ""
print(the_str)
print(the_str[1:])
print(the_str[:5])
print(the_str[-4:])

# So this is something odd
# I gave an empty string and all the slices are just returning empty string
# let's try 1 more thing
print("Some more odd slices:")
print(the_str[4:5])
print(the_str[4:100:2])

# Still empty strings, no errors at all
