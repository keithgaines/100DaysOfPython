import random
import turtle


# import colorgram
# rgb_colors = []

# uses colorgram to extract 15 colors from the image.jpg
# colors = colorgram.extract('image.jpg', 15)
#
# for extracted colors, assign rgb values to variables r, g, and b and assign those as a tuple to the new_color variable
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


def random_color():
    """returns a random color from the rgb_colors list from the commented out/previously run section of code"""
    rgb_colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
                  (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
                  (47, 121, 86), (73, 43, 35), (145, 178, 149)]

    return random.choice(rgb_colors)


# initializes screen
screen = turtle.Screen()
screen.setup(width=900, height=900, startx=0, starty=0)

# turtles basic settings
turtle.colormode(255)
jim = turtle.Turtle()  # initializes the turtle named Jim
jim.hideturtle()  # hides the turtle icon/cursor
jim.speed("fastest")
jim.penup()
# # setheading 0-east, 90-north, 180-west, 270-south
jim.setheading(225)
jim.forward(250)
jim.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    jim.dot(20, random_color())
    jim.forward(50)
    # moves turtle to the next row if dot count 10, 20, 30, etc.
    if dot_count % 10 == 0:
        jim.setheading(90) # points turtle north/up
        jim.forward(50)
        jim.setheading(180) # points turtle left
        jim.forward(500)
        jim.setheading(0) # points turtle right

screen.exitonclick()