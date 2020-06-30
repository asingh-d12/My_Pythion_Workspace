my_age = int(input("What is your age : "))

print("Using AND")
# if my_age >= 17 and my_age <= 65:
if 17 <= my_age <= 65:
    print("Have a good day at work.")
else:
    print("No work for you.")

print("*" * 50)

print("Using OR")
if my_age <= 16 or my_age > 65:
    print("No Work for you.")
else:
    print("Have a good day at work.")
