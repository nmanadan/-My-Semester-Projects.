#neil
#1/6
#rock paper scissors

#init
import random
#functions
#main
def game():
    print("welcome to rock paper scissors")
    computer_win=0
    human_win=0
    while True:
        human=input("select rock, paper, or scissors")
        if human=="quit":
                break
        computer=random.randint(1,3)
        if computer==1:
                computer="rock"
        if computer==2:
                computer="paper"
        if computer==3:
                computer="scissors"
        if computer==human:
                print("tie")
        if human=="rock" and computer=="paper":
                print("you lose")
                computer_win+=1
        if human=="rock" and computer=="scissors":
                print("you win")
                human_win+=1
        if human=="paper" and computer=="rock":
                print("you win")
                human_win+=1
        if human=="paper" and computer=="scissors":
                print("you lose")
                computer_win+=1
        if human=="scissors" and computer=="rock":
                print("you lose")
                computer_win+=1
        if human=="scissors" and computer=="paper":
                print("you win")
                human_win+=1
        print("you chose "+ str(human)+ " and the computer chose "+ str(computer)+ ".")
        print("player wins= " + str(human_win) + " computer wins= " + str(computer_win))
game()
