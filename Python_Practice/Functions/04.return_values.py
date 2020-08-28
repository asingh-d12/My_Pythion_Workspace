def center_text(*args, sep=' '):
    # We are going to join all the text we get with the help of *args
    # Now, we are only taking one named/default parameter... sep=' '
    # This is mainly because we are not going to print directly in here... in
    # stead we are going to return a value
    text = ""
    for arg in args:
        text = text + str(arg) + sep
    width = 222
    # This will be converting any argument we pass to a string
    text = str(text)
    left_margin = width//2 - len(text) // 2
    return "{}{}".format(" " * left_margin, text)


# Now that center_text function is returning instead of directly printing
print(center_text("Amritpal Singh Narula"))
# We can do like this as well... return to a variable
z = center_text("Jupnit Singh")
print(z)
print(center_text(200))
print(center_text("Amrit"))

# Now that we have used *args in center_text function, we can call like this
# as well
print(center_text("Amrit", "Jupnit", "Lucky", 7, "Awesome!!", sep='*'))
