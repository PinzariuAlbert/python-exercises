"""import random
#1
name=input("WHat is your name? ")
print("Hello, "+name+"!")

#2
radius=input("What's the radius of the circle? ")
print("The area of the circle will be: "+ str(int(radius)**2*3.14))

#3
length=input("What is the LENGTH of the rectangle? ")
width= input("And what is the WIDTH of the rectangle? ")
print("The perimeter of the rectangle is: "+ str(int(length)*2+int(width)*2))

#4
n1=input("Enter the first number: ")
n2=input("Enter the second number: ")
n3=input("Enter the third number: ")
print("The sum is: "+ str(int(n1)+int(n2)+int(n3)))
print("The product is: "+ str(int(n1)*int(n2)*int(n3)))
print("The average is: "+ str((int(n1)+int(n2)+int(n3))/3))"""

#5
talents=float(input("Enter talents:\n"))
pounds=float(input("Enter punds:\n"))
lots=float(input("Enter lots:\n"))
total_pounds = talents * 20 + pounds
total_lots = total_pounds * 32 + lots
total_grams = float(total_lots) * 13.3

print("The weight in modern units: "+ str(total_grams // 1000)+" and "+str(total_grams % 1000)+"grams")
#6
combiation1= [random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)]
combiation2= [random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]
print("The first combination is: " + str(combiation1))
print("The second combination is: " + str(combiation2))
