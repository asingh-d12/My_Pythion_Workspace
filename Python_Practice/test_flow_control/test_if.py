name = input("Please enter your name : ")
age = int(input("How old are you {} : ".format(name)))

print("{}, you are {}yrs old".format(name, age))

if age >= 18:
    # This whole block will be executed if the if statement is true
    print("You are old enough to Vote!!")
    print("Please put an X in the box!!")

else:
    print("Please come back in {} yrs".format(18 - age))

# What if we want to add a condition that checks if age is a certain value > 18
# Say age is >60, and we want to provide special transport for the users who wish to vote

# In that case we can not the code below age>=18... because that will contain >60 as well
# So we need to add >60 condition first as this is a subset of condition >=18

print("*" * 80)

if age > 60:
    print("You are old enough to Vote!!")
    print("Please put an X in the box!!")
    print("We will provide special transport for you if you want it!!")
elif age >= 18:
    print("You are old enough to Vote!!")
    print("Please put an X in the box!!")
else:
    print("Please come back in {} yrs".format(18 - age))

