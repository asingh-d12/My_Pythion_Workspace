# this is going to very similar to what we did in 17

import tkinter

main_window = tkinter.Tk()
main_window.title("Pack GM Part-2")
main_window.geometry("640x480+200+200")

a_label = tkinter.Label(main_window, text="Hello, World!!")
a_label.pack(side='top')

# Here are where changes start, instead of directly adding canvas
# Let's create a Frame first
left_frame = tkinter.Frame(main_window)
left_frame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

# Now Canvas is going to be inside this left_frame, with pack GM
canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

# Next, create a right frame
right_frame = tkinter.Frame(main_window)
right_frame.pack(side='right', anchor='n', expand=True)

# expand, if provided.. takes the available space available

# Now adding those buttons to this right_frame
btn_1 = tkinter.Button(right_frame, text="Button 1")
btn_2 = tkinter.Button(right_frame, text="Button 2")
btn_3 = tkinter.Button(right_frame, text="Button 3")

btn_1.pack(side='top')
btn_2.pack(side='top')
btn_3.pack(side='top')

main_window.mainloop()
