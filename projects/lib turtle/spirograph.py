from os import system
from random import *

system('cls')


############################################################
from turtle import Turtle, Screen, colormode

turtle = Turtle()
colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    x =  (r, g, b)
    return x


screen = Screen()
screen.title('Deus é bom')

turtle.speed(80)
turtle.width(2)

for _ in range(73):
    turtle.color(random_color())
    turtle.circle(100, 360)
    turtle.left(5)
    












screen.exitonclick()