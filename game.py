import random
print("Welcom to the Code Breaker Game\nyou have to guess the three digit number genreated by the Computer\nSo let's begin ! Good Luck\n---------------------------------------------------------------------------\nThe Code has been Generated")
name=input("Player Name:")
#generating Random NUmber
def randomNo():
    randNumber=[]
    for x in range(0,3):
        a=random.choice(['0','1','2','3','4','5','6','7','8','9'])
        randNumber.append(a)
    return randNumber
rnum=randomNo()

#Main Function
def gameOn():
    i=0
    #Iteration
    while(True):
        #User Input
        num1=str(input("Enter your Guess for the Three Digit Code:"))
        #Checking If Three Digit Or Not
        if 2 <= len(num1) >= 4:
            num1=str(input("You have to Enter Three Digit Code:"))
        i+=1
        checkNum(num1,rnum)
        #break Conditon
        if list(num1)==rnum:
            if i==1 or i==2:
                print("You won! \nYou Craked the code in {} attempts You're a Genius {}".format(i,name))
            elif i<10:
                print("You won! \nYou Craked the code in {} attempts but you took to long to crack it".format(i))
            else:
                print("*****Game Over*****")
            break;

#Checking Number
def checkNum(num1,rnum):
    checkFirst(num1[0],rnum[0])
    checkSecond(num1[1],rnum[1])
    checkThird(num1[2],rnum[2])
    print("_________________________________________________")
    
#Checking First Number
def checkFirst(a,b):
    if a==b:
        print("You got 1st number right")
    elif   int(b)-2 <= int(a) <=int(b)+2:
        print("You're close Keep Guessing for 1st Number")
    else:
        print("Wrong Guess Try Agian :(")

#Checking Second Number
def checkSecond(a,b):
    if a==b:
        print("You got 2nd number right")
    elif   int(b)-2 <= int(a) <=int(b)+2:
        print("You're close Keep Guessing for 2nd Number")
    else:
        print("Wrong Guess Try Agian :(")

#Checking Third Number
def checkThird(a,b):
    if a==b:
        print("You got 3rd number right")
    elif   int(b)-2 <= int(a) <=int(b)+2:
        print("You're close Keep Guessing 3rd Number")
    else:
        print("Wrong Guess Try Agian :(")

#Calling Mian Game Function
gameOn()
