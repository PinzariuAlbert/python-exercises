import random
money=18
plots = []
def checkInteractable(row, col):
    if(not str(row).isdigit() or not str(col).isdigit()):
        print("Error: Something wasn't inputed correctly!")
        return False
    elif(int(row)>4 or int(col)>9 or int(row)<1 or int(col)<1):
        print("Error: Something wasn't inputed correctly!")
        return False
    else:
     return True
    
class Plot():
    def __init__(self,row,col,display_value=0, value=0, bugged=False):
        self.display_value=0  #uhhh, dont forget to use [ print(str(variable).zfill(2)) ]
        self.value=0
        self.bugged=bugged
        self.row=row
        self.col=col
        self.protection=1
        self.seed=""
    def plant(self, seed):
            global money
            self.seed=seed
            if(seed=="wheat" or seed=="5"):
                if(money>=20):
 #           if(self.value!=5):
                    money-=20
                    self.value=5
                    self.maxvalue=40
                else: print("You need more money!")   
            elif(seed=="carrot" or seed=="4"):
                if(money>=15):
                    money-=15
                    self.value=4
                    self.maxvalue=32
                else: print("You need more money!")   
            elif(seed=="cucumber" or seed=="3"):
                if(money>=11):
                    money-=11
                    self.value=3
                    self.maxvalue=27
                else: print("You need more money!")   
            elif(seed=="celery" or seed=="2"):
                if(money>=8):
                    money-=8
                    self.value=2
                    self.maxvalue=16
                else: print("You need more money!")   
            elif(seed=="potato" or seed=="1"):
                if(money>=3):
                    money-=3
                    self.value=1
                    self.maxvalue=7  
                else: print("You need more money!")   
            else: 
                print("Seed aint real")
                self.seed=""
            self.display_value=self.value
    def harvest(self, row, column):
        if(self.seed!=""):
         if(self.value==self.maxvalue):
           global money
           money+=self.value
           self.value=0
           self.display_value=0
           self.seed=""
        else: print("Cant harvest")
    def bug(self):
        self.protection-=1
        self.bugged=True
        rnd= random.randint(0,3)
        if(rnd==0): 
            self.display_value="~#"
        elif(rnd==1):
            self.display_value="*/"
        else:self.display_value="&^"
    def debug(self):
        self.bugged=False
        self.display_value=self.value
    def grow(self):
       # print("tried to grow")
        if(self.bugged==True and self.protection!=0):
            self.protection-=1
        elif self.bugged==True and self.protection==0:
            self.value=0
            self.display_value=0
            self.seed=0
            self.protection=1
            if(plots[self.row-1][self.col] and plots[self.row-1][self.col].value!=0):
                 plots[self.row-1][self.col].protection=2 ; plots[self.row-1][self.col].bug()
            if(plots[self.row][self.col-1] and plots[self.row][self.col-1].value!=0):
                 plots[self.row][self.col-1].protection=2 ; plots[self.row][self.col-1].bug()
            if(plots[self.row+1][self.col] and plots[self.row+1][self.col].value!=0):
                 plots[self.row+1][self.col].protection=2 ; plots[self.row+1][self.col].bug()
            if(plots[self.row][self.col+1] and plots[self.row][self.col+1].value!=0):
                 plots[self.row][self.col+1].protection=2 ; plots[self.row][self.col+1].bug()
            self.bugged=False
        elif self.value!=0:
         if(self.value<self.maxvalue):
            #put all the crop stuff here
            if(self.seed=="wheat" or self.seed=="5"):
             self.value+=5
            #elif(self.value%4==0 and self.value!=0 and (self.value+16)/len(self.seed)<len(self.seed)):     what was i even doing here...bs
            elif(self.seed=="carrot" or self.seed=="4"):
             self.value+=4
            elif(self.seed=="cucumber" or self.seed=="3"):
             self.value+=3
            elif(self.seed=="celery" or self.seed=="2"):
             self.value+=2
            elif(self.seed=="potato" or self.seed=="1"):
             self.value+=1
            #this part of the else is only related to "bugs"
            rnd_buggin= random.randint(0,25)
            if(rnd_buggin==0):
                self.bug()
            else:
                self.display_value=self.value
        
game=True
for i in range(4):
    row=[]
    for j in range(9):
        row.append(Plot(i,j))
    plots.append(row)
command=input("command:")
if(command=="stop"):
    game=False

while(game==True):
 if(command=="show" or command=="s"):
    for i in plots:
        for j in i:
            print(str(j.display_value).zfill(2), end=" ")
        print()

 elif(command=="plant" or command=="p"):
    row_coord=input("row coordinate: ")
    collumn_coord=input("collumn coordinate: ")
    if(checkInteractable(row_coord,collumn_coord)): 
     seed_type=input("seed type: ")
     plots[int(row_coord)-1][int(collumn_coord)-1].plant(seed_type)

 elif(command=="next" or command==""):
    for i in range(4):
        for j in range(9):
            plots[i][j].grow()

 elif(command=="harvest" or command=="h"):
    row_coord=input("row coordinate: ")
    collumn_coord=input("collumn coordinate: ")
    if(checkInteractable(row_coord,collumn_coord)): 
     plots[int(row_coord)-1][int(collumn_coord)-1].harvest(int(row_coord),int(collumn_coord))

 elif(command=="debug" or command=="d"):
    row_coord=input("row coordinate: ")
    collumn_coord=input("collumn coordinate: ")
    if(checkInteractable(int(row_coord),int(collumn_coord))): 
     plots[int(row_coord)-1][int(collumn_coord)-1].debug()

 elif(command=="mone"):
    print(money)
 command=input("command: ")
 if(command=="stop"):
    game=False
