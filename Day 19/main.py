import turtle
from turtle import Turtle, Screen
import random

scr = Screen()
scr.setup(width=500, height=400)
bet = scr.textinput(title="Make yout bet", prompt="Which turtle will win the race? Enter a color: ")
print(bet)

is_race_on = False
colors = ["red","orange","yellow", "green","blue","purple"]
y_positions =[-180,-120,-60,0,60,120]
all_turtles = []


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if new_turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print (f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")



        losowynumer = random.randint(0, 10)
        turtle.forward(losowynumer)




scr.exitonclick()
