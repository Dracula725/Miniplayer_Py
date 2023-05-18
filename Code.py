import time
import random
def my_sort(line):
            line_fields = line.split(' ')
            amount = int(line_fields[3])
            return amount
def guess(count,num):
    print("you have chosen 'Guess the number'")
    list=[]
    for i in range(1,num+1):
            list.append(i)
    a=random.choice(list)
    b=int(input("enter a number in between 1 to {} \n".format(num)))
    if(a==b):
        print("you have guessed correctly")
        print(a)
    else:
        print("nope")
        print(a)
        count+=1
    if(count==3):
        print("you lost 3 times lol, wanna change the range?\n1)Yes\n2)No")
        c=int(input("enter your choice: "))
        if(c==1):
            x=int(input("enter range :"))
            guess(count,x)
        elif(c==2):
            print("visit again")
    print("do you want to play again? :\n1)Yes\n2)Nope")
    again=int(input("enter choice:"))
    if(again==1):
        guess(count,num)
    else:
        print("thank you for playing")
        
def handcricket():
    print("WELCOME TO HAND CRICKET")
    print("-----------------------")
    print("TIME TO TOSS")
    toss=eval(input("Take a number for toss in[1,2]:"))
    l=[1,2]
    l2=[1,2,3,4,5,6]
    if(toss==random.choice(l)):
        charge1=input("Enter ball or bat:")
    else:
        a=1
        if(a==random.choice(l)):
            charge1="ball"
        else:
            charge1="bat"
    print("\n\n","HUMAN NEED TO:",charge1,"\n\n")
    human=0
    comp=1
    targeth,targetc=0,0
    while(comp!=human):
        if(charge1=="ball"):
            human=eval(input("Enter a no[1,6]:"))
            
            comp=random.choice(l2)
            print("computer number is:",comp)
            targetc+=comp
            if(human==comp):
                charge2="bat"
                print("The human target is:",targetc+1)
        elif(charge1=="bat"):
            human=eval(input("Enter a no[1,6]:"))
            comp=random.choice(l2)
            print("computer number is:",comp)
            targeth+=human
            if(human==comp):
                charge2="ball"
                print("The computer target is:",targeth+1)
    human=0
    comp=1
    print("\n\n","HUMAN NEED TO:",charge2,"\n\n")
    while(comp!=human):
        if(charge2=="ball"):
            human=eval(input("Enter a no[1,6]:"))
            comp=random.choice(l2)
            print("computer number is:",comp)
            targetc+=comp
            if(targetc>targeth):
                break
        elif(charge2=="bat"):
            human=eval(input("Enter a no[1,6]:"))
            comp=random.choice(l2)
            print("computer number is:",comp)
            targeth+=human
            if(targeth>targetc):
                break
    print("total runs of human:",targeth)
    print("total runs of computer:",targetc)
    if(targetc>targeth):
        print("\n\n\tCOMPUTER WON THE MATCH\t\n\n")
    elif(targeth>targetc):
        print("\n\n\tHUMAN WON THE MATCH\t\n\n")
    else:
        print("\n\n\t MATCH TIED \t\n\n")
        

def quiz():
    print("Welcome to Quizzz\n")
    count=0
    name=str(input("Enter your name : "))
    time.sleep(1)
    print("For this Quizzz the Topics are :\n1)Movies\n2)Sports\n3)History\n4)Science\n5)Food and Nutrition\n")
    quiz=int(input("Enter your choice (1 to 5) : "))
    if(quiz==1):
        print("\nMovie Quizzz\n")
        print("Gathering Questions...\n")
        time.sleep(3)
        print("Which was the first Indian movie to win an Oscar? :")
        print("a)Slumdog Millionaire\nb)Mother India\nc)Gandhi\nd)None of above\n")
        opt=str(input("Enter option : "))
        if(opt=='b'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("What is the first movie in India? :")
        print("a)Raja Harishchandra\nb)Alam Ara\nc)Mother India\nd)Kisan Kanya\n")
        opt=str(input("Enter option : "))
        if(opt=='a'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("Who is known as Father of Indian Cinema? :")
        print("a)Charan Singh\nb)Raja Lalith Rai\nc)Dhundiraj Govind Phalke\nd)Balram Naidu\n")
        opt=str(input("Enter option : "))
        if(opt=='c'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("How many times AR Rahman was nominated for Oscar? :")
        print("a)4 time(s)\nb)3 time(s)\nc)1 time(s)\nd)2 time(s)\n")
        opt=str(input("Enter option : "))
        if(opt=='d'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("Who is the father of Telugu Film Industry? :")
        print("a)Rama Naidu\nb)Annapurna Devi\nc)Raghupati Venkaiah Naidu\nd)Krishnam Reddy\n")
        opt=str(input("Enter option : "))
        if(opt=='c'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        print("Adding up ur score...\n")
        time.sleep(2)
        print("Your score is {}".format(count))
        
        
        
    elif(quiz==2):
        print("\nSports Quizzz\n")
        print("Gathering Questions...\n")
        time.sleep(3)
        print("Who among the gollowing is known as 'Flying Sikh of India' :")
        print("a)Kapil Dev\nb)P.T.Usha\nc)Joginder Singh\nd)Milkha Singh\n")
        opt=str(input("Enter option : "))
        if(opt=='d'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("Which animal represented in the mascot of Delhi Asian Games 1982? :")
        print("a)Tiger\nb)Lion\nc)Elephant\nd)Panda\n")
        opt=str(input("Enter option : "))
        if(opt=='c'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("In Basket Ball how many players are there in each side? :")
        print("a)5\nb)7\nc)9\nd)6\n")
        opt=str(input("Enter option : "))
        if(opt=='a'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("National Sports Day is celebrated on? :")
        print("a)12th November\nb)29th August\nc)30th November\nd)28th November\n")
        opt=str(input("Enter option : "))
        if(opt=='b'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("The Headquarters of International Cricket Council is located in the city :")
        print("a)London\nb)Mumbai\nc)Melbourne\nd)Dubai\n")
        opt=str(input("Enter option : "))
        if(opt=='d'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        print("Adding up ur score...\n")
        time.sleep(2)
        print("your score is {}".format(count))
        
        
        
    elif(quiz==3):
        print("\nHistory Quizzz\n")
        print("Gathering Questions...\n")
        time.sleep(3)
        print("Who is believed to be the reason World War 2 started? :")
        print("a)Sun Min Chui\nb)Chiang Kai Shek\nc)Adolf Hitler\nd)Mao Zedong\n")
        opt=str(input("Enter option : "))
        if(opt=='c'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("Who Wrote 'Vande Mataram'? :")
        print("a)Bhagat Singh\nb)Mahatma Gandhi\nc)Rabindranath Tagore\nd)Bankin Chandra Chatterjee\n")
        opt=str(input("Enter option : "))
        if(opt=='d'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("From which word the name India Originated? :")
        print("a)Iditarod\nb)Indus\nc)Yamuna\nd)Ganga\n")
        opt=str(input("Enter option : "))
        if(opt=='b'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("The first British Presidency in India was established at :")
        print("a)Madras\nb)Rajasthan\nc)Surat\nd)Bengal\n")
        opt=str(input("Enter option : "))
        if(opt=='c'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("In which year Swadeshi Movement started in India? :")
        print("a)1911\nb)1890\nc)1945\nd)1905\n")
        opt=str(input("Enter option : "))
        if(opt=='b'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        print("Adding up ur score...\n")
        time.sleep(2)
        print("your score is {}".format(count))   
            
            
    elif(quiz==4):
        print("\nScience Quiz\n")
        print("Gathering Questions...\n")
        time.sleep(3)
        print("Which of the following is a non metal that remains in Liquid state ar room temperature? :")
        print("a)Phosporous\nb)Bromine\nc)Chlorine\nd)Helium\n")
        opt=str(input("Enter option : "))
        if(opt=='b'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("Which material is used in making pencils? :")
        print("a)Graphite\nb)Silicon\nc)Charcoal\nd)Phosporous\n")
        opt=str(input("Enter option : "))
        if(opt=='a'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("Which of the following gases is not a Green House gas? :")
        print("a)Methane\nb)Hydrogen\nc)Nitrous Oxide\nd)Carbon Dioxide\n")
        opt=str(input("Enter option : "))
        if(opt=='b'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("The group of metals Iron(Fe)/Cobalt(Co)/Nickel(Ni) may best called as :")
        print("a)Transition Metals\nb)Main Group Metals\nc)Alkali Metals\nd)Carbon Dioxide\n")
        opt=str(input("Enter option : "))
        if(opt=='b'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("Which of the following is most soluble in water :")
        print("a)Camphor\nb)Common Salt\nc)Sugar\nd)Sulphur\n")
        opt=str(input("Enter option : "))
        if(opt=='c'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        print("Adding up ur score...\n")
        time.sleep(2)
        print("your score is {}".format(count))    
            
            
    elif(quiz==5):
        print("\nFood and Nutrition Quizzz\n")
        print("Gathering Questions...\n")
        time.sleep(3)
        print("Which of the following helps to maintain a constand body temperature? :\n")
        print("a)Roughage\nb)Vitamin\nc)Water\nd)Proteins\n")
        opt=str(input("Enter option : "))
        if(opt=='c'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("Night Blindness is caused by the deficiency of? :\n")
        print("a)Vitamin C\nb)Vitamin D\nc)VItamin B1\nd)Vitamin A\n")
        opt=str(input("Enter option : "))
        if(opt=='d'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("The food component present in Sugar is? :\n")
        print("a)Fats\nb)Proteins\nc)Vitamins\nd)Carbohydrates\n")
        opt=str(input("Enter option : "))
        if(opt=='d'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("Which is essential for forming Haemoglobin in the blood? :\n")
        print("a)Calcium\nb)Iron\nc)Phosporous\nd)Magnesium\n")
        opt=str(input("Enter option : "))
        if(opt=='b'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        time.sleep(1)
        print("Excessive body weight due to overnutrition leads to :\n")
        print("a)Rickets\nb)Maramus\nc)Obesity\nd)Kwashiorker\n")
        opt=str(input("Enter option : "))
        if(opt=='c'):
            print("Your answer is correct\n")
            count+=1
        else:
            print("Your answer is wrong\n")
        print("Adding up ur score...\n")
        time.sleep(2)
        print("your score is {}".format(count))
        
    file=open("score.txt","a+")
    file.write("{} got score {} \n".format(name,count))
    file.close()
    print("Do you want to see previous scores?")
    choice=str(input("Enter Yes or No : \n"))
    if(choice=='yes' or choice=='Yes'):
        print("Reading files...\n")
        time.sleep(2)
        fp = open('score.txt',"r+")
        contents = fp.readlines()
        contents.sort(key=my_sort)
        contents.reverse()
        for i in contents:
            print(i)
        fp.close()
    else:
        print()
    print("Thank You for Playing")
    
class ttt:
    def __init__(self):
        self.board=[]
    def makeboard(self):
        for i in range(3):
            row=[]
            for j in range(3):
                row.append("-")
            self.board.append(row)
    def showboard(self):
        for row in self.board:
            for i in row:
                print(i,end=" ")
            print()
    def wincondition(self,player):
        win=None
        n=len(self.board)
        for i in range(n):
            win=True
            for j in range(n):
                if self.board[i][j]!=player:
                    win=False
                    break
            if win:
                return win
        for i in range(n):
            win=True
            for j in range(n):
                if self.board[j][i]!=player:
                    win=False
                    break
            if win:
                return win
        win=True
        for i in range(n):
            if self.board[i][i]!=player:
                win=False
                break
        if win:
            return win
        win=True
        for i in range(n):  
            if self.board[i][n-1-i]!=player:
                win=False
                break
        if win:
            return win
        return False
        for row in self.board:
            for i in row:
                if(i=='-'):
                    return False
        return True
    def seto(self,row,col,player):
        self.board[row][col]=player
    def full(self):
        for row in self.board:
            for i in row:
                if i == '-':
                    return False
        return True
    def swap(self,player):
        return 'X' if player=='O' else 'O'
    def begin(self):
        self.makeboard()
        player='X'
        while(True):
            print("player ",player," turn\n")
            self.showboard()
            row, col = list(
                map(int, input("Enter row and column numbers (row*space*column) format: ").split()))
            print()
            self.seto(row - 1, col - 1, player)
            if self.wincondition(player):
                print(f"Player {player} wins the game!")
                break
            if self.full():
                print("Match Draw!")
                break
            player = self.swap(player)
        print()
        self.showboard()

print("Hello and welcome to MINIPLAYER\n")
print("Available games are :\n")
print("1)Guess the number\n2)Hand Cricket\n3)Quizzz\n4)TicTacToe")
choice=int(input("Enter your choice : "))
if choice==1:
           count=0
           print("you have chosen Guess the number\n")
           num=int(input("enter range(1 to n), you are entering n: \n"))
           print("Loading game...\n")
           time.sleep(5)
           guess(count,num)
elif(choice==2):
           print("You have chosen Hand Cricket\n")
           print("Loading game...\n")
           time.sleep(5)
           handcricket()
elif(choice==3):
           print("You have chosen Quizzz")
           print("Loading game...\n")
           time.sleep(5)
           quiz()
elif(choice==4):
           print("You have chosen TicTacToe")
           print("Loading game...\n")
           time.sleep(5)
           obj=ttt()
           obj.begin()

else:
    print("Enter valid number")
           
