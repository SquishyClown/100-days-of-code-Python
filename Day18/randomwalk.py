from turtle import Turtle, Screen
import random
import sys
tim = Turtle()
tim.shape("turtle")
tim.color("red")
scr = tim.screen



obrot = [0, 90, 180, 270]

def randomwalk():
    scr.colormode(255)
    tim.width(15)
    tim.speed("fastest")
    while 1 > 0:
        tim.forward(50)
        wybor = int(random.choice(obrot))
        tim.right(wybor)

        r = int(random.randint(0, 255))
        g = int(random.randint(0, 255))
        b = int(random.randint(0, 255))
        tim.color(r, g, b)


randomwalk()
















screen = Screen()
screen.exitonclick()