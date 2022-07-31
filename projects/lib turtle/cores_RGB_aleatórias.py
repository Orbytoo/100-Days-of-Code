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

directions = [0, 90, 180, 270]


turtle.width(15)
turtle.speed('fast')

for _ in range(200):
    turtle.color(random_color())

    turtle.forward(30)
    turtle.setheading(choice(directions))    










screen.exitonclick()