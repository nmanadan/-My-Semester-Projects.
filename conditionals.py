#conditional statements

#init
#functions


#challenge 1

#18 years old
#U.S. Cititzen
def vote_check():
    age=int(input("please enter your age:"))#input by default collects str
    uscitizen=input("are you are US citizen?")
    #process the data using conditional statements
    if age >= 18 and uscitizen== "yes": #evaluate to True or False #conditional statement<-
        print("congrats, you are eligable to vote")
    else:
        print(" you are NOT eligible to vote")


#Challenge 2

#prints the largest number (a,b, and c)
def max_num(a,b,c):
    if a>b and a>c:
        print("a is the largest, the value of a is: "+ str(a))
    if b>c and b>a:
        print("b is the largest, the value of a is: "+ str(b))
    if c>a and c>b:
        print("c is the largest, the value of a is: "+ str(c))




#challenege 3
#this challenge takes a score(integer) and translates to a grade (string)

def score():
    grade=int(input("please enter your grade"))
    if grade>= 90:
        print("your grade is an A, your grade is an " +str(grade))
    elif grade>= 80:
        print("your grade is an B, your grade is a " +str(grade))
    elif grade>= 70:
        print("your grade is an C, your grade is a " +str(grade))
    elif grade>= 60:
        print("your grade is an D, your grade is " +str(grade))
    else:
        print("your grade is an F, your grade is " +str(grade))





#main
vote_check()
max_num(1,2,3)
score()




