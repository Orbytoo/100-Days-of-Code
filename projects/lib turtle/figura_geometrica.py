from random import *
from os import system

system('cls')

# =====================================================================

from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

screen.title('Deus é fiel')

colors = ['cyan', 'navy', 'dark gray', 'medium aquamarine', 'medium purple' , 'burlywood' , 'dark green', 'chartreuse' , 'dark orchid' , 'black', 'medium slate blue', 'magenta', 'firebrick', 'red','dodger blue', 'light slate blue', 'dark magenta', 'orange red', 'spring green', 'yellow', 'chartreuse']
icons = ['turtle', 'circle', 'square', 'triangle', 'classic']


def create_figure(sides: int):
    """
    Parameters:
        sides = A quantidade de lados da figura geométrica;
    Obs:
        Possibilita criar figuras geométricas 
        (   triangle, square, pentagono, hexagon, circle
            heptagon, octagon, nonagon and decagon. )
    """
    turtle.fillcolor(choice(colors))
    screen.bgcolor(choice(colors))
    
    turtle.shape(choice(icons))
    turtle.pencolor(choice(colors))

    angle = 360 / sides

    for _ in range(sides):
        turtle.left(angle)
        turtle.forward(100)


def starting_position():
    """Posição Inicial"""
    turtle.penup()
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(50)
    turtle.pendown()


#Programa principal
starting_position()

for count in range(3, 11):
    create_figure(count)



screen.exitonclick()