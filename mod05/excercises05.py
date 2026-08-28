#1
"""i=1
while(i<=1000) :
      if (i%3==0) : 
         print(f"I found a number dividable by 3!! {i}")
      i+=1

#2
inches=0
while(inches>=0):
    inches = int(input("Enter the number of inches: \n"))
    if(inches>=0) :
     print(f"Your number in centimeters: {inches*2.54}")"""

#3
number = input("Please enter a number or enter nothing to quit: ")
if number!="" :
   max_number= int(number)
   min_number = int(number)
   while(number != "") : 
       number = input("Please enter a number or enter nothing to quit: ")
       if(number!="") : 
          if(max_number< int(number)): max_number=int(number)
          if(min_number>int(number)): min_number=int(number)
   print(f"The biggest number was: {max_number} \nAnd the smallest one was: {min_number}")

#4