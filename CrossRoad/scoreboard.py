FONT = ("Courier", 24, "normal")
from turtle import Turtle,Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-250,250)
        self.hideturtle()
        self.currentlevel = 1
        self.write(arg=f"Level:{self.currentlevel}", font=FONT)

    def scoreupdate(self):
        self.clear()
        self.currentlevel += 1
        self.write(arg=f"Level:{self.currentlevel}", font=FONT)