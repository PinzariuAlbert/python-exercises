import os
clear = lambda: os.system('cls')

name=input("Enter your name: ")
age=input("Enter your age: ")

"""print("I think your name is "+ name + " and you are "+ age +" years old")"""
if int(age)<12 : print("Access denied.")
else: 

    exit=False
    clear()
    while(exit==False) :
     print(f"\nWelcome to the game,{name}\n")
     print("TITLE\n\n")
     print("1. START")
     print("2. COTINUE")
     print("3. OPTIONS")
     print("4. LOPETA")
     command= input("What command would you like to execute? ")
     if(command=="start" or command=="START" or command=="1"):
        print("You started the game!!")
     elif(command=="continue" or command == "CONTINUE" or command=="2"):
        print("You will continue from your save!") 
     elif(command=="options" or command == "OPTIONS" or command=="3"):
        print("This is the options menu")  
     elif(command=="lopeta" or command == "LOPETA" or command=="4"):
        print("Goodbye")
        exit=True  
