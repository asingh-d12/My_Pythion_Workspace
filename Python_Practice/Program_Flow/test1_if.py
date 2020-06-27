name = input("What is your name? : ")
# Remember age is supposed to be int, so let's convert age to int using int() function
age = int(input("How old are you {}? : ".format(name)))
# Remember, that if you try to enter any value other than an int in age, when python tries to convert age to int, it will throw ValueError
print("{}, you are {} yrs old.".format(name, age))

# Now, we are going to check a condition using if statement
# Basically, we are going to check if the person is old enough to vote.
# This will be on basis of condition that will added on age
if age >= 65:
    print("{}, You are eligible for Older Citizen Voting Facility.".format(name))
    print("Your date time slot is as follows:2020-06-29 12:12:45 PM.")
elif age >= 18:
    print("{}. you are eligible to vote.".format(name))
else:
    # So, basically this is else block, kind of catch all in case no condition passes this block is executed
    print("{}, please come back in {} years.".format(name, (18-age)))

# Now if you note above if-elif-else, you can see that the condition if person is > 65 is checked first
# Then it is checked if person is aged > 18
# last is else
# Why can't we check first for >18.... It's obvious...
# Basically 65 is also > 18, so if a person age >= 65, for him/her as well the >18 code block will execute
# and in if-elif-else, once 1 code block executes control goes back to outside
# So, keep in mind to always check narrower condition first before more broader one
