#1
"""
seasons= ("spring", "summer", "autumn", "winter")
month=int(input("Enter the5 month's number "))
if(month==12 or month<=2) : print(f"It's {seasons[3]}")
elif (month<=5): print(f"It's {seasons[0]}")
elif (month<=8): print(f"It's {seasons[1]}")
else : print(f"It's {seasons[2]}")
"""
#2
name=input("Enter a name ")
name_list=set()
okay = True
while(name!=""):
    
    for n in name_list:
        if n==name : 
            print("Existing name")
            okay=False
    if(okay==True):
         print("New name")
    okay=True
    name_list.add(name)
    name=input("Enter a name ")

for n in name_list:
    print(n)

#3