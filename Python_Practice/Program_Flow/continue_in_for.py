shop_list = ["processor", "RAM", "SSD", "Power Supply", "Motherboard", "Keyboard", "Monitor"]

for an_item in shop_list:
    print("You have to buy {}".format(an_item))

print("*" * 100)
# What if I don't to buy Keyboard, how to exclude it

for an_item in shop_list:
    if an_item != "Keyboard":
        print("You have to buy {}".format(an_item))

print("*" * 100)
# We can also do this using 'continue'
# Basically it will skip where we encounter continue to next iteration
for an_item in shop_list:
    if an_item == "Keyboard":
        continue
    print("You have to buy {}".format(an_item))
