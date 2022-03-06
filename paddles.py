# from turtle import Turtle




class Paddle
    def __init__(self):
        self = Turtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(350, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        paddle.goto(paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
