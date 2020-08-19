import tkinter

# Here we are going to create an empty window, but this process we are going
# to use going forward when creating other GUIs

# Top level widget of Tk which represents mostly the main window of an
# application. This is a init call to Tk Class.
main_window = tkinter.Tk()
print(type(main_window))

# Now let's invoke a couple of methods in Tk class
# This is to provide title to the main window.
main_window.title("Empty Main Window")

# Next, let's tell the window about its width and height using "geometry method"
# Make sure to put the width and height in string with width and height
# separated by x
main_window.geometry("640x480")

# Oh an we can also tell where to open the screen by providing offsets
# + represents position from top and left
# - represents position from right and bottom
# Oh, and offset is pixels
# Check this out
main_window.geometry("640x480+640+285")

# Now, we are done with everything that we have to do... and now we are going
# to pass control to tk so it can run the gui
# This is done using method mainloop()
main_window.mainloop()

# Yup, we got an empty window just now
