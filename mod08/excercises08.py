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
airports = {}
while True:
    print("Airport Information System ---")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Choose an option (1-3): ")
    if choice == "1":
        icao = input("Enter the ICAO code: ").upper().strip()
        name = input("Enter the airport name: ").strip()
        airports[icao] = name
        print(f"Airport {icao} successfully added.")
    elif choice == "2":
        icao = input("Enter the ICAO code to look up: ").upper().strip()
        if icao in airports:
            print(f"The name of the airport is: {airports[icao]}")
        else:
            print("Airport not found in the database.")
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("You need to pick between 1 2 or 3")
