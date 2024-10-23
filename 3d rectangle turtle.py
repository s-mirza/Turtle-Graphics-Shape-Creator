import turtle

side_side1 = 50
side2 = 100

turtle.pencolor('#7C5E01')
turtle.pensize(5)

turtle.bgcolor('#FFFFFF')

turtle.begin_fill()

turtle.forward(side_side1)
turtle.right(90)

turtle.setheading(90)

turtle.forward(side_side1)
turtle.left(90)

turtle.forward(side_side1)
turtle.right(90)

turtle.setheading(180)
turtle.left(90)
turtle.forward(side_side1)

turtle.left(45)
turtle.forward(side2)

turtle.left(135)
turtle.forward(side_side1)

turtle.left(45)
turtle.forward(side2)

turtle.left(225)
turtle.forward(side_side1)

turtle.right(45)
turtle.forward(side2)

turtle.right(45)
turtle.forward(side_side1)

turtle.right(90)
turtle.forward(side_side1)

turtle.right(90)
turtle.forward(side_side1)

turtle.right(90)
turtle.forward(side_side1)

turtle.right(90)
turtle.forward(side_side1)

turtle.right(135)
turtle.forward(side2)

turtle.done()