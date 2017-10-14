"""Nickelbacki kontsert."""
import calendar
import locale
import turtle
import random


def get_month_name(month_no):
    """Convert a month's numeric value into its Estonian name as a string."""
    locale.setlocale(locale.LC_TIME, "et-EE")
    return calendar.month_name[month_no]


def draw_graph(pencil: turtle.Turtle, posx, posy, data_list):
    """
    Draw a bar chart-style graph and a legend describing the data.

    Arguments:
    pencil -- the turtle object used for drawing
    posx, posy -- start coordinates of the drawing
    data_list -- the data shown on the graph as a list of numeric values
    """
    main()
    pencil.up()
    pencil.setpos(posx, posy)
    draw_bars(pencil, data_list)
    pencil.forward(50)
    draw_legend(pencil, data_list)


def draw_legend(pencil: turtle.Turtle, data_list):
    """
    Draw a legend box for a graph.

    The legend box contains text describing the data.
    Arguments:
    pencil -- the turtle object used for drawing
    data_list -- the data as a list of numeric values
    """
    pencil.down()
    pencil.left(90)
    pencil.forward(450)
    pencil.right(90)
    pencil.forward(300)
    pencil.right(90)
    pencil.forward(450)
    pencil.right(90)
    pencil.forward(300)
    pencil.up()
    pencil.right(90)
    pencil.forward(420)
    pencil.right(90)
    pencil.forward(30)
    for i in range(len(data_list)):
        pencil.write(get_month_name(i + 1).capitalize() + " " + str(data_list[i]) + " EUR")
        pencil.right(90)
        pencil.forward(30)
        pencil.left(90)
    if sum(data_list) >= 470:
        pencil.write("Saad minna kontserdile!")
    else:
        pencil.write("Pead veel koguma!")
    turtle.done()


def draw_bars(pencil: turtle.Turtle, data_list):
    """
    Draw a bar chart.

    Arguments:
    pencil -- the turtle object used for drawing
    data_list -- the data as a list of numeric values
    """
    for i in range(len(data_list)):
        pencil.down()
        pencil.fillcolor(random.random(), random.random(), random.random())
        pencil.begin_fill()
        pencil.left(90)
        pencil.forward(data_list[i] * 1.5)
        pencil.right(90)
        pencil.forward(50)
        pencil.right(90)
        pencil.forward(data_list[i] * 1.5)
        pencil.right(90)
        pencil.forward(50)
        pencil.right(180)
        pencil.up()
        pencil.end_fill()
        pencil.forward(50)
        pencil.fillcolor("white")


def main():
    """Set up the turtle window and start the drawing process."""
    turtle.setup(width=1.0, height=1.0)


if __name__ == "__main__":
    main()
data_list = [100, 50, 150, 300, 200, 100, 50, 150, 300, 200.9, 200, 100]

draw_graph(turtle,-200,-200,data_list)