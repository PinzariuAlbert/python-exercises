import os
import random
#global money=18
money=18
plots = []
field_size_row=2
field_size_col=3
bugged_col=[]
bugged_row=[]
clear = lambda: os.system('cls')


# This, down here, is the class that creates our plots. I use this function to make a matrix of game objects, this represents our "field"
# in it there are fundamental functions that let us interact with the game, like planting, harvesting and advancing the time("grow").
class Plot():
    def __init__(self,row,col,display_value=0, value=0, bugged=False):
        self.display_value=0  #uhhh, dont forget to use [ print(str(variable).zfill(2)) ]
        self.value=0
        self.bugged=bugged
        self.row=row
        self.col=col
    #item uses
        self.protection=0
        self.watered=0
        self.fertilized=0
        self.seed=""
    def plant(self, seed):
        if(not(self.row+1 in bugged_row or self.col+1 in bugged_col)):
            global money
            self.seed=seed
            if((seed=="watermelon" or seed=="9") and items.dict["motherboard"]>=2):
                if(money>=60):
                    money-=60
                    self.value=9
                    self.maxvalue=90
            elif((seed=="strawberries" or seed=="8") and items.dict["motherboard"]>=2):
                if(money>=40):
                    money-=40
                    self.value=8
                    self.maxvalue=48
            elif((seed=="pumpkin" or seed=="7") and items.dict["motherboard"]>=2):
                if(money>=35):
                    money-=35
                    self.value=7
                    self.maxvalue=56
            elif((seed=="corn" or seed=="6") and items.dict["motherboard"]>=1):
                if(money>=30):
                    money-=30
                    self.value=6
                    self.maxvalue=42
            elif((seed=="wheat" or seed=="5") and items.dict["motherboard"]>=1):
                if(money>=20):
 #           if(self.value!=5):
                    money-=20
                    self.value=5
                    self.maxvalue=40
                else: print("You need more money!")   
            elif((seed=="carrot" or seed=="4") and items.dict["motherboard"]>=1):
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
        if(self.seed!="" and not (self.row+1 in bugged_row or self.col+1 in bugged_col)):
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
           self.watered-=1
        else: print("Cant harvest")
    def bug(self):
        if(self.protection>0):
            self.protection-=1
        else:
            self.bugged=True
            rnd= random.randint(0,3)
            if(rnd==0): 
                self.display_value="~#"
            elif(rnd==1):
                self.display_value="*/"
            else:self.display_value="&^"
    def debug(self):
        if(not (self.row+1 in bugged_row or self.col+1 in bugged_col)):
            self.bugged=False
            self.protection=0
            self.display_value=self.value
    def grow(self):
       # print("tried to grow")
        #if(self.bugged==True and self.protection!=0):
         #   self.protection-=1
        if self.bugged==True:
            self.value=0
            self.display_value=0
            self.seed=""
            self.protection=0
            # maybe just check self.row-1>=0,, etc
            # instead of "plots[self.row-1][self.col]!=None"
            if( self.row-1>=0 and plots[self.row-1][self.col].value!=0): plots[self.row-1][self.col].bug()
            if(self.col-1>=0 and plots[self.row][self.col-1].value!=0): plots[self.row][self.col-1].bug()
            if(self.row+1<field_size_row and plots[self.row+1][self.col].value!=0): plots[self.row+1][self.col].bug()
            if(self.col+1<field_size_col and plots[self.row][self.col+1].value!=0): plots[self.row][self.col+1].bug()
            self.bugged=False
        elif self.value!=0:
         if(self.row+1 not in bugged_row and self.col+1 not in bugged_col):
          if(self.value<self.maxvalue):
            #put all the crop stuff here
            #                                              ADDDDDD MORE CROPS TO 7-9
            if(self.seed=="watermelon" or self.seed=="9"):
             if(self.watered>0):
                    self.value+=18
             else:
                     self.value+=9
            elif(self.seed=="strawberries" or self.seed=="8"):
             if(self.watered>0):
                    self.value+=16
             else:
                     self.value+=8
            elif(self.seed=="pumpkin" or self.seed=="7"):
             if(self.watered>0):
                    self.value+=14
             else:
                     self.value+=7
            elif(self.seed=="corn" or self.seed=="6"):
             if(self.watered>0):
                    self.value+=12
             else:
                     self.value+=6
            elif(self.seed=="wheat" or self.seed=="5"):
                if(self.watered>0):
                    self.value+=10
                else:
                     self.value+=5
            #elif(self.value%4==0 and self.value!=0 and (self.value+16)/len(self.seed)<len(self.seed)):     what was i even doing here...bs
            elif(self.seed=="carrot" or self.seed=="4"):
             if(self.watered>0):
                    self.value+=8
             else:
                     self.value+=4
            elif(self.seed=="cucumber" or self.seed=="3"):
             if(self.watered>0):
                    self.value+=6
             else:
                     self.value+=3
            elif(self.seed=="celery" or self.seed=="2"):
             if(self.watered>0):
                    self.value+=4
             else:
                     self.value+=2
            elif(self.seed=="potato" or self.seed=="1"):
             if(self.watered>0):
                    self.value+=2
             else:
                     self.value+=1
            if(self.value>self.maxvalue): self.value=self.maxvalue
            #this part of the else is only related to "bugs"
         rnd_buggin= random.randint(0,10)
         if(rnd_buggin==1):
                self.bug()
         else:
                self.display_value=self.value
#functions that manage the secomd kind of Bug that you can encounter
def bug2():
    row_bug_value=random.randint(1,field_size_row)
    col_bug_value=random.randint(1,field_size_col)
    if(random.randint(0,1)==0):
        if(row_bug_value not in bugged_row):
            bugged_row.append(row_bug_value)
    elif(col_bug_value not in bugged_col):
        bugged_col.append(col_bug_value)
def debug2(requested):
    if( requested in bugged_row):
        bugged_row.remove(requested)
    if(requested in bugged_col):
        bugged_col.remove(requested)

#Functions that trigger your tools(like plant and harvest) on multiple plots at the same time
def multi_plant(row1, col1,row2, col2, seed):
        for i in range(row1-1, row2):
            for k in range(col1-1, col2):
                plots[i][k].plant(seed)
def multi_harvest(row1, col1,row2, col2):
        for i in range(row1-1, row2):
            for k in range(col1-1, col2):
                plots[i][k].harvest()

#I use this function to check if the input from the player is usable
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

# class that handples our items! it acts as an inventory and the way to use the items themselves
class Items(Plot):
    def __init__(self):
        self.dict = {
            "water" : 0,
            "fertilizer" : 0,
            "protection" : 0,
            "worker" : 0,
            "motherboard": 0,
            "multiplant": 0,
            "multiuse":0,
            "multiharvest":0
        }
        self.total_workers=1
    def item_add(self,requested):
        global money
        global field_size_row
        global field_size_col
        global plots
        if requested in self.dict:
            if(requested=="motherboard"):
                if(self.dict[requested]==0):
                    if(money>=100):
                        input("You feel accomplished as you make your first step forward. This is your first upgrade in years, since your f@th3r gifted you your first board on your 18th birthday.".center(lengh) +"But you can't stop here, you did not achive the goal you set out for.".center(lengh)+ "Press enter to continue: \n".center(lengh-1))
                        clear()
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
                        input("One step closer once again. The generation of the field of 0-s in front of you might be the most beautiful graphics you have seen in your life.".center(lengh) +"You feel like something is missing.. or maybe that there is too much.".center(lengh)+ "Press enter to continue: \n".center(lengh-1))
                        clear()
                        clear()
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
            elif(requested=="water"):
                if(money>=20):
                    money-=20
                    self.dict[requested]+=1
                else: print("You do not have enough money.")
            elif(requested=="fertilizer"):
                if(money>=30):
                    money-=30
                    self.dict[requested]+=1
                else: print("You do not have enough money.")
            elif(requested=="protection"):
                if(money>=40):
                    money-=40
                    self.dict[requested]+=1
                else: print("You do not have enough money.")
            elif(requested=="worker"):
                if(money>=100*self.total_workers):
                    self.dict[requested]+=1
                    self.total_workers+=2
                else: print("You do not have enough money.")
            elif(requested=="multiuse"):
                if(money>=1000):
                    if(self.dict[requested]>0):
                        print("You already have this upgrade bought.")
                    else:
                        money-=1000
                        self.dict[requested]+=1
                else: print("You do not have enough money.")
            elif(requested=="multiplant"):
                if(money>=1000):
                    if(self.dict[requested]>0):
                        print("You already have this upgrade bought.")
                    else:
                        money-=1000
                        self.dict[requested]+=1
                else: print("You do not have enough money.")
            elif(requested=="multiharvest"):
                if(money>=2500):
                    if(self.dict[requested]>0):
                        print("You already have this upgrade bought.")
                    else:
                        money-=2500
                        self.dict[requested]+=1
                else: print("You do not have enough money.")
        else: print("Item does not exist.")
    def item_use(self,row, col,requested):
     if(not(row in bugged_row or col in bugged_col)):
        if (requested in self.dict and self.dict[requested]>0):
            if(requested=="water"):
                plots[row][col].watered=3
            elif(requested=="fertilizer"):
                plots[row][col].fertilized=3
                                           #CHANGE PROTECTION, i need prot to deflect the bugs entirely. not just delay the destruction of the plant.
            if(requested=="protection"):
                plots[row][col].protection=3
            self.dict[requested]-=1
        else: print("Error: Item doesn't exist")
    def multi_use(self, row1, col1, row2, col2, requested):
        for i in range(row1-1, row2):
            for k in range(col1-1, col2):
                self.item_use(i,k,requested)
    def item_show(self):
        print(self.dict)
items= Items()
won= False
if True:
    lengh=os.get_terminal_size().columns
    final_exit=True
    clear()
    while(final_exit) :
        #The start of the game, this is just the main menu. There was supposed to be a "Continue" button, but making the save system would take too long
     print("Bit Defender".center(lengh) + "A Farming Simulator\n".center(lengh))  
     print( "1. START".center(lengh) #+ "2. CONTINUE".center(lengh)
      + "2. OPTIONS".center(lengh) +"3. LOPETA".center(lengh))

     command= input("What command would you like to execute?".center(lengh) +"\n".center(lengh))
     if(command=="start" or command=="START" or command=="1"):
        clear()
        game=True
        input("You are a poor byte farmer.".center(lengh) + "You have seen newer and better generations of hardware appearing every year while you are stuck on your old, prone to crashes and bugs motherboard from 2007.".center(lengh) + '"Enough is enough.." you said to yourself as you grabbed your hoe and de-bugging kit, and headed out your folder into the files.'.center(lengh) + "Press enter to continue: \n".center(lengh-1))
        clear()
        #print("Bit Defender".center(lengh))
        print("You started the game!!")
        # making the field
        for i in range(field_size_row):
              row=[]
              for j in range(field_size_col):
                row.append(Plot(i,j))
              plots.append(row)
        while(game==True):
            
          #This is the main game loop. The first lines of code here are only made for the looks of the game. I am printing the fields, the player data and the commands.

            print(f"Current bytes: {money}/10000".center(lengh))
            if(money>=10000 and not won):
              while(not won):
                clear()
                print("This is it. You have all the money you would need to finally get to the top.".center(lengh) +"But... something is not right.".center(lengh) + "You feel like you miss the times when the bugs were not constantly attacking you, you miss the attention the old Makers paid to every detail.".center(lengh) + "You miss they way you could count every polygon on the surface of your crops, you miss the old times...".center(lengh))
                choice=input("The newer --- do offer so many advantages, but now you are not so sure about their worth.".center(lengh) + "What will you choose? Will you go back to the simpler times or will you adapt to your new life?".center(lengh) + "(continue/go back)\n".center(lengh))
                if(choice=="continue"):
                    plots=[]
                    field_size_row=9
                    field_size_col=36
                    for i in range(field_size_row):
                            row=[]
                            for j in range(field_size_col):
                              row.append(Plot(i,j))
                            plots.append(row)
                    won=True
                    clear()
                elif(choice=="go back"):
                    plots=[]
                    field_size_row=4
                    field_size_col=5
                    for i in range(field_size_row):
                            row=[]
                            for j in range(field_size_col):
                              row.append(Plot(i,j))
                            plots.append(row)
                    won=True
                    clear()
            print("------------------------------------------------------------------------------------------------".center(lengh))
            show_row=0
            show_col=0
            print("".center(int(lengh/2-len(plots)*3)+2), end="")
            for j in range(field_size_col):
                show_col+=1
                if(show_col>9):
                    if(show_col in bugged_col):
                        random_col = random.randint(10,field_size_col)
                        while(random_col == show_col):
                            random_col= random.randint(10,field_size_col)
                        print(f" {random_col}",end="")
                    else : print(f" {show_col}",end="")
                else:
                    if(show_col in bugged_col):
                        random_col = random.randint(1,9)
                        while(random_col == show_col):
                            random_col= random.randint(1,9)
                        print(f"  {random_col}",end="")
                    #what was i on.. yes, there is a difference, it prints more spaces, jeez 
                    else:
                        print(f"  {show_col}",end="")
            print()
            for i in plots:
                print(" ".center(int(lengh/2-len(plots)*3)), end="")
                show_row+=1
                if(show_row in bugged_row):
                        random_row = random.randint(1,6)
                        while(random_row == show_row):
                            random_row= random.randint(1,6)
                        print(f"{random_row}| ", end="")
                else : print(f"{show_row}| ", end="")
                
                for j in i:
                    print(str(j.display_value).zfill(2) , end=" ")
                print("|", end="")
                print()
            print("------------------------------------------------------------------------------------------------".center(lengh))
            print("List of commands:".center(lengh),end="" + "1.Advance(next,' ',1)".center(lengh) +"2.Plant(plant,p,2) 3.MultiPlant(multiplant,mp,3) 4.Harvest(harvest,h,3) 5.MultiHarvest(multiharvest,mh,5) 6.Use Item(use/u/6) 7.MultiUse(multiuse,mu,7)".center(lengh) + "8.Debug(debug,d,8) 9.Buy(buy,b,9) 10.Exit(exit/e/0)".center(lengh))
            print()
            
            # After all the printing is done, the player can pick their command. The rest is pretty intuitive. 

            command=input("command: \n".center(lengh))

            if(command=="plant" or command=="p" or command=="2"):
                row_coord=input("row coordinate: \n".center(lengh))
                collumn_coord=input("collumn coordinate: \n".center(lengh))
                if(checkInteractable(row_coord,collumn_coord)):
                    if(items.dict["motherboard"]>=2): 
                        seed_type=input("seed type: 1.potato($3) 2.celery($8) 3.cucumber($11) 4.carrot(15$) 5.wheat($20) 6.corn($30) 7.pumpkin($35) 8.strawberries($40) 9.watermelon($60)\n".center(lengh))
                    elif(items.dict["motherboard"]==1):
                        seed_type=input("seed type: 1.potato($3) 2.celery($8) 3.cucumber($11) 4.carrot(15$) 5.wheat($20) 6.corn($30)\n".center(lengh))
                    else: 
                        seed_type=input("seed type: 1.potato($3) 2.celery($8) 3.cucumber($11)\n".center(lengh))
                    clear()
                    plots[int(row_coord)-1][int(collumn_coord)-1].plant(seed_type)
            elif(command=="multiplant" or command=="mp" or command=="3"):
                if(items.dict["multiplant"]>0):
                    row_coord1=input("first row coordinate: \n".center(lengh))
                    collumn_coord1=input("first collumn coordinate: \n".center(lengh))
                    row_coord2=input("second row coordinate: \n".center(lengh))
                    collumn_coord2=input("second collumn coordinate: \n".center(lengh))
                    if(checkInteractable(row_coord1,collumn_coord1) and checkInteractable(row_coord2, collumn_coord2)):
                        if(items.dict["motherboard"]>=2): 
                            seed_type=input("seed type: 1.potato($3) 2.celery($8) 3.cucumber($11) 4.carrot(15$) 5.wheat($20) 6.corn($30) 7.pumpkin($35) 8.strawberries($40) 9.watermelon($60)\n".center(lengh))
                        elif(items.dict["motherboard"]==1):
                            seed_type=input("seed type: 1.potato($3) 2.celery($8) 3.cucumber($11) 4.carrot(15$) 5.wheat($20) 6.corn($30)\n".center(lengh))
                        else: 
                            seed_type=input("seed type: 1.potato($3) 2.celery($8) 3.cucumber($11)\n".center(lengh))
                        clear()
                        multi_plant(int(row_coord1),int(collumn_coord1),int(row_coord2), int(collumn_coord2),seed_type)
                else: 
                    clear()
                    print("You have not bought this upgrade yet.")
            elif(command=="next" or command=="" or command=="1"):
                clear()
              #  for i in range(field_size_row):
             #       for j in range(field_size_col):
            #            plots[i][j].grow()
                bugged_plots=[]
                for i in range(field_size_row):
                    for j in range(field_size_col):
                        if plots[i][j].bugged:
                            bugged_plots.append(plots[i][j])
                        else:
                            plots[i][j].grow()
                for bplots in bugged_plots:
                    bplots.grow()
                if(items.dict["motherboard"]>=2):
                    if(random.randint(0, 40)==1):
                        bug2()

            elif(command=="harvest" or command=="h" or command=="4"):
                row_coord=input("row coordinate: \n".center(lengh-5))
                collumn_coord=input("collumn coordinate: \n".center(lengh-5))
                if(checkInteractable(row_coord,collumn_coord)): 
                    clear()
                    plots[int(row_coord)-1][int(collumn_coord)-1].harvest()
            elif(command=="multiharvest" or command=="mh" or command=="5"):
                if(items.dict["multiharvest"]>0):
                    row_coord1=input("first row coordinate: \n".center(lengh-5))
                    collumn_coord1=input("fisrt collumn coordinate: \n".center(lengh-5))
                    row_coord2=input("second row coordinate: \n".center(lengh-5))
                    collumn_coord2=input("second collumn coordinate: \n".center(lengh-5))
                    if(checkInteractable(row_coord1,collumn_coord1) and checkInteractable(row_coord2,collumn_coord2)): 
                        clear()
                        multi_harvest(int(row_coord1),int(collumn_coord1),int(row_coord2), int(collumn_coord2))
                else: 
                    clear()
                    print("You have not bought this upgrade yet.")
            
            elif(command=="buy" or command=="b" or command=="9"):
                print("What would you want to buy? \n".center(lengh))

                                          # The Worker you see here has not been implemented!! I could not get them to work as easily as I had hoped so for the time being they are a nonfunctional feature.

                print("0. Exit 1. Water(makes crops grow faster)[20] 2. Fertilizer(makes crops give a bigger yeld)[30] 3. Protection(makes crops un-buggable)[40] 4. Worker[100]".center(lengh))
                print("5. MultiPlant[1000] 6. MultiUse[1000]  7. MultiHarvest[2500] 8.New Motherboard(sell all your crops before hand)[100/3000]".center(lengh))
                buy_request=input("item: \n".center(int(lengh)))
                quantity=input("How many?: \n".center(lengh-4))
                clear()
                if(buy_request!=0 and buy_request!="exit" and quantity!=0 and quantity!="" and quantity.isdigit()):
                    for i in range(int(quantity)):
                        items.item_add(buy_request)
            elif(command=="use" or command=="u" or command=="6"):
                print("What item do you want to use?".center(lengh))
                print("0. Exit 1. Water 2. Fertilizer 3. Protection 4.Worker".center(lengh))
                use_request=input("item: \n".center(lengh))
                row_coord=input("row coordinate: \n".center(lengh-5))
                collumn_coord=input("collumn coordinate: \n".center(lengh-5))
                if(checkInteractable(row_coord,collumn_coord)): 
                    if(use_request!=0 or use_request!="exit"):
                        clear()
                        items.item_use(int(row_coord)-1,int(collumn_coord)-1,use_request)
            elif(command=="multiuse" or command=="mu" or command=="7"):
                if(items.dict["multiuse"]>0):
                    print("What item do you want to use?".center(lengh))
                    print("0. Exit 1. Water 2. Fertilizer 3. Protection 4.Worker".center(lengh))
                    use_request=input("item: \n".center(lengh))
                    row_coord1=input("first row coordinate: \n".center(lengh-5))
                    collumn_coord1=input("sirst collumn coordinate: \n".center(lengh-5))
                    row_coord2=input("second row coordinate: \n".center(lengh-5))
                    collumn_coord2=input("second collumn coordinate: \n".center(lengh-5))
                    if(checkInteractable(row_coord1,collumn_coord1) and checkInteractable(row_coord2, collumn_coord2)): 
                        if(use_request!=0 or use_request!="exit"):
                            clear()
                            items.multi_use(int(row_coord1),int(collumn_coord1),int(row_coord2), int(collumn_coord2), use_request)
                else: print("You have not bought this upgrade yet.")
                    
            elif(command=="debug" or command=="d" or command=="8"):
                if(items.dict["motherboard"]<2):
                    row_coord=input("row coordinate: \n".center(lengh-5))
                    collumn_coord=input("collumn coordinate: \n".center(lengh-5))
                    if(checkInteractable(row_coord,collumn_coord)): 
                        clear()
                        plots[int(row_coord)-1][int(collumn_coord)-1].debug()
                else:
                    print("What do you want to debug? (plot(1)/line(2))\n".center(lengh))
                    debug_command=input("".center(lengh))
                    if(debug_command=="1" or debug_command=="plot"):
                        row_coord=input("row coordinate: \n".center(lengh-5))
                        collumn_coord=input("collumn coordinate: \n".center(lengh-5))
                        if(checkInteractable(row_coord,collumn_coord)): 
                            clear()
                            plots[int(row_coord)-1][int(collumn_coord)-1].debug()
                    elif(debug_command=="2" or debug_command=="line"):
                        line_coord=input("line coordinate: \n".center(lengh))
                        clear()
                        debug2(int(line_coord))
                    else: print("Error: Command does not exist.")
            elif(command=="exit" or command=="e" or command=="0"):
              clear()
              game=False
            elif(command=="GiveMoney"):
                money+=6000
                clear()
            else: 
                clear()
                print("Error: Command does not exist.")

     #elif(command=="continue" or command == "CONTINUE" or command=="2"):
      #  print("You will continue from your save!")
     elif(command=="options" or command == "OPTIONS" or command=="2"): 
        print("This is the options menu")
     elif(command=="exit" or command == "EXIT" or command=="3"):
        exit_def()
        final_exit=False