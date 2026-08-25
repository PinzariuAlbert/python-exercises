import os
clear = lambda: os.system('cls')
#added the os library so i could finally use clear(), got the code from stack overflow -w-

"""print("Hello World!")
print('Hello World!')
print("It's a beautiful day!")
print('"Moi", said Asli')


print("Hello")
print("World")
print("Hello\nWorld")


name = "Abhinoor"
print(name)
add1=id(name)
print(add1)
name="Albert"
print(name)
add2=id(name)
print(add2)
#bahbahbah
#clear()
user=input("Enter Your Name: ")
print(user)
print("Hello, "+ user + "!")"""

"""n1=int(input("first number "))
n2=int(input("second number "))
result= n1+n2
print(type(n1))
print(type(n2))
print(result)

print(type(result))
division = n1/n2
print(division)
print(type(division))

print(id(n1)==id(n2))"""

a1=10
a2=-20
a3=1.2
a4=-2+3j
a5=1_22_333_444

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(type(a1))
print(type(a2))
print(type(a3))
print(type(a4))
print(type(a5))

s1="Hello"
s2='Hello'
s3="123"
s4=""
s5="Albert said: 'Hewwo'"

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

print(type(s3))
s3_converted= float(s3)
print(type(s3_converted))

clear()

a6=7
a7=2
a8mod= a6%a7
print(a8mod)
a9floor=a6//a7
print(a9floor)
a10power=a6**a7
print(a10power)

farenheit_str= input("ENter a temperature: ")
farenheit = float(farenheit_str)
celsius = (farenheit-32)*5/9
print("The temperature in Celcius: " + str(celsius))
print(f"The temperature in Celsius:  {celsius:10.8f}")

import math
print(f"{'Pi':5s}:{math.pi:10.20f}")