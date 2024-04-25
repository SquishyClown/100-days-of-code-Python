from turtle import Turtle

class Guesser(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def state(self,state_name,state_x,state_y):
        self.goto(state_x,state_y)
        self.write(f"{state_name}")

    def gg(self):
        self.goto(-140,0)
        self.write("YOU WIN GG",font=("Verdana",32, "normal"))

