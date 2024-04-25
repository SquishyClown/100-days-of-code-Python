pricelist = """
+----------------------------------+---------+
|           Product                |  Price  |
+----------------------------------+---------+
| espresso                         | $1.5    |
| latte                            | $2.5    | 
| cappuccino                       | $3.0    |
+----------------------------------+---------+
"""


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 2.5
}



def choice():
    global coffeechoice
    print(pricelist)
    coffeechoice = input("What would you like to order? (espresso/latte/cappucino) ")

koniec = "nie"

while(koniec == "nie"):

    choice()


    waterreq = 0
    milkreq = 0
    coffeereq = 0
    moneytoadd = 0
    reszta = 0

    if(coffeechoice=="report"):
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffe: {resources['coffee']}")
        print(f"Money: {resources['money']}")

    elif(coffeechoice=="off"):
        koniec = "tak"


    elif coffeechoice == "espresso":
        waterreq = MENU["espresso"]["ingredients"]["water"]
        milkreq = 0
        coffeereq = MENU["espresso"]["ingredients"]["coffee"]
        if(waterreq > resources["water"] or milkreq > resources["milk"] or coffeereq > resources["coffee"]):
            print("Sorry there's no enough resources")
        else:
            print("Insert coins:")
            quartersinsert = int(input("How many quarters?"))
            dimesinsert = int(input("How many dimes?"))
            nicklesinsert = int(input("How many nickles?"))
            penniesinsert = int(input("How many pennies?"))
            suma = quartersinsert*0.25 + dimesinsert*0.10 + nicklesinsert*0.05 + penniesinsert*0.01
            if (suma > MENU["espresso"]["cost"]):
                resources["money"] += suma
                reszta = suma - MENU["espresso"]["cost"]
                resources["money"] -= reszta
                print(f"Here's {reszta} dollars in change")
                resources["water"] -= waterreq
                resources["milk"] -= milkreq
                resources["coffee"] -= coffeereq
                print("Enjoy your espresso!")
            elif (suma == MENU["espresso"]["cost"]):
                resources["money"] += suma
            elif (suma < MENU["espresso"]["cost"]):
                print("Sorry that's not enough money. Money refunded")


    elif coffeechoice == "latte":
        waterreq = MENU["latte"]["ingredients"]["water"]
        milkreq = MENU["latte"]["ingredients"]["milk"]
        coffeereq = MENU["espresso"]["ingredients"]["coffee"]
        if (waterreq > resources["water"] or milkreq > resources["milk"] or coffeereq > resources["coffee"]):
            print("Sorry there's no enough resources")
        else:
            print("Insert coins:")
            quartersinsert = int(input("How many quarters?"))
            dimesinsert = int(input("How many dimes?"))
            nicklesinsert = int(input("How many nickles?"))
            penniesinsert = int(input("How many pennies?"))
            suma = quartersinsert * 0.25 + dimesinsert * 0.10 + nicklesinsert * 0.05 + penniesinsert * 0.01
            if(suma > MENU["latte"]["cost"]):
                resources["money"] += suma
                reszta = suma - MENU["latte"]["cost"]
                resources["money"] -= reszta
                print(f"Here's {reszta} dollars in change")
                resources["water"] -= waterreq
                resources["milk"] -= milkreq
                resources["coffee"] -= coffeereq
                print("Enjoy your latte!")
            elif(suma == MENU["latte"]["cost"]):
                resources["money"] += suma
            elif (suma < MENU["latte"]["cost"]):
                print("Sorry that's not enough money. Money refunded")


    elif coffeechoice == "cappuccino":
        waterreq = MENU["cappuccino"]["ingredients"]["water"]
        milkreq = MENU["cappuccino"]["ingredients"]["milk"]
        coffeereq = MENU["cappuccino"]["ingredients"]["coffee"]
        if (waterreq > resources["water"] or milkreq > resources["milk"] or coffeereq > resources["coffee"]):
            print("Sorry there's no enough resources")
        else:
            print("Insert coins:")
            quartersinsert = int(input("How many quarters?"))
            dimesinsert = int(input("How many dimes?"))
            nicklesinsert = int(input("How many nickles?"))
            penniesinsert = int(input("How many pennies?"))
            suma = quartersinsert * 0.25 + dimesinsert * 0.10 + nicklesinsert * 0.05 + penniesinsert * 0.01
            if (suma > MENU["cappuccino"]["cost"]):
                resources["money"] += suma
                reszta = suma - MENU["cappuccino"]["cost"]
                resources["money"] -= reszta
                print(f"Here's {reszta} dollars in change")
                resources["water"] -= waterreq
                resources["milk"] -= milkreq
                resources["coffee"] -= coffeereq
                print("Enjoy your cappucino!")
            elif (suma == MENU["cappuccino"]["cost"]):
                resources["money"] += suma
            elif (suma < MENU["cappuccino"]["cost"]):
                print("Sorry that's not enough money. Money refunded")




