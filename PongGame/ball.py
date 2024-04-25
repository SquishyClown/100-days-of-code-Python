from turtle import Turtle, Screen
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(2,2)
        self.penup()
        self.setpos(-70,-70)
        self.bouncex = 5
        self.bouncey = 5

    def auto_move(self):
        newx = self.xcor() + self.bouncex
        newy = self.ycor() + self.bouncey
        self.goto(newx,newy)

    def bounceup(self):
        self.bouncex = 5
        self.bouncey = -5

    def bounceupwithouttouch(self):
        self.bouncex = -5
        self.bouncey = -5


    def bouncedown(self):
        self.bouncey =  5
        self.bouncex = -5

    def bouncedownwithouttouch(self):
        self.bouncey = 5
        self.bouncex = 5


    def bounceleft(self):
        self.bouncex =  5
        self.bouncey =  5

    def bouncerightgora(self):
        self.bouncex = -5
        self.bouncey = 5

    def bounceright(self):
        self.bouncex = -5
        self.bouncey = -5

    def score(self):
        self.goto(0,0)





