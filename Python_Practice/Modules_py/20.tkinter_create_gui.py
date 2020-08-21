import tkinter
import os

# Here we are going to create 1 of the advanced GUI that contains several GUI
# elements and good demonstration of Grid Geometry Manager
# PFB the GUI elements:
# 1. Label
# 2. Listbox and scrollbar
# 3. Label Frames

main_window = tkinter.Tk()
main_window.title("Advanced GUI")
main_window.geometry("640x480+200+200")

# First let's create a label
label = tkinter.Label(main_window, text="Tkinter Grid Demo")

# Now if we see the grid diagram, the label is extending over 3 columns
# Let's see how to do thatfrom
# use columnspan kw in grid() method
label.grid(row=0, column=0, columnspan=3)
# Even though the sticky by default is centered, the label is not centered on
# the screen...
# This is mainly because we haven't given any weights to main window yet

# I Think, weights help in providing %age of the screen..

# Let's provide weight's to the columns - TODO - WHY??
main_window.columnconfigure(0, weight=100)
main_window.columnconfigure(1, weight=5)
main_window.columnconfigure(2, weight=100)
main_window.columnconfigure(3, weight=25)
main_window.columnconfigure(4, weight=50)
# main_window.columnconfigure(0, weight=1)
# main_window.columnconfigure(1, weight=1)
# main_window.columnconfigure(2, weight=3)
# main_window.columnconfigure(3, weight=3)
# main_window.columnconfigure(4, weight=3)

# Also, we are going to provide weights to rows as well - TODO - WHY?
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=10)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=3)
main_window.rowconfigure(4, weight=3)

# Have to understand why these weights?

# But if we run GUI now, it will be much more centered.

# Now, let's add the list box
# Not much required while creating it.. only parent window
file_list = tkinter.Listbox(main_window)
# Let's add it to the grid... make sure it is expanding over 2 rows as seen
# in the screenshot
# Also, we want to expand it over the whole cell in the grid... so using
# sticky='nsew'
file_list.grid(row=1, column=0, sticky='nsew', rowspan=2)
# We are using config to add properties to this listbox here, we can have
# done this while creating listbox as well in the constructor
# border and borderwidth are same
file_list.config(border=2, relief='sunken')

# Now, code to populate the listbox - we are going to use files in a
# particular directory
for a_file in os.listdir('/usr/bin'):
    # Here we are going to add the file to file_list listbox
    # tkinter.END is the index which is required by this method
    # So, each element will be inserted at the end of the list
    # We could also have mentioned an index... for ex: 0 to insert each new
    # element at the start
    file_list.insert(tkinter.END, a_file)

# Let's run and check it out.

# Now, we require to add the scrollbar, it is a separate component and not
# part of listbox... let's check it out
# orient KW - vertical or horizontal... here it is vertical
# command KW - so, this is actually the keyword argument that helps associate
# event to cause an action... so in case of a scrollbar.. what actually
# happens when we scroll the scrollbar up and down... it should affect the
# file_list
# file_list.yview() is a method that does that, itQuery and change the vertical
# position of the view. that is scrolls the listbox...
# So how to associate this method with command in Scrollbar.. simple pass
# reference of this method to command
# REMEMBER - NOT THE METHOD, BUT REFERENCE TO THE METHOD
# If we pass method... it will provide what method returns to command... we
# don't want that... we want command to have method's reference.. so
# scrollbar can call this method
list_scroll = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL,
                                command=file_list.yview)
# Adding scrollbar to the grid... right next to listbox we created
list_scroll.grid(row=1, column=1, rowspan=2, sticky='nsw')
# 1 more step
# Now if we scroll using scrollbar, listbox will be affected.
# But what id we scroll listbox directly using mouse wheel.. in that case
# scrollbar has to be affected as well
# We are going to use this method to connect listbox to scrollbar
# Another way to create a property of an element
file_list['yscrollcommand'] = list_scroll.set
# we could have used this as well
file_list.config(yscrollcommand=list_scroll.set)
# What is listscroll.set... another reference to the method in scrollbar
# set method - Set the fractional values of the slider position (upper and
#         lower ends as value between 0 and 1)

# Let's run now.

# Let's add Label Frames now..
# What are Label Frames? Basically they have label at top of a frame,
# with radio buttons in it
option_frame = tkinter.LabelFrame(main_window, text="File Details, Label Frame")
option_frame.grid(row=1, column=2, sticky='ne')
# So, now we have create the Label Frame
# We require to add radio buttons in it
# So, how to create radio buttons
# Simple, we associate a variable with all the radio buttons in a single set
# So, that only 1 can be selected at a time, and the variable will get the
# value of that radio button
# This here is going to be an Int Control Variable
# Control Variables are Variables that can be bound to widgets
rb_value = tkinter.IntVar()
# Let's create the radio buttons now
# text kw -  what to display against the rb
# value kw - what is the value associated with the radio button
# variable kw - this variable will get the value of any particular radio
# button, and this variable will be same for all the radio buttons in a
# single set
radio1 = tkinter.Radiobutton(option_frame, text="Filename", value=1,
                             variable=rb_value)
radio2 = tkinter.Radiobutton(option_frame, text="Path", value=2,
                             variable=rb_value)
radio3 = tkinter.Radiobutton(option_frame, text="Timestamp", value=3,
                             variable=rb_value)
# Adding radio buttons to the frame
# Also, we want to align the radio buttons to left... so sticky='w'
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')
# Let' set a default value for the radio buttons
rb_value.set(1)

# Next, we are going to add result label and entry associated there
result_label = tkinter.Label(main_window, text='Result')
result_label.grid(row=2, column=2, sticky='nw')
result_entry = tkinter.Entry(main_window)
result_entry.grid(row=2, column=2, sticky='sw')
# Remember, if the windows becomes small enough, the label will hide behind
# entry

# Now we are going to create the spinners inside a label frame
time_frame = tkinter.LabelFrame(main_window, text="Time")
time_frame.grid(row=3, column=0, sticky='new')
# Now, adding spinners to the frame
# Also, how to add values to the spinners
# width basically calls for width of value
# This is 1 way to add value to Spinner... using a tuple
hour_spinner = tkinter.Spinbox(time_frame, width=2, values=tuple(range(0, 24)))
# Another way to add values to spinbox... we use from_ becoz from is a keyword
minute_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
second_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
hour_spinner.grid(row=0, column=0)
tkinter.Label(time_frame, text=":").grid(row=0, column=1)
minute_spinner.grid(row=0, column=2)
tkinter.Label(time_frame, text=":").grid(row=0, column=3)
second_spinner.grid(row=0, column=4)
# Right now, the spinners are very close to left side of the main_window
# Good thing, we can provide padding inside time_frame... padx and pady
# Though i think, here we need padx only... this pads left and right edge
time_frame['padx'] = 36

# Now let's add date spinners as well
# First frame for the date... here this is not label frame, but a simple frame
date_frame = tkinter.Frame(main_window, border=2, relief='raised')
date_frame.grid(row=4, column=0, sticky='new')
# Now adding labels
day_label = tkinter.Label(date_frame, text="Day")
mon_label = tkinter.Label(date_frame, text="Month")
year_label = tkinter.Label(date_frame, text="year")
day_label.grid(row=0, column=0, sticky='w')
mon_label.grid(row=0, column=1, sticky='w')
year_label.grid(row=0, column=2, sticky='w')
# Now spinners for day, month and year
day_spinner = tkinter.Spinbox(date_frame, width=5, from_=1, to=31)
# Here we will have to manually specify values... as these are going to be
# months
month_spinner = tkinter.Spinbox(date_frame, width=5, values=("Jan", "Feb",
                                                             "Mar", "Apr",
                                                             "May", "Jun",
                                                             "Jul", "Aug",
                                                             "Sep", "Oct",
                                                             "Nov", "Dec"))
year_spinner = tkinter.Spinbox(date_frame, width=5,
                               values=tuple(range(1990, 2099)))
# Adding date spinners to date_frame
day_spinner.grid(row=1, column=0, sticky='w')
month_spinner.grid(row=1, column=1, sticky='w')
year_spinner.grid(row=1, column=2, sticky='w')

# Adding OK and Cancel Button Now
ok_btn = tkinter.Button(main_window, text="OK")
# So, here we are adding command, so that if cancel button is clicked,
# main_window quits
cancel_btn = tkinter.Button(main_window, text="Cancel",
                            command=main_window.quit)
# Adding buttons to grid
# sticky='e' so that it can be towards right side
ok_btn.grid(row=4, column=3, sticky='e')
# sticky='w' so that it can be left and close to ok button
cancel_btn.grid(row=4, column=4, sticky='w')

# 1 more thing, the widgets are too close to the left edge, so let's add some
# padding... mainly padx
main_window['padx'] = 10

main_window.mainloop()

# Let's see the value of radio button, once gui is stopped
print(rb_value.get())
