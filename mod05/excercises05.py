import random
#1
"""i=1
while(i<=1000) :
      if (i%3==0) : 
         print(f"I found a number dividable by 3!! {i}")
      i+=1

#2
inches=0
while(inches>=0):
    inches = int(input("Enter the number of inches: \n"))
    if(inches>=0) :
     print(f"Your number in centimeters: {inches*2.54}")

#3
number = input("Please enter a number or enter nothing to quit: ")
if number!="" :
   max_number= int(number)
   min_number = int(number)
   while(number != "") : 
       number = input("Please enter a number or enter nothing to quit: ")
       if(number!="") : 
          if(max_number< int(number)): max_number=int(number)
          if(min_number>int(number)): min_number=int(number)
   print(f"The biggest number was: {max_number} \nAnd the smallest one was: {min_number}")

#4
want_play=True
while(want_play) : 
   random_num= random.randint(1,10)
   win= False
   while(win==False):
      guessed_num=int(input("Guess a number between 1 and 10! "))
      if(guessed_num==random_num): 
         print("You won!")
         win=True
      elif (guessed_num<random_num) : print("Too low")
      else : print("Too high")
   answer=input("Do you want to keep playing?(y/n) ")
   if (answer!="y" and answer!="Y") : want_play=False 

#5

fails=0
correct=False
while(fails<5 and correct==False):
  username=input("Enter your username\n")
  password=input("Enter your password\n")
  if(username!="python" or password!="rules") :
    fails+=1
    if(fails==5) : print("Access denied.")
    else :
          print("Your password or your username is wrong. Try again.\n")
  else: 
      print("Welcome!")
      correct=True"""

#6