import os
clear = lambda: os.system('cls')

name=input("Enter your name: ")
age=input("Enter your age: ")

"""print("I think your name is "+ name + " and you are "+ age +" years old")"""

def exit_def(): 
   print("Goodbye")
  
def item_add(requested):
   item_list.append(requested)
def item_show():
   print(item_list)

item_list=[]
if int(age)<12 : print("Access denied.")
else: 

    exit=False
    clear()
    while(exit==False) :
     print(f"\nWelcome to the game,{name}\n")
     print("TITLE\n\n")
     print("1. START")
     print("2. COTINUE")
     print("3. ADD ITEM")
     print("4. SHOW ITEMS")
     print("5. OPTIONS")
     print("6. LOPETA")
     command= input("What command would you like to execute? ")
     if(command=="start" or command=="START" or command=="1"):
        print("You started the game!!")
     elif(command=="continue" or command == "CONTINUE" or command=="2"):
        print("You will continue from your save!") 
     elif(command=="add item" or command == "ADD ITEM" or command=="3"):
        item=input("What item would you like to add? ")
        item_add(item)
     elif(command=="show items" or command == "SHOW ITEMS" or command=="4"):
        item_show()
     elif(command=="options" or command == "OPTIONS" or command=="5"):
        print("This is the options menu")  
     elif(command=="lopeta" or command == "LOPETA" or command=="6"):
        exit_def()
        exit=True
