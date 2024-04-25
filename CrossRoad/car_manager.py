import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
from random import Random
from player import Player
from scoreboard import Scoreboard


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.scoreboard = Scoreboard()

    def new_car(self):
        new_car = Turtle()
        new_car.shapesize(1,2.5)
        new_car.shape("square")
        random_number = random.randint(0,5)
        new_car.color(COLORS[random_number])
        random_y = random.randint(-200,270)
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(300,random_y)
        self.all_cars.append(new_car)


    def moving(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE*self.scoreboard.currentlevel)

    def carscore(self):
        self.scoreboard.scoreupdate()



