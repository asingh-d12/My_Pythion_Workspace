# If I take the code that i ran for continue
# and replace continue with Break
# What will happen?

shop_list = ["processor", "RAM", "SSD", "Power Supply", "Motherboard", "Keyboard", "Monitor"]

for an_item in shop_list:
    if an_item == "Keyboard":
        break
    print("You have to buy {}".format(an_item))

# So it seems anything in the list after we break is skipped
# So, basically we come out of loop all together

print('*' * 100)
item_to_search = "DVD Drive"

# What we have to do is:
# 1. Search for the item mentioned in the list above.
# 2. If found print the index and come out of the loop
# 3. If not print -1

found_at = None

for index in range(len(shop_list)):
    if shop_list[index] == item_to_search:
        found_at = index
        break
print("Item Found @ Position {}".format(found_at))
