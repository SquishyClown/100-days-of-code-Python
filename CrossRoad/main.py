import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move,"Up")

#cars
carmanager = CarManager()
carall = []


game_is_on = True
opoznienie = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    opoznienie += 1
    if(opoznienie%7 == 0):
        carmanager.new_car()
    carmanager.moving()
    if(player.ycor() > 280):
        player.levelfinished()
        carmanager.carscore()
    #kolizja
    for kolizja in carmanager.all_cars:
        if(player.distance(kolizja) < 25):
            print("game over")
            game_is_on = False






