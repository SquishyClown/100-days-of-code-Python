from turtle import Turtle
pointsl = 0
pointsr = 0
class Scoreboardleft(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.goto(-800,600)
        self.hideturtle()


    def show(self):
        self.clear()
        global pointsl
        pointsl += 1
        self.write(f"{pointsl}", font=("Verdana", 48), align="center")


class Scoreboardright(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.goto(800,600)
        self.hideturtle()

    def show(self):
        self.clear()
        global pointsr
        pointsr += 1
        self.write(f"{pointsr}", font=("Verdana", 48), align="center")



