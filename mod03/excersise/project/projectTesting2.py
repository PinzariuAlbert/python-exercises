import random
money=0
plots = []
def checkInteractable(row, col):
    if(row>4 or collumn>9 or row!=int or collumn!=int or row=="" or collumn!=""):
        print("Error: Something wasn't inputed correctly!")
        return False
    return True
    
class Plot():
    def __init__(self,row,col,display_value=0, value=0, bugged=False):
        self.display_value=0  #uhhh, dont forget to use [ print(str(variable).zfill(2)) ]
        self.value=0
        self.bugged=bugged
        self.row=row
        self.col=col
        self.protection=1
    def plant(self, seed):
        self.seed=seed
        if(seed=="wheat"):
            if(self.value!=5):
                self.value=5
        else: print("Seed aint real")
        self.display_value=self.value
    def harvest(self, row, column):
        if(self.value/len(self.seed)==len(self.seed)):
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
            #put all the crop stuff here
            if(self.value%5==0 and self.value!=0 and self.value/len(self.seed)<len(self.seed)):
             self.value+=5
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
    row_coord=int(input("row coordinate: "))
    collumn_coord=int(input("collumn coordinate: "))
    if(checkInteractable(row_coord,collumn_coord)): 
     seed_type=input("seed type: ")
     plots[row_coord-1][collumn_coord-1].plant(seed_type)

 elif(command=="next" or command==""):
    for i in range(4):
        for j in range(9):
            plots[i][j].grow()

 elif(command=="harvest" or command=="h"):
    row_coord=int(input("row coordinate: "))
    collumn_coord=int(input("collumn coordinate: "))
    if(checkInteractable(row_coord,collumn_coord)): 
     plots[row_coord-1][collumn_coord-1].harvest(row_coord,collumn_coord)

 elif(command=="debug" or command=="d"):
    row_coord=int(input("row coordinate: "))
    collumn_coord=int(input("collumn coordinate: "))
    if(checkInteractable(row_coord,collumn_coord)): 
     plots[row_coord-1][collumn_coord-1].debug()

 elif(command=="mone"):
    print(money)
 command=input("command: ")
 if(command=="stop"):
    game=False
