from guesser import Guesser
import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# po zgadnieciu niech dodaje do tablicy nowej i potem sprawdza czy w niej coś jest

df = pd.read_csv("50_states.csv")
# print(df)


guesser = Guesser()
state_blank = [] #pusta tablica na zgadniete juz stany
isgameon = True
states_tab = df.state.tolist() #lista stanów
score = 0


while isgameon:
    if score == 50:
        guesser.gg()
    else:
        answer_state = screen.textinput(title=f"Guess The State {score}/50", prompt="What's another state's name?").title()
        print(answer_state)
        guess = df[df.state == f"{answer_state}"]  # wyszukuje w db stan
        guess_state = guess.state.to_string().split("    ")
        guess_x = guess.x.to_string().split()
        guess_y = guess.y.to_string().split()
        print(guess_state)
        # print(guess_x)
        # print(guess_y)

        if answer_state in states_tab:
            state_blank.append(answer_state)
            score += 1
            guesser.state(guess_state[1],int(guess_x[1]),int(guess_y[1]))
        else:
            print("CHUJ2")


        #print(guess_state)






print(guess_state)







screen.exitonclick()