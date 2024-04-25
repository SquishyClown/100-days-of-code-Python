from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("red")
scr = tim.screen


walls = 3


def shape():
    global walls
    for x in range(walls):
        scr.colormode(255)
        degree = 360 / walls
        tim.forward(100)
        tim.right(degree)
    r = int(random.randint(0, 256))
    g = int(random.randint(0, 256))
    b = int(random.randint(0, 256))
    tim.color(r, g, b)
    degree -= 12
    walls += 1

for y in range(7):
    shape()

















screen = Screen()
screen.exitonclick()