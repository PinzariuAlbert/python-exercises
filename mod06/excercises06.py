import random
#1
sum_die=0
n=int(input("Enter how many dice you want to roll: "))
for number in range(n): 
    sum_die = sum_die+random.randint(1,6)
print(f"The sum of the die was: {sum_die}")