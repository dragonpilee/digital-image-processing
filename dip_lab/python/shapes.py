import turtle

turtle.shape("turtle")
turtle.fillcolor("green")
turtle.begin_fill()
turtle.color("blue")
turtle.circle(45)
turtle.end_fill()

turtle.bgcolor("red")

turtle.penup()
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.pendown()

turtle.fillcolor("grey")
turtle.begin_fill()
for _ in range(4):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()

turtle.left(180)
turtle.penup()
turtle.forward(100)
turtle.pendown()

turtle.fillcolor("orange")
turtle.begin_fill()
for _ in range(3):
    turtle.forward(100)
    turtle.right(120)
turtle.end_fill()

turtle.done()

