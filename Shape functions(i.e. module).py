#To use these functions, import turtle as t, and add the functions to your code
#Lines 5-7 keep the window on top of all the other open windows. Feel free to use this as well
import turtle as t
class TurtleShapes:
    window = t.Screen()
    canvas = window.getcanvas().winfo_toplevel()
    canvas.call('wm', 'attributes', '.', '-topmost', '1')
    def rectangle_with_fill(horizontal, vertical, color):
        t.clear()
        t.pendown()
        t.pensize(1)
        t.color(color)
        t.begin_fill()
        for counter in range(2):
            t.forward(horizontal)
            t.right(90)
            t.forward(vertical)
            t.right(90)
        t.end_fill()
        t.penup()

    def star_with_fill(length, points, color):
        t.clear()
        sumangle = ((points * 2) - 2) * 180
        oneangle = sumangle/points
        smallangle = oneangle/3.5
        bigangle = oneangle - smallangle
        t.pensize(1)
        t.color(color)
        t.begin_fill()
        t.pendown()
        for counter in range(points):
            t.forward(length)
            t.left(smallangle)
            t.forward(length)
            t.left(bigangle)
        t.end_fill()
        t.penup()

    def any_polygon_with_fill(length, angles, color):
        t.clear()
        sumangle = (angles - 2) * 180
        oneangle = (sumangle/angles) - 180
        t.color(color)
        t.pensize(1)
        t.begin_fill()
        t.pendown()
        for counter in range(angles):
            t.forward(length)
            t.right(oneangle)
        t.end_fill()
        t.penup()

    def rectangle_without_fill(horizontal, vertical, color, pensize):
        t.clear()
        t.pendown()
        t.pensize(pensize)
        t.color(color)
        for counter in range(2):
            t.forward(horizontal)
            t.right(90)
            t.forward(vertical)
            t.right(90)
        t.penup()

    def star_without_fill(length, points, color, pensize):
        t.clear()
        sumangle = ((points * 2) - 2) * 180
        oneangle = sumangle/points
        smallangle = oneangle/3.5
        bigangle = oneangle - smallangle
        t.color(color)
        t.pensize(pensize)
        t.pendown()
        for counter in range(points):
            t.forward(length)
            t.left(smallangle)
            t.forward(length)
            t.left(bigangle)
        t.penup()

    def any_polygon_without_fill(length, angles, color, pensize):
        t.clear()
        sumangle = (angles - 2) * 180
        oneangle = (sumangle/angles) - 180
        t.color(color)
        t.pensize(pensize)
        t.pendown()
        for counter in range(angles):
            t.forward(length)
            t.right(oneangle)
        t.penup()
