#if(condition):
#	conditionally executed block of code
#elif:
"""
dog1 = "A"
dog2 = "a"
if dog1 <= dog2: print("Dog 1 is bigger than gog2!")
else: print("Oh, dog 2 is bigger")
print(ord(dog1))
print(ord(dog2))
print(chr(65))"""

"""age=int(input("Enter your age: "))
if 15<= age < 18:
    weight = float(input("Enter your weight(kg): "))
if (age>=18 or age>=15 and weight >=55):
    print("THe medicine can be used.")
else: print("The medicine cannot be used.")"""

"""grade = int(input("Enter your grade: "))
if grade >= 90: print("A1")
elif grade >= 80: print("A2")
elif grade>=70: print("B1")
elif grade>=60: print("B2")
elif grade>=50: print("C1")
elif grade>=40: print("C2")
elif grade>=30: print("D1")
elif grade>=20: print("D2")
elif grade>=10: print("E1")
else: print("E2")"""

citizenship = input("Do you have citizenship(y/n)? ")
if citizenship=="y" or citizenship=="Y":
    age=int(input("What is your age? "))
    if age>=18: print("You can vote!")
    else: print("You cannot vote yet, you need to wait untill you are 18..")    
else: print("You cannot vote..")    