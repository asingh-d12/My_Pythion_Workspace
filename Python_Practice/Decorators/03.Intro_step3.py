# Here we are trying to understand step-by-step how decorator works?

# 03. Returning a function


def say_hello(name="Amrit"):
    print("I am inside say_hello() function")

    # 02b. inside the say_hello() function, let's create another function greet
    def greet():
        return "\tThis is inside greet()"

    # Let's create yet another function
    def welcome():
        return "\tThis is inside welcome()"

    # 03. Let's return function here
    if name == "Amrit":
        return greet
    else:
        return welcome


# Calling this function
x = say_hello(name="Singh")
# x is the variable which will bind to the returned function from say_hello()
# function
# Since, say_hello is returning the function itself and not the executed
# function result... we can execute it ourself
print(x())
