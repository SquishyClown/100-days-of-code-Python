from turtle import Turtle, Screen
import random
import sys
tim = Turtle()
tim.shape("turtle")
tim.color("red")
scr = tim.screen





def circle():
    scr.colormode(255)
    #tim.width(15)
    tim.speed("fastest")
    head = 1
    while 1 > 0:
        r = int(random.randint(0, 255))
        g = int(random.randint(0, 255))
        b = int(random.randint(0, 255))
        tim.color(r, g, b)
        tim.circle(100)
        tim.setheading(head)
        tim.heading()
        head += 10



circle()
















screen = Screen()
screen.exitonclick()