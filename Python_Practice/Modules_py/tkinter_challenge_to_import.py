import tkinter

calc_buttons = [[('C', 1), ('CE', 1)],
                [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
                [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
                [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
                [('0', 1), ('=', 2), ('/', 1)]]

main_window = tkinter.Tk()
main_window.geometry("240x240+100+100")
main_window.title("Calculator")

# Add entry to the
result_entry = tkinter.Entry(main_window, width=20)
result_entry.grid(row=0, column=0, sticky='nwes')
main_window['padx'] = 10
main_window['pady'] = 10

# Adding a frame for buttons
btn_frame = tkinter.Frame(main_window, relief='sunken', border=2)
btn_frame.grid(row=1, column=0, sticky='nwes')

btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)
btn_frame.columnconfigure(2, weight=1)
btn_frame.columnconfigure(3, weight=1)

btn_frame.rowconfigure(0, weight=1)
btn_frame.rowconfigure(1, weight=1)
btn_frame.rowconfigure(2, weight=1)
btn_frame.rowconfigure(3, weight=1)
btn_frame.rowconfigure(4, weight=1)


# Adding buttons to button frame
i = 0
for a_row in calc_buttons:
    j = 0
    for a_btn in a_row:
        tkinter.Button(btn_frame, text=a_btn[0]).\
            grid(row=i, column=j, columnspan=a_btn[1], sticky='nsew')
        j += a_btn[1]
    i += 1

# So, here comes the concept of update()
# What this will do, is update the whole main_window with all gui elements...
# though not display them
main_window.update()
# Why are we updating though?
# Mainly, so that we can determine what the min size is going to be.
# This can be done by adding the width and height of all the elements and
# then providing it to minsize() method...
# So, that our main_window doesn't go smaller than that
main_window.minsize(width=btn_frame.winfo_width() + 2*10,
                    height=btn_frame.winfo_height() +
                           result_entry.winfo_height())

# Also, going to set max size of the window, so that it doesn't go beyond
# that size
main_window.maxsize(width=240, height=240)

main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=8)

main_window.mainloop()
