from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(10,2)
        self.color("white")
        self.penup()


    def position(self,whichone):
        if whichone == "right":
            self.setpos(1200,0)
        elif whichone == "left":
            self.setpos(-1200, 0)


    def movement_up_arrows(self):
        current_posup = self.pos()
        self.goto(current_posup[0], current_posup[1] + 40)
        print (current_posup)
       # self.screen.update()


    def movement_down_arrows(self):
        current_posdown = self.pos()
        self.goto(current_posdown[0],current_posdown[1]-40)
       # self.screen.update()

    def movement_up_wsad(self):
        current_posup = self.pos()
        self.goto(current_posup[0], current_posup[1] + 40)
      #  self.screen.update()

    def movement_down_wsad(self):
        current_posdown = self.pos()
        self.goto(current_posdown[0], current_posdown[1] - 40)
      #  self.screen.update()







