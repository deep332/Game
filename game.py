import random
print("***********Welcom to the Code Breaker Game***********\nyou have to guess the three digit number genreated by the Computer\nSo let's begin ! Good Luck\n---------------------------------------------------------------------------\nThe Code has been Generated")
name=input("Player Name:")

#generating Random NUmber
def randomNo():
    rand=['0','1','2','3','4','5','6','7','8','9']
    random.shuffle(rand)
    return rand[:3]

#Main Function
def gameOn():
        i=0
        rnum=randomNo()
        rnumstr = ''.join([str(elem) for elem in rnum])
        lvl=str(input("Choose your level: Easy or Hard:"))
        if lvl == 'Easy' or lvl=='easy' or lvl == 'Hard' or lvl=='hard':
            #Iteration
            while(True):
                print("You have {} Attempts left".format(10-i))
                 #User Input
                num1=str(input("Enter your Guess for the Three Digit Code:"))
                #Checking If Three Digit Or Not
                if len(num1)<=2 or len(num1) >= 4:
                    num1=str(input("You have to Enter Three Digit Code:"))
                i+=1
                if lvl == 'Easy' or lvl=='easy':
                    checkNum(num1,rnum)
                elif lvl == 'Hard' or lvl=='hard':
                    checkingNumber(num1,rnum,rnumstr)
                #Game Over Condition
                if i>9:
                    print("*******Game Over******* \nHard luck {} try again :(\nThe Computer Genereated Code was '{}'".format(name,rnumstr))
                    playAgain()
                    break
                #break Conditon
                if list(num1)==rnum:
                    if i==1 or i==2:
                        print("You won! \nYou Craked the code in {} attempts You're a Genius {}".format(i,name))
                    elif i<5:
                        print("You won! \nYou Craked the code in {} attempts {}".format(i,name))
                    elif i<10:
                        print("You won! \nYou Craked the code in {} attempts {} but you took to long to crack it".format(i,name))
                    playAgain()
                    break
        else:
            print("Invalid Level Name\n Please Restart and enter proper level")
            playAgain()

    
#Checking Number
def checkNum(num1,rnum):
    checkFirst(num1[0],rnum[0])
    checkSecond(num1[1],rnum[1])
    checkThird(num1[2],rnum[2])
    print("_________________________________________________")

#Checking all Number at Once
def checkingNumber(num1,rnum,rnumstr):
    if num1==rnumstr:
        print("Code Cracked On hard level")
    elif (int(rnumstr)-20) <= int(num1) <= (int(rnumstr)+20):
        print("You're close Keep Guessing")
    else:
        print("Wrong Guess Try Agian :(")
    print("_________________________________________________")

#Checking First Number
def checkFirst(a,b):
    if a==b:
        print("You got 1st number right")
    elif   int(b)-2 <= int(a) <=int(b)+2:
        print("1st Number- You're close Keep Guessing")
    else:
        print("1st Number- Wrong Guess Try Agian :(")

#Checking Second Number
def checkSecond(a,b):
    if a==b:
        print("You got 2nd number right")
    elif   int(b)-2 <= int(a) <=int(b)+2:
        print("2nd Number- You're close Keep Guessing")
    else:
        print("2nd Number- Wrong Guess Try Agian :(")

#Checking Third Number
def checkThird(a,b):
    if a==b:
        print("You got 3rd number right")
    elif   int(b)-2 <= int(a) <=int(b)+2:
        print("3rd Number- You're close Keep Guessing")
    else:
        print("3rd Number- Wrong Guess Try Agian :(")

#Play Again ?
def playAgain():
    a=input("Do you Wish to Play Again? (y/n):")
    if a=='y' or a=='Y':
        gameOn()
    else:
        a=input("Press Enter to Exit")
#Calling Mian Game Function
gameOn()

