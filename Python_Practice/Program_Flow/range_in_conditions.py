my_age = int(input("What is your age : "))

# if my_age >= 17 and my_age <= 65:
# if 17 <= my_age <= 65:
# Even though the above mentioned method is most efficient
# For the purpose of learning, let's try the above mentioned condition with a range.
if my_age in range(17, 66):
    print("Have a good day at work.")
else:
    print("No work for you.")
