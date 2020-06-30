day = "Saturday"
temperature = 30
is_raining = False

if day == "Saturday" and temperature > 27 and not is_raining:
    print("Let's go outdoor swimming!!")
else:
    print("Let's play counter strike!!")

print('*' * 100)
print("Let's check out some of the values that are treated as false")

print(bool(0))
print(bool(''))
print(bool(' '))
print(bool(None))

print("PFB 1 of the use")
your_name = input("Please enter your name : ")
if your_name:
    print("Your Name = {}".format(your_name))
else:
    print("Please find your Birth Certificate.")
