# We are taking the code from Pack GM 18

# this is going to very similar to what we did in 17

import tkinter

main_window = tkinter.Tk()
main_window.title("Pack GM Part-2")
main_window.geometry("640x480+200+200")

a_label = tkinter.Label(main_window, text="Hello, World!!")
# Now putting an element in a grid in row=0 and column=0
a_label.grid(row=0, column=0)

left_frame = tkinter.Frame(main_window)
left_frame.grid(row=1, column=1)

canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

# Next, create a right frame
right_frame = tkinter.Frame(main_window)
# # Right now, frame is in the middle and not anchored to the top
# right_frame.grid(row=1, column=2)
# c0. in grid GM, we have "sticky" property that helps us in anchoring
right_frame.grid(row=1, column=2, sticky='n')

# expand, if provided.. takes the available space available

# Now adding those buttons to this right_frame
btn_1 = tkinter.Button(right_frame, text="Button 1")
btn_2 = tkinter.Button(right_frame, text="Button 2")
btn_3 = tkinter.Button(right_frame, text="Button 3")

btn_1.grid(row=0, column=0)
btn_2.grid(row=1, column=0)
btn_3.grid(row=2, column=0)

# c1. Right now, the buttons are very close to left_frame, but we want there to
# be some gap. How to do it?
# so, currently right_frame is as big as it requires to be
# We can change by adding weights to the columns here for main_window
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
# This grid_columnconfigure is same as column configure
main_window.grid_columnconfigure(2, weight=1)

# c2. Here we are going to change some properties of left_frame and
# right_frame so that we can see the borders of these frames
# config() can be used to add configurations to a window/object
left_frame.config(relief='sunken', borderwidth=1)
right_frame.config(relief='sunken', borderwidth=1)
# c3. Now calling grid() function on left and right frame again, so that
# left_frame is fully expanded vertically 'ns' and right frame is fully expanded
# horizontally 'new'. n added to anchor it to top
left_frame.grid(sticky='ns')
right_frame.grid(sticky='new')

# c4. Right now, buttons are at left edge of the right_frame, but we want in
# expanded and centered
# so if we try this
btn_1.grid(sticky='ew')
# Will this work?
# NOPE!!!
# Mainly because sticky only works if there is weight option available to
# tell what weight column or row has and expand into that
# So, let's add weight to the right_frame
right_frame.columnconfigure(0, weight=1)
# sticky='ew' Works now for button1
main_window.mainloop()
