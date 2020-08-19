import tkinter

main_window = tkinter.Tk()
main_window.title("Pack GM")
main_window.geometry("640x480+200+200")

# Let's start off by creating a label object/Window
# Label(and every other window) mandatory requires what its master window
# going to be
# Here master is main_window
# text - keyword argument of label
a_label = tkinter.Label(main_window, text="Hello, World!!")
# Now to tell where we want this label to be in the main window
# This we are going to use using pack geometry manager
# this pack method we call upon "Child Window" itself
# side is 1 of keyword arguments in any window class
a_label.pack(side='top')

# Next, let's create a canvas
# master window = main_window... mandatory argument
# relief and borderwidth are keyword arguments that canvas can have
a_canvas = tkinter.Canvas(main_window, relief="raised", borderwidth=1)
# a_canvas.pack(side='left')
# One other keyword argument in pack()
# fill - tells window to fill the space in either x or y or in both directions
a_canvas.pack(side='left', fill=tkinter.Y)
# Though note that when it is filling, it is only using space that is below
# label and not on it. this is because label already allocated space before.

# What if we do fill=tkiner.X
# a_canvas.pack(side='left', fill=tkinter.X)
# This doesn't work
# Ok, so we have to understand this
# fill works only in single direction, mainly
# if pack is to left or right.... fill will only work in y
# if pack is in top or bottom... fill will only work in x

# But, what if WE WANT to do fill in another direction, or say both directions
# There is another keyword argument for that
# expand=true
# a_canvas.pack(side='left', fill=tkinter.X, expand=True)
# Now this work

# Or we can do this as well
# a_canvas.pack(side='left', fill=tkinter.BOTH)
# Right now it will expand only in direction where it is allowed i.e. Y...
# even though BOTH is mentioned

# So, we can do something like this
# a_canvas.pack(side='left', fill=tkinter.BOTH, expand=True)

# Adding Buttons to this window now
# text kw(keyword argument) to provide text on button
btn_1 = tkinter.Button(main_window, text="Button 1")
btn_2 = tkinter.Button(main_window, text="Button 2")
btn_3 = tkinter.Button(main_window, text="Button 3")
#
# btn_1.pack(side='left')
# btn_2.pack(side='left')
# btn_3.pack(side='left')
# Right now, when these buttons are created, they will just stick to canvas
# just simple meaning of pack... pack 1 aside other

# Though to change that, we can provide anchor ro where we are packing
# Check this out
# btn_1, btn_2 and btn_3 are anchored to north, south and east respectively
btn_1.pack(side='left', anchor='n')
btn_2.pack(side='left', anchor='s')
# Though even if it looks like anchor='e' is doing anything
# It is not, because we have placed window in horizontal axis
# So horizontal anchors won't work
btn_3.pack(side='left', anchor='e')

# Same is true if windows are placed in vertical axis,
# then vertical anchors won't work

main_window.mainloop()

# REMEMBER PACK IS SUITABLE FOR VERY SIMPLE LAYOUT, AND USE IS VERY BASIC
