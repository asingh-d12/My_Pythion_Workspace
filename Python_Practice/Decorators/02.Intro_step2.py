# Here we are trying to understand step-by-step how decorator works?

# 02a. Adding argument to simple say_hello() function


def say_hello(name="Amrit"):
    print("I am inside say_hello() function")

    # 02b. inside the say_hello() function, let's create another function greet
    def greet():
        return "\tThis is inside greet()"

    # Let's create yet another function
    def welcome():
        return "\tThis is inside welcome()"

    # Now, calling greet inside say_hello() function
    print(greet())
    print(welcome())


# Calling this function
say_hello()
