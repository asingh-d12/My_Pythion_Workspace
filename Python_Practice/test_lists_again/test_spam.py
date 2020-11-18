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
    if 'spam' in a_meal:
        for index, item in enumerate(a_meal[::-1]):
            if item == "spam":
                del a_meal[len(a_meal) - index - 1]
    print(a_meal)

print(".".join("Hello World"))

panagram = "The quick brown fox jumps over the lazy dog"
print(panagram.split())
