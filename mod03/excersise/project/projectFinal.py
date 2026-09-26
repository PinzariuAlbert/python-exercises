import os
import random
money=18
plots = []
clear = lambda: os.system('cls')
#to do list: items(water, fertilizer,protection), workers for sutomatization, buying rows/colls, save/continue, make pretty
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

def checkInteractable(row, col):
    if(not str(row).isdigit() or not str(col).isdigit()):
        print("Error: Something wasn't inputed correctly!")
        return False
    elif(int(row)>4 or int(col)>9 or int(row)<1 or int(col)<1):
        print("Error: Something wasn't inputed correctly!")
        return False
    else:
     return True
     
def exit_def(): 
   print("Goodbye")
class Items():
    def __init__(self):
        self.dict = {
            "water" : 0,
            "fertilizer" : 0,
            "protection" : 0,
            "worker" : 0
        }
    def item_add(requested):
        if requested in self.dict:
           self.dict[requested]+=1
        else: print("nuh, bad item")
    def item_show():
        print(self.dict)

item_list=[]
#name=input("Enter your name: ")
#age=input("Enter your age: ")
#if int(age)<12 : print("Access denied.")
#else:
if True: 
    final_exit=True
    clear()
    while(final_exit) :
    # print(f"\nWelcome to the game,{name}\n")
     print("   Bit Defender\nA Farming Simulator\n\n")
     print("1. START")
     print("2. COTINUE")
     #print("3. ADD ITEM")
     #print("4. SHOW ITEMS")
     print("5. OPTIONS")
     print("6. LOPETA")

     command= input("What command would you like to execute? ")
     if(command=="start" or command=="START" or command=="1"):
        clear()
        game=True
        print("You started the game!!")
        for i in range(4):
              row=[]
              for j in range(9):
                row.append(Plot(i,j))
              plots.append(row)
        while(game==True):
            #if(command=="show" or command=="s"):
            #i might as well make it so that the plots always show themselves
            for i in plots:
                for j in i:
                    print(str(j.display_value).zfill(2), end=" ")
                print()
            print(f"Current bytes: {money}")
            command=input("command: ")

            if(command=="plant" or command=="p"):
                row_coord=input("row coordinate: ")
                collumn_coord=input("collumn coordinate: ")
                if(checkInteractable(row_coord,collumn_coord)): 
                    seed_type=input("seed type: 1.potato 2.celery 3.cucumber 4.carrot 5.wheat")
                    clear()
                    plots[int(row_coord)-1][int(collumn_coord)-1].plant(seed_type)

            elif(command=="next" or command==""):
                clear()
                for i in range(4):
                    for j in range(9):
                        plots[i][j].grow()

            elif(command=="harvest" or command=="h"):
                row_coord=input("row coordinate: ")
                collumn_coord=input("collumn coordinate: ")
                if(checkInteractable(row_coord,collumn_coord)): 
                    clear()
                    plots[int(row_coord)-1][int(collumn_coord)-1].harvest(int(row_coord),int(collumn_coord))
            
            elif(command=="buy" or command=="b"):
                print("What would you want to buy?")
                request=int(input("0. Exit 1. Water(makes crops grow faster) \n 2. Fertilizer(makes crops give a bigger yeld) \n 3. Protection(makes crops un-buggable) \n 4. More rows \n 5. More columns \n 6. Worker\n"))
                if(request==1):
                    item_add("water")

            elif(command=="debug" or command=="d"):
                row_coord=input("row coordinate: ")
                collumn_coord=input("collumn coordinate: ")
                if(checkInteractable(int(row_coord),int(collumn_coord))): 
                    clear()
                    plots[int(row_coord)-1][int(collumn_coord)-1].debug()

            elif(command=="money"):
                clear()
                print(money)
            if(command=="stop" or command=="exit"):
              clear()
              game=False

     elif(command=="continue" or command == "CONTINUE" or command=="2"):
        print("You will continue from your save!") 
     #elif(command=="add item" or command == "ADD ITEM" or command=="3"):
     #   item=input("What item would you like to add? ")
     #   item_add(item)
     #elif(command=="show items" or command == "SHOW ITEMS" or command=="4"):
     #   item_show()
     elif(command=="options" or command == "OPTIONS" or command=="5"):
        print("This is the options menu")  
     elif(command=="lopeta" or command == "LOPETA" or command=="6"):
        exit_def()
        final_exit=False