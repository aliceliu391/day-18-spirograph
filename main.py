import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)

angle = 0


def new_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


while angle <= 360:
    tim.color(new_color())
    tim.left(10)
    tim.circle(90)
    angle += 10

s = Screen()
s.exitonclick()
