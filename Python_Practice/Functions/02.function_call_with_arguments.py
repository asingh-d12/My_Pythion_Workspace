# Function definition
def python_food():
    # Function begins here
    width = 222
    text = "spam and eggs"
    left_margin = width//2 - len(text) // 2
    print("{}{}".format(" " * left_margin, text))


def center_text(d_text):
    width = 222
    # This will be converting any argument we pass to a string
    d_text = str(d_text)
    left_margin = width//2 - len(d_text) // 2
    print("{}{}".format(" " * left_margin, d_text))


# Now center_text is a function that accepts arguments, let's do that
center_text("Amritpal Singh Narula")
center_text("Jupnit Singh")
center_text(200)
center_text("Amrit")
