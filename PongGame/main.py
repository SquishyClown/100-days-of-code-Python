from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboardleft, Scoreboardright
import random

screen = Screen()
paddleleft = Paddle()
paddleright = Paddle()
ball = Ball()
scoreboardl = Scoreboardleft()
scoreboardr = Scoreboardright()


screen.screensize(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(1)

#paddle right
paddleright.position("right")
screen.listen()
screen.onkey(paddleright.movement_up_arrows,"Up")
screen.onkey(paddleright.movement_down_arrows,"Down")

#paddle left
paddleleft.position("left")
screen.onkey(paddleleft.movement_up_wsad,"w")
screen.onkey(paddleleft.movement_down_wsad,"s")

#ball
gameison = True
pointsl = 0
pointsr = 0
while gameison == True:
    screen.update()
    ball.auto_move()
    distleft = ball.distance(paddleleft)
    distright = ball.distance(paddleright)
    randomliczba = random.randint(0,1)
    if ball.ycor() > 680 :
        if(ball.bouncex == 5 and ball.bouncey ==5):
            ball.bounceup()
            print("chujgora")

        elif(ball.bouncex == -5 and ball.bouncey == 5):
            ball.bounceupwithouttouch()

    elif ball.ycor() < -680 :
        if(ball.bouncex == -5 and ball.bouncey == -5):
            ball.bouncedown()
            print("chujdol")
        elif(ball.bouncex == 5 and ball.bouncey == -5):
            ball.bouncedownwithouttouch()

    elif distleft < 50:
        if(randomliczba == 0):
            ball.bounceleft()
        elif(randomliczba == 1):
            ball.bounceup()

    elif distright < 50:
        if(randomliczba == 0):
            ball.bounceright()
        elif(randomliczba == 1):
            ball.bouncerightgora()

    elif ball.xcor() < -1300:
        ball.score()
        scoreboardr.show()

    elif ball.xcor() > 1300:
        ball.score()
        scoreboardl.show()





screen.exitonclick()
