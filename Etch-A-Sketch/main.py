import turtle

# initializes screen
screen = turtle.Screen()
screen.setup(width=900, height=900, startx=0, starty=0)

# turtles basic settings
turtle.colormode(255)
jim = turtle.Turtle()  # initializes the turtle named Jim
jim.width(25)


def move_forward():
    jim.pendown()
    jim.pencolor("black")
    jim.forward(10)


def move_backwards():
    jim.pendown()
    jim.pencolor("black")
    jim.backward(10)


def turn_left():
    jim.left(45)


def turn_right():
    jim.right(45)


def clear_screen():
    jim.clear()


screen.listen()  # starts the screen listening for events

# sets onkey press event listener to call functions based on which key is pressed
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
