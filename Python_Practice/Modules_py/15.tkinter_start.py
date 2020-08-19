try:
    import tkinter
except ImportError:
    # Catching for Python2 as well
    import Tkinter as tkinter

# To check tk version
print(tkinter.TkVersion)

# To check TCL version
print(tkinter.TclVersion)

# Now to test if tk can create a gui
tkinter._test()

# It works, Awesome!!!
