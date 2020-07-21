# So this is a simple splitting, where we are not giving any argument in .split() method
# Argument here is suppose to be the delimiter by which we are splitting the string
# By default it takes any whitespace as delimiter
a_str = "My name is amrit"
print(a_str.split())

a_str = "My\nname\nis\namrit"
print(a_str.split())

# If more than 1 whitespaces are present
# In that case empty strings are expected
# but these empty strings are ignored
a_str = "My\n\tname\nis\n amrit"
print(a_str.split())

# Let's talk about line from csv file
# say it is info about some user,age,nationality,hobbies
a_csv_line = "Amrit,30,Indian,Reading:Playing Games:Watching Movies"
# By use of split method, we can do something like this
# Check out the argument here.. we want to split by ','
name, age, nationality, hobbies = a_csv_line.split(',')
print("Details:\n\tName:{}\n\tAge:{}\n\tNationality:{}\n\tHobbies:{}".format(name, age, nationality, hobbies.split(':')))

print("*" * 50)

# Remember this old challenge code, here this approach prints each element individiually
# But, since we don't want new line between items in a single meal list, we used end keyword argument

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# Though this is fine, the only thing that looks kinda tacky is ',' after the last string
for a_meal in menu:
    for item in a_meal:
        if item != "spam":
            print(item, end=',')
    print()

print()

# So, can join() work
# Of course it can
# Check this out
for a_meal in menu:
    if "spam" not in a_meal:
        print(','.join(a_meal))
    else:
        print(','.join([item for item in a_meal if item != "spam"]))


print("*" * 100)
# A list with an int in it
# If we try join on it, it will fail
# a_list = ['My', 'name', 'is', 'amrit', 30]
# print(' '.join(a_list))
