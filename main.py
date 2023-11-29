# import colorgram

# colors = colorgram.extract('./image.png',30)

# array_of_colors = []

# for color in colors:
#     array_of_colors.append((color.rgb[0],color.rgb[1],color.rgb[2]))

# print(array_of_colors)

# PROGRAM REQUIREMENTS
# we need a 10 x 10 square of colored spots
# Each circle needs to be 20 in size and each one has to be 50 from their neighbour

from turtle import Turtle, Screen
import random

# Screen setup
screen = Screen()
screen.colormode(255)
screen.title('Hirst Dots Replica Painting')

tim = Turtle()
color_list = [(250, 228, 12), (198, 11, 36), (246, 234, 238), (207, 13, 11), (233, 228, 5), (195, 67, 21), (239, 147, 30), (45, 210, 59), (30, 91, 187), (34, 32, 153), (17, 25, 54), (245, 38, 143), (68, 10, 52), (224, 249, 240), (61, 205, 231), (14, 203, 220), (247, 43, 12), (64, 25, 11), (223, 20, 102), (14, 150, 30), (227, 167, 8), (97, 75, 9), (248, 11, 8), (64, 242, 167), (226, 241, 247), (224, 137, 208), (9, 97, 62), (5, 46, 38), (85, 227, 237)]

# Start 'tim' config
tim.home()
tim.penup()
x = -200
y = -200
tim.setposition(x, y)
tim.hideturtle()

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

    tim.penup()
    y = y + 50
    tim.setposition(x, y)





screen.exitonclick()