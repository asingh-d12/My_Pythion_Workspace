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

for a_meal in menu:
    a_spamless_meal = []
    if "spam" in a_meal:
        for item in a_meal:
            if item != "spam":
                a_spamless_meal.append(item)
        print(a_spamless_meal)
    else:
        print(a_meal)


print("*" * 50)

for a_meal in menu:
    if "spam" in a_meal:
        for i in range(len(a_meal) - 1, -1, -1):
            if a_meal[i] == "spam":
                del a_meal[i]
    print(a_meal)

print("*" * 50)

for a_meal in menu:
    for item in a_meal:
        if item != "spam":
            print(item, end=',')
    print()
