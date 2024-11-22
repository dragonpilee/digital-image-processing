import turtle

# Function to draw a square
def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

# Function to draw a hexagon
def draw_hexagon():
    for _ in range(6):
        turtle.forward(100)
        turtle.right(60)

# Setup the turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("Square and Hexagon Drawing")

# Create a turtle object
t = turtle.Turtle()

# Set up turtle attributes
t.penup()
t.color("blue")
t.pensize(2)
t.speed(1)

# Draw the square
t.goto(-150, 0)
t.pendown()
draw_square()

# Draw the hexagon
t.penup()
t.goto(100, 0)
t.pendown()
draw_hexagon()

# Keep the window open
screen.mainloop()
