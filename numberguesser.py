#guessing game
#init
import random
guess=int(input("welcome to the number guesser game. you are trying to guess the correct integer 1-10"))
secret=random.randint(0,10)

#functions
def numberguesser():

    if guess==secret:
        print("congrats you guessed the correct number")

    elif guess>secret:
        print("too high."+ " "+ "the number was,"+ " " + str(secret))
    elif secret>guess:
        print("too low." + " "+ "the number was,"+ " " + str(secret))

#main
numberguesser()
