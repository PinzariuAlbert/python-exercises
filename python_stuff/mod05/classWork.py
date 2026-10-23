"""rounds=int(input("How many greetings: "))
finished_rounds = 0
while finished_rounds<rounds:
    print("Good morning")
    finished_rounds=finished_rounds+1

command = input("ENter command: ")
while command!="stop" :
    print("Executing command: " + command)
    command = input("Enter command: ")
print("Execution stopped.")        

import random
dice1=dice2 = rolls = 0
while(dice1 !=6 or dice2 !=6) :
    dice1=random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls = rolls +1
print(f"Rolled {rolls:d} times.")    

first = 1
while first <= 5:
    second = 1
    while second <=5:
        print(f"{first} times {second} is {first*second:d}")
        second = second +1
    first = first +1
print("Goodbye.") """
import random
rounds = 0
total_rolls = 0
while(rounds < 100000) :
 dice1=dice2 = rolls = 0
 while(dice1 !=6 or dice2 !=6) :
    dice1=random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls = rolls +1
 total_rolls = total_rolls +rolls
 rounds +=1   
print(f"Rolled {total_rolls/rounds:6.2f} times.")    

#break