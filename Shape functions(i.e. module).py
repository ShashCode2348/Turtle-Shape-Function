#To use these functions, import turtle as t, and add the functions to your code
class turtleShapes:
    import turtle as t
    def rectangle_with_fill(horizontal, vertical, color):
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

    def star_with_fill_improved(length, points, color):
        t.penup()
        angle = 180 - (180/points)
        t.color(color)
        t.begin_fill()
        for point in range(points):
            t.forward(length)
            t.right(angle)
        t.end_fill()
        t.penup()

    def any_polygon_with_fill(length, angles, color):
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

    def star_without_fill_improved(length, points, color, pensize):
        t.pendown()
        angle = 180 - (180/points)
        t.color(color)
        t.pensize(pensize*2)
        for point in range(points):
            t.forward(length)
            t.right(angle)
        t.penup()
        t.right((angle/4))
        t.forward(pensize/4)
        t.setheading(0)
        t.pensize(1)
        t.forward(pensize/4)
        t.color('#FFFFFF')
        t.pendown()
        t.begin_fill()
        for point in range(points):
            t.forward(length - (pensize))
            t.right(angle)
        t.end_fill()
        t.penup()

    def any_polygon_without_fill(length, angles, color, pensize):
        sumangle = (angles - 2) * 180
        oneangle = (sumangle/angles) - 180
        t.color(color)
        t.pensize(pensize)
        t.pendown()
        for counter in range(angles):
            t.forward(length)
            t.right(oneangle)
        t.penup()








