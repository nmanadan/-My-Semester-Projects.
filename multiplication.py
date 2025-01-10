#Neil Manadan
#init
import random #this imports the random



#fucntions
def multiplicationquiz():
    print("welcome to the multiplication quiz. Answer as many questions correctly as possible")

    score=0#start this to store the score
    number_of_questionsanswered=0#start this to store the nubmer of questions
    question_count=5 #varaible that counts questions remaining

    while(question_count>0):#keeps the program running until it gets to zero

        number1=random.randint(1,9)#this gives the first number in the multiplication problem random integers 1-9
        number2=random.randint(1,9)#this gives the first number in the multiplication problem random integers 1-9

        ans=int(input("what is " + str(number1) + "times " + str(number2))) #this asks the user what the answer of number 1 times number 2 is
        #put str  before the numbers

        correct=number1*number2 #this creates a variable that checks the answer

        if ans==correct:
            print("your answer is correct")
            score+=1 #when the answer is corret add 1
            number_of_questionsanswered+=1 #number of questions has increased
            question_count-=1#every time a question is generated, subtracts 1 from the while loop
        else:
            print("your answer is inccorect")
            number_of_questionsanswered+=1 #number of questions has increased
            question_count-=1#every time a question is generated, subtracts 1 from the while loop

    print("your score is: " + str(score))#put this outside of the while loop bc feedback on quiz score is given after quiz is done
    print("the number of questions you answered is: " + str(number_of_questionsanswered))


#main
multiplicationquiz()
