import tkinter


# Parabola is where y=x^2
def parabola(page, size):
    # Parabola function will be used to actually plot the parabola on canvas
    for i in range(size):
        plot(page, i, -i**2/size)
        plot(page, -i, -i ** 2 / size)


def plot(canvas, x, y):
    """Canvas do not really have a way to plot single points, but it can plot lines with length=1
    so we are going to plot lines of length=1"""
    canvas.create_line(x, y, x+1, y+1, fill="blue")

def draw_axis(canvas):
    """This method will be used to draw the axis on the Canvas
    but first, we have to shift origin in middle"""

    # We are making sure canvas is updated with the settings we mentioned in main so as to get accurate width and height
    canvas.update()

    # Here we are calculating half of width and height, as they will form our new origin for the canvas
    x_origin = canvas.winfo_width()/2
    y_origin = canvas.winfo_height()/2

    # This will make sure that origin is shifted in middle as this tells that scroll region starts with -x_origin and
    # goes till x_origin for x axis. Similarly, for y axis.
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="black")
    print("In draw_axis mehtod, locals = {}".format(locals()))


# Now let's see how we can plot this parabola on a graph
# using tkinter
def main():
    main_window = tkinter.Tk()
    main_window.title("Parabola")
    main_window.geometry("640x480")
    # We are adding Canvas to plot the graph
    canvas = tkinter.Canvas(main_window, width=640, height=480)
    canvas.grid(row=0, column=0)

    # Canvas has 0,0 at top left and not in middle so we have to check out screen width and height so as to shift the
    # origin in the middle, and also create x and y axis
    draw_axis(canvas)
    parabola(canvas, 100)

    print("In Main Function locals = {}".format(locals()))

    main_window.mainloop()


if __name__ == '__main__':
    # Print out global variables
    print(globals())

    # print out local variables outside in the main
    print(locals())

    # Are globals and locals same outside all the methods
    print(globals() == locals())

    print("*" * 50)
    main()
