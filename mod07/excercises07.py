import random
#1. 

def roll_dice() :
    return str(random.randint(1,6))
print("The die rolled a "+ roll_dice())

#2
def roll_dice(sides) :
    while(True) : 
        current = random.randint(1, int(sides))
        print("I rolled a: " + str(current))
        if(current==int(sides)) : return
        
sides = input("How many sides do you want the die to have? ")
roll_dice(sides)

#3
def converter(gallons):
    print(f"{gallons} gallons is equal to {gallons*3,78541} liters")
quantity=int(input("Quantity of gallons? "))
while(quantity>=0):
    converter(quantity)
    quantity=int(input("Quantity of gallons? "))

#4
def sum_list(list):
    final=0
    for n in list:
        final+=n
    print(f"The sum of the numbers is {final}")  
numbers=[1,24,5]
sum_list(numbers)

#5
def uneven_remover(full_list):
    okay=False
    print(f"Initial list: {full_list}")
    while(okay==False) :
     okay=True
     for i in full_list :
        #print(i)
        if(i%2!=0):
           full_list.remove(i)
           okay=False
    print(f"After changes: {full_list}")

full_list=[12,3,24,4,5,9,133,428]
uneven_remover(full_list)

#6
def pizza_2(dia , price) : 
    return float(price)/float(dia)
diameter = input("What's the diamater of the first pizza? ")
price = input("What's the price of the first pizza? ")
diameter2=input("What's the diamater of the second pizza? ")
price2 = input("What's the price of the second pizza? ")
if(pizza_2(diameter,price)<pizza_2(diameter2, price2)): print(f"The first pizza has a better value for money with a price of {pizza_2(diameter,price)} per square meter")
else: print(f"The second pizza has a better value for money with a price of {pizza_2(diameter2,price2)} per square meter")