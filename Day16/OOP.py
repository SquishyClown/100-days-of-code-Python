#import turtle

#timmy = turtle.Turtle()
#print(timmy)
#timmy.shape("turtle")
#timmy.color("coral")
#timmy.forward(100)


#my_screen = turtle.Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon",["Pikachu", "Squirtle", "Toronto"])
table.add_column("Type" ,["Electric","Fire","Psychic"])
table.align= "l"
print(table)