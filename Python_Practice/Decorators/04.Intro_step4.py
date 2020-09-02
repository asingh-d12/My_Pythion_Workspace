# Let's think about functions as arguments now.
def hello():
    return "Hi Amrit!!"


def other(func):
    print("Some other code")
    # Here I am assuming func is a function and thus execute this function here
    print(func())


# Here I am executing other function and passing function hello as an argument
other(hello)
