money=0
class Plot():
    def __init__(self,display_value=0, value=0, bugged=False):
        self.display_value=0  #uhhh, dont forget to use [ print(str(variable).zfill(2)) ]
        self.value=0
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
           
    def grow(self):
       # print("tried to grow")
        if(self.value%5==0 and self.value!=0 and self.value/len(self.seed)<len(self.seed)):
            self.value+=5
        self.display_value=self.value


plots = []
game=True
for i in range(4):
    row=[]
    for j in range(9):
        row.append(Plot())
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
 if(command=="plant" or command=="p"):
    row_coord=int(input("row coordinate: "))
    collumn_coord=int(input("collumn coordinate: "))
    if(row_coord>4 or collumn_coord>9):
        print("Woah! you don't have *that* much land!")
    else: 
     seed_type=input("seed type: ")
     plots[row_coord-1][collumn_coord-1].plant(seed_type)
 if(command=="next" or command==""):
    for i in range(4):
        for j in range(9):
            plots[i][j].grow()
 if(command=="harvest" or command=="h"):
    row_coord=int(input("row coordinate: "))
    collumn_coord=int(input("collumn coordinate: "))
    plots[row_coord-1][collumn_coord-1].harvest(row_coord,collumn_coord)
 if(command=="mone"):
    print(money)
 command=input("command: ")
 if(command=="stop"):
    game=False
