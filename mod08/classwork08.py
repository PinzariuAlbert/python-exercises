import random
"""
def cast():
 first, second = random.randint(1,6), random.randint(1,6)
 return first, second
die1, die2 = cast()
print(f"The dice show {die1} and {die2}") """

numbers = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"}

numbers["Olga"] = "050-1011012"
numbers["Mary"] = "0401-2132139"

print(numbers)

name = input("Enter name: ")
if name in numbers:
    print(f"{name}'s phone number is {numbers[name]}.")