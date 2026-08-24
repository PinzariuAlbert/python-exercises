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

n1=int(input("first number "))
n2=int(input("second number "))
result= n1+n2
print(type(n1))
print(type(n2))
print(result)

print(type(result))
division = n1/n2
print(division)
print(type(division))

print(id(n1)==id(n2))