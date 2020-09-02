# This is Global Scope x
# Until and Unless we explicitly try changing it inside the functions,
# it will never change inside the function
x = "I am outside the func"


def report():
    x = "I am inside the func"
    return x


# What will be printed here.. will it be the x from outside or inside
print(x)
# Of course the one that is outside will be printed
# But how we know that?
# Because x inside the function is the local variable that is inside the
# function

print("*" * 100)
# What if I do this
print(report())
print(x)
# This will print inside x when function is called
# But, when x is printed, it will still be outside one

print("*" * 100)
