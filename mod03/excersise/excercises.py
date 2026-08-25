import random
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
print("The average is: "+ str((int(n1)+int(n2)+int(n3))/3))

#5
talents=input("Enter talents:\n")
pounds=input("Enter punds:\n")
lots=input("Enter lots:\n")
print("The weight in modern units:\n" + ((talents*20)+pounds)*0,453592 + " kilograms and " )

#6
combiation1= [random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)]
combiation2= [random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]
print("The first combination is: " + str(combiation1))
print("The second combination is: " + str(combiation2))
