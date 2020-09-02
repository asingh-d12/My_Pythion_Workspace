# Let's understand LEGB Scope Rule

# Local
def report():
    # This is local
    x = "local"
    print(x)


# Enclosing - Will happen if a function inside a function
x = "This is Global level String"
y = "This is also a GLOBAL level String"


def enclosing():
    x = "This is Enclosing level"

    def inside_enclosing():
        print(x)
        print(y)

    # This will print x inside enclosing function as there is no local x in
    # inside_enclosing
    inside_enclosing()


# This will print the local x inside the report function
report()

# This will print enclosing x as per LEGB rule and not the Global x
enclosing()
# But, now inside_enclosing() is printing y as well, which is neither present
# in local scope nor in enclosing... but is only present in Global Scope
