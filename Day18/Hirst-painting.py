#import colorgram

#colors = colorgram.extract('pallete.jpg', 10)
#rgb_colors= []

#for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
   # new_color = (r, g, b)
  #  rgb_colors.append(new_color)

#print(rgb_colors)


from turtle import Turtle, Screen
import random
#10x10 rows and collumns, 50 odstępu, 20 kolko

color_list = [(240, 242, 245), (223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93)]
tim = Turtle()
scr = Screen()
scr.colormode(255)
scr.setup(400,400)

#start pozycja
tim.penup()
tim.setx(-1200)
tim.sety(-650)
#tim.goto(-1100,-650)
timx = -1200
timy = -650
tim.speed("fastest")
#rysowanie kolka
def kolko():
    global timx,timy
    losowy_kolor = random.choice(color_list)
    tim.color(losowy_kolor)
    tim.pendown()
    tim.begin_fill()
    tim.circle(20,360)
    tim.end_fill()
    tim.penup()
    timx += 265
    if (timx == 1450):
        timx = -1200
        timy += 135
    tim.goto(timx,timy)



while 1 > 0:
    kolko()
    if (timy == 1350 and timx == 1450):
        break



#400x300



screen = Screen()
screen.exitonclick()