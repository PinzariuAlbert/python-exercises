#1
fish_size=input("What is the value of your zander(cm)?\n")
if float(fish_size) >= 42: print("The fish is long enough to keep!")
else: print("The fish is too small, you need to release it.")

#2
cabin_class= input("What's your cabin class? ")
if cabin_cass=="LUX": print("LUX: upper-deck cabin with a balcony.")
elif cabin_cass=="A": print("A: above the car deck, equipped with a window.")
elif cabin_cass=="B": print("B: windowless cabin above the car deck.")
elif cabin_cass=="c": print("C: windowless cabin below the car deck.")
else : print("Invalid cabin class.")

#3
gender = input("What is your biological gender(m/f)? ")
globin = float(input("What is your hemoglobin value(g/l)? "))
if gender=="m" or gender=="M":
     if globin >167 : print("Your hemoglobin is high!")
     elif globin>=134 : print("Your hemoglobin is normal.")
     else  : print("Your hemoglobin is low!")
else:
     if globin >155 : print("Your hemoglobin is high!")
     elif globin>=117 : print("Your hemoglobin is normal.")
     else  : print("Your hemoglobin is low!")

#4
year=int(input("Enter the year you were born in: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year.")