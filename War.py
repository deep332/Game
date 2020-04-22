import  random
import time

#READ RULES
def rules():
    fhand=open('rule.txt','r',encoding='utf-8')
    print(fhand.read())

#WELCOME STATEMENT
print("*"*15,"Welcome To The 'War' Game ","*"*15,"\nPlease View in Full Screen Mode")

#TO READ RULES
readMe=str(input("Do you Wish To read the Rules? (y/n):"))
if readMe=='y' or readMe=='Y':
    rules()
    intp=input("Press Enter to Start the Game")
elif readMe=='n' or readMe=='N':
    print("Good Let's get Going!")
    
#Name OF the player
name=str(input("Enter Player's Name:"))

#NUMBER OF PLAY CARDS
num=int(input("With how many Cards would you like play? b/w(3-26):"))
if num<3 or num>26:
    num=int(input("Enter valid Number between(3-26):"))

#DECIDING LEVEL
lvl=str(input("Do want to play blind or show? (b/s):"))

#Shuffling Cards
def shuffle(cards):
    print("_"*40)
    print("Shuffling Card Deck")
    random.shuffle(cards)
    time.sleep(3)
    return cards

#Main Function
def gameOn(name,num,lvl):
    #MAKING CARD DECK
    if lvl=='b' or lvl=='B':
        suite=['♥','♦','♣','♠']
    elif lvl=='s' or lvl=='S':
        print("=====TURN ON YOUR CAPSLOCK=====")
        suite=['H','D','C','S']
    ranks=['A','K','Q','J','10','9','8','7','6','5','4','3','2']
    card=[]
    card.append([x+y for x in suite for y in ranks])
    cards=card[0]
    print("Card Deck:\n",cards)
    #SHUFFLING CARDS
    shuffle(cards)
    PlayerCards=cards[:num]
    ComputerCards=cards[num:num+num]
    print("Cards Distributed {} Each".format(num))
    print("_"*40)
    print("Let the Game begin")
    Play(PlayerCards,ComputerCards,lvl,name)
        
#PLAY FUNCTION    
def Play(p,c,lvl,name):
    i=1
    while True:
        if len(p)==0:
            print("*** Computer has Won ***")
            playAgain()
            break
        elif len(c)==0:
            print("*** {} has Won ***".format(name))
            playAgain()
            break
        print("Round ",i)
        if lvl=='b' or lvl=='B':
            a=input("Press Enter to pick your Card")
            a=random.choice(p)
        elif lvl=='s' or lvl=='S':
            print("Your Cards:\n",p)
            a=input("Which card you wish to pick {}:".format(name))
        if a not in p:
            a=input("Enter valid card from the deck:")
        print("You Picked: {}".format(a))
        time.sleep(2)
        b=random.choice(c)
        print("Computer Picked: {}".format(b))
        time.sleep(2)
        #FUNCTION TO CHECK WHICH CARD IS GREATER
        check(a,b,p,c,name,lvl)
        print("Your remaining Cards {}".format(len(p)))
        print("Computer's remaining Cards {}".format(len(c)))
        print("-"*40)
        time.sleep(2)
        i+=1
        if i==20:
            print("-"*10,"This Game is becoming Intersteting","-"*10)
        elif i==35:
            print("-"*10,"Running out of patience now","-"*10)
        elif i>=55:
            print("-"*13,"Do Give up ??","-"*13)
            g=input("(y/n)")
            if g=='Y' or g=='y':
                print("You tried your best Thankyou {}".format(name))
                break
        if len(p)==1 and p[1:]=='A':
            print("Last Remaining Card of Player is 'A' and that being the biggest Card {} has Won the game".format(name))
            playAgain()
            break
        elif len(c)==1 and c[1:]=='A':
            print("Last Remaining Card of Player is 'A' and that being the biggest Card Computer has Won the game")
            playAgain()
            break
        elif len(c)==len(p) and p[1:]==c[1:]:
            print("It's a Draw as both have same cards available")
            playAgain()
            break
               
#CHECK CARDS FOR BIGGEST
def check(a,b,p,c,name,lvl):
    p1=a[1:]
    c1=b[1:]
    #CHECKING FOR NUMBER CARD
    if p1.isdigit() and c1.isdigit():
        p1=int(a[1:])
        c1=int(b[1:])
        if p1 > c1:
            plyr(a,b,p,c,name)
        elif p1 < c1:
            cmp(a,b,p,c,name)
        elif p1==c1:
            war(a,b,p,c,name,lvl)
    #CHECKING FOR KQJA WITH NUMBER
    elif p1.isalpha() and c1.isdigit():
        plyr(a,b,p,c,name)
    elif c1.isalpha() and p1.isdigit():
        cmp(a,b,p,c,name)
    #Checking for (ACE,KING, QUEEN,JACK)
    elif p1.isalpha() and c1.isalpha():
        #CHECK FOR A
        if p1=='A':
            if c1=='A':
                war(p1,c1,p,c,name,lvl)
            else:
                plyr(a,b,p,c,name)
        #CHECK FOR K
        if p1=='K':
            if c1=='Q' or c1=='J':
                plyr(a,b,p,c,name)
            elif c1=='A':
                cmp(a,b,p,c,name)
            elif c1=='K':
                war(a,b,p,c,name,lvl)
        #CHECK FOR Q
        elif p1=='Q':
            if c1=='J':
                plyr(a,b,p,c,name)
            elif c1=='K' or c1=='A':
               cmp(a,b,p,c,name)
            elif c1=='Q':
                war(a,b,p,c,name,lvl)
        #CHECK FOR J
        elif p1=='J':
            if c1=='K' or c1=='Q' or c1=='A':
                cmp(a,b,p,c,name)
            elif c1=='J':
                war(a,b,p,c,name,lvl)

#PLAYER WON
def plyr(a,b,p,c,name):
    print("{} you won this round!".format(name))
    p.append(b)
    c.remove(b)

#COMPUTER WON
def cmp(a,b,p,c,name):
     print("Computer won this round!")
     c.append(a)
     p.remove(a)

#PLAY AGAIN FUNCTION
def playAgain():
    a=input("Do you Wish to Play Again? (y/n):")
    if a=='y' or a=='Y':
        name=input("Enter Palyers name:")
        num=int(input("With how many Cards would you like play? b/w(3-26)"))
        lvl=input("Do want to play blind or show? (b/s):")
        gameOn(name,num,lvl)
    else:
        a=input("Press Enter to Exit")

def war(a,b,p,c,name,lvl):
    p.remove(a)
    c.remove(b)
    print("","="*20,"\n It's a War\n","="*20)
    if lvl=='b' or lvl=='B':
        print("Pick a show card\nYour Show card",p)
        p1=input("Enter the card you want to pick:")
    elif lvl=='s' or lvl=='S':
        p1=input("Pick one Blind Cards\nPress Enter to pick Blind card {}:".format(name))
        p1=random.choice(p)
    print("You Picked: {}".format(p1))
    time.sleep(2)
    c1=random.choice(c)
    print("Computer Picked : {}".format(c1))
    check(p1,c1,p,c,name,lvl)
    
#CALLING MAIN FUNCTION
gameOn(name,num,lvl)
