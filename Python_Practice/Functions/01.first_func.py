# Function definition
def python_food():
    # Function begins here
    width = 222
    text = "spam and eggs"
    left_margin = width//2 - len(text) // 2
    print("{}{}".format(" " * left_margin, text))


python_food()

# By default a function returns None
# What we are doing here is called function call within a function call
# Basically what ever is returned in from inner function call will be used as
# an argument for outer function call
print(python_food())
