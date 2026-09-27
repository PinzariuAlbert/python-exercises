import random
#1
sum_die=0
n=int(input("Enter how many dice you want to roll: "))
for number in range(n): 
    sum_die = sum_die+random.randint(1,6)
print(f"The sum of the die was: {sum_die}")
#2
numbers = []
while(True):
    number = input("Enter a number : ")
    if (number == ""):
        break
    numbers.append(float(number))
numbers.sort(reverse=True)
print("The five greatest numbers are:")
for num in numbers[:5]:
    print(num)
#3
number = int(input("Enter an integer: "))
is_prime = True
if(number <= 1):
    is_prime = False
else:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
#4
cities = []
for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)
print("The cities you entered are:")
for city in cities:
    print(city)