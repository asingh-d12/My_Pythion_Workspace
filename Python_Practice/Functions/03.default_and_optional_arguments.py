def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    # We are going to join all the text we get with the help of *args
    # Next, we are adding all the named arguments we noticed in print
    # function here as well
    text = ""
    for arg in args:
        text = text + str(arg) + sep
    width = 222
    # This will be converting any argument we pass to a string
    text = str(text)
    left_margin = width//2 - len(text) // 2
    print("{}{}".format(" " * left_margin, text), end=end, file=file,
          flush=flush)


center_text("Amritpal Singh Narula")
center_text("Jupnit Singh")
center_text(200)
center_text("Amrit")

# Now that we have used *args in center_text function, we can call like this
# as well
center_text("Amrit", "Jupnit", "Lucky", 7, "Awesome!!")
# Let's call with different separator
# So, by default sep=' '... but if call the function with the named arguments
# sep=';'.... the default value is overridden by the value we are sending
center_text("Amrit", "Jupnit", "Lucky", 7, "Awesome!!", sep=";")

with open("centered", 'w') as center_file:
    center_text("Amrit", "Jupnit", "Lucky", 7, "Awesome!!", sep="*",
                file=center_file)
