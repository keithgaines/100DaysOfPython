import time
from turtle import Turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(turtle.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False

    if turtle.ycor() == 280:
        turtle.reset_position()



screen.exitonclick()
