"""def greet(times):
    for i in range(times):
        print("Round " + str(i+1) + " of saying hello.")
    return

print("A new day starts with greetings.")
greet(5)
print("Let's greet some more.")
greet(2)
def change():
    city = "Vantaa"
    print("At the end of the function: " + city)
    return

city = "Helsinki"
print("At the beginning in the main program: " + city)
change()
print("At the end of the main program: " + city)"""

def averages(float_list):
    float_sum = 0
    for i in float_list:
        float_sum = float_sum+i
    return float_sum/len(float_list)
main_list= [0.2143,12,23.43,9]
print(f"The average of your numbers is: {averages(main_list)}")

average_list=[]
def average_grade(lists_list):
    for i in lists_list:
            average_list.append(averages(i))
average_grade([[21,32,2.43],[122,34,12.23]])
for n in range(len(average_list)):
    
    print(f"This is the {n+1} average: {average_list[int(n-1)]}")
            
