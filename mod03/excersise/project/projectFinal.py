import os
import random
#global money=18
money=18
plots = []
field_size_row=2
field_size_col=3
clear = lambda: os.system('cls')
#to do list: items(water, fertilizer,protection), workers for sutomatization, buying rows/colls, save/continue, make pretty
#            make the error messages more serious(28.09)
class Plot():
    def __init__(self,row,col,display_value=0, value=0, bugged=False):
        self.display_value=0  #uhhh, dont forget to use [ print(str(variable).zfill(2)) ]
        self.value=0
        self.bugged=bugged
        self.row=row
        self.col=col
    #item uses
        self.protection=1
        self.watered=0
        self.fertilized=0
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
    def harvest(self):
        if(self.seed!=""):
         if(self.value==self.maxvalue):
           global money
           if plots[self.row][self.col].fertilized>0:
            plots[self.row][self.col].fertilized-=1
            money+=int(self.value*1.5)
           else:
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
        self.protection=1
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
            # maybe just check self.row-1>=0,, etc
            # instead of "plots[self.row-1][self.col]!=None"
            if( self.row-1>=0 and plots[self.row-1][self.col].value!=0):
                 plots[self.row-1][self.col].protection=1 ; plots[self.row-1][self.col].bug()
            if(self.col-1>=0 and plots[self.row][self.col-1].value!=0):
                 plots[self.row][self.col-1].protection=1 ; plots[self.row][self.col-1].bug()
            if(self.row+1<field_size_row and plots[self.row+1][self.col].value!=0):
                 plots[self.row+1][self.col].protection=1 ; plots[self.row+1][self.col].bug()
            if(self.col+1<field_size_col and plots[self.row][self.col+1].value!=0):
                 plots[self.row][self.col+1].protection=1 ; plots[self.row][self.col+1].bug()
            self.bugged=False
        elif self.value!=0:
         if(self.value<self.maxvalue):
            #put all the crop stuff here
            if(self.seed=="wheat" or self.seed=="5"):
                if(self.watered>0):
                    self.value+=10
                    self.watered-=1
                else:
                     self.value+=5
            #elif(self.value%4==0 and self.value!=0 and (self.value+16)/len(self.seed)<len(self.seed)):     what was i even doing here...bs
            elif(self.seed=="carrot" or self.seed=="4"):
             if(self.watered>0):
                    self.value+=8
                    self.watered-=1
             else:
                     self.value+=4
            elif(self.seed=="cucumber" or self.seed=="3"):
             if(self.watered>0):
                    self.value+=6
                    self.watered-=1
             else:
                     self.value+=3
            elif(self.seed=="celery" or self.seed=="2"):
             if(self.watered>0):
                    self.value+=4
                    self.watered-=1
             else:
                     self.value+=2
            elif(self.seed=="potato" or self.seed=="1"):
             if(self.watered>0):
                    self.value+=2
                    self.watered-=1
             else:
                     self.value+=1
            if(self.value>self.maxvalue): self.value=self.maxvalue
            #this part of the else is only related to "bugs"
            rnd_buggin= random.randint(0,2)
            if(rnd_buggin==1):
                self.bug()
            else:
                self.display_value=self.value

def checkInteractable(row, col):
    if(row=="" or col==""):
        clear()
        print("Error: Something wasn't inputed correctly!")
        return False
    elif(not str(row).isdigit() or not str(col).isdigit()):
        clear()
        print("Error: Something wasn't inputed correctly!")
        return False
    elif(int(row)>field_size_row or int(col)>field_size_col or int(row)<1 or int(col)<1):
        clear()
        print("Error: Something wasn't inputed correctly!")
        return False
    else:
     return True

def exit_def(): 
   print("Goodbye")

class Items(Plot):
    def __init__(self):
        self.dict = {
            "water" : 0,
            "fertilizer" : 0,
            "protection" : 0,
            "worker" : 0,
            "motherboard": 0
        }
    def item_add(self,requested):
        global money
        global field_size_row
        global field_size_col
        global plots
        if requested in self.dict:
            #if(request=="water"):
            #    if(money>="")
            if(requested=="motherboard"):
                if(self.dict[requested]==0):
                    if(money>=100):
                        money-=100
                        plots=[]
                        field_size_row=5
                        field_size_col=7
                        for i in range(field_size_row):
                            row=[]
                            for j in range(field_size_col):
                              row.append(Plot(i,j))
                            plots.append(row)
                        self.dict[requested]+=1
                elif(self.dict[requested]==1):
                    if(money>=3000):
                        money-=3000
                        plots=[]
                        field_size_row=6
                        field_size_col=12
                        for i in range(field_size_row):
                            row=[]
                            for j in range(field_size_col):
                              row.append(Plot(i,j))
                            plots.append(row)
                        self.dict[requested]+=1
                else: print("You're at the maximum field level")
            else: self.dict[requested]+=1
        else: print("nuh, Item doesn't exist")
    def item_use(self,row, col,requested):
        if (requested in self.dict and self.dict[requested]>0):
            if(requested=="water"):
                plots[row][col].watered=3
            elif(requested=="fertilizer"):
                plots[row][col].fertilized=3
                                               #CHANGE PROTECTION, i need prot to deflect the bugs entirely. not just delay the destruction of the plant.
            if(requested=="protection"):
                plots[row][col].protection=3
            self.dict[requested]-=1
        else: print("Item doesn't exist")
    def item_show(self):
        print(self.dict)

item_list=[]
items= Items()
if True:
    lengh=os.get_terminal_size().columns
    final_exit=True
    clear()
    while(final_exit) :
     print("Bit Defender".center(lengh) + "A Farming Simulator\n".center(lengh))  
     print( "1. START".center(lengh) + "2. CONTINUE".center(lengh) + "3. OPTIONS".center(lengh) +"4. LOPETA".center(lengh))

     command= input("What command would you like to execute?".center(lengh) +"\n".center(lengh))
     if(command=="start" or command=="START" or command=="1"):
        clear()
        game=True
        print("You started the game!!")
        for i in range(field_size_row):
              row=[]
              for j in range(field_size_col):
                row.append(Plot(i,j))
              plots.append(row)
        while(game==True):
            for i in plots:
                #print(" ".center(int(lengh/2-len(plots)*2)), end="")
                for j in i:
                    print(str(j.display_value).zfill(2) , end=" ")
                print()
            print(f"Current bytes: {money}")
            command=input("command: ")

            if(command=="plant" or command=="p"):
                row_coord=input("row coordinate: ")
                collumn_coord=input("collumn coordinate: ")
                if(checkInteractable(row_coord,collumn_coord)): 
                    seed_type=input("seed type: 1.potato 2.celery 3.cucumber 4.carrot 5.wheat ")
                    clear()
                    plots[int(row_coord)-1][int(collumn_coord)-1].plant(seed_type)

            elif(command=="next" or command==""):
                clear()
                for i in range(field_size_row):
                    for j in range(field_size_col):
                        plots[i][j].grow()

            elif(command=="harvest" or command=="h"):
                row_coord=input("row coordinate: ")
                collumn_coord=input("collumn coordinate: ")
                if(checkInteractable(row_coord,collumn_coord)): 
                    clear()
                    plots[int(row_coord)-1][int(collumn_coord)-1].harvest()
            
            elif(command=="buy" or command=="b"):
                print("What would you want to buy?")
                request=input("0. Exit 1. Water(makes crops grow faster) \n 2. Fertilizer(makes crops give a bigger yeld) \n 3. Protection(makes crops un-buggable) \n 4. More rows \n 5. More columns \n 6. Worker\n 7.New Motherboard(sell all your crops before hand)\n")
                clear()
                items.item_add(request)

            elif(command=="debug" or command=="d"):
                row_coord=input("row coordinate: ")
                collumn_coord=input("collumn coordinate: ")
                if(checkInteractable(int(row_coord),int(collumn_coord))): 
                    clear()
                    plots[int(row_coord)-1][int(collumn_coord)-1].debug()

            elif(command=="money"):
                clear()
                print(money)
            elif(command=="stop" or command=="exit"):
              clear()
              game=False
            elif(command=="GiveMoney"):
                money+=6000
                clear()
            else: 
                clear()
                print("Error: Command does not exist.")

     elif(command=="continue" or command == "CONTINUE" or command=="2"):
        print("You will continue from your save!")
     elif(command=="options" or command == "OPTIONS" or command=="3"): 
        print("This is the options menu")
     elif(command=="exit" or command == "EXIT" or command=="4"):
        exit_def()
        final_exit=False