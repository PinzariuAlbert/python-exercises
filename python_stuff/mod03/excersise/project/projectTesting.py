class Plot():
    def __init__(self,display_value=0, value=0, bugged=False):
        self.display_value=0  #uhhh, dont forget to use [ print(str(variable).zfill(2)) ]
        self.value=0
"""plot_matrix=[]
for i in range(9):
    for j in range(4):
        plot_matrix.append(Plot())
for i in range(9):
    for j in range(4):
        print(plot_matrix[i].display_value)
    print("\n")"""

#so this is what a matrix looks like in pytho(?)
matTest1=[[1,2],
     [3,4]]
for row in matTest1:
    print(row)
print("\n")
#how do you *not* hard code it???
matTest2=[]
for i in range(4):
    matTest2.append([0,0])
for i in matTest2:
    print(i)
print("\n")
#so i can make as many rows as I want.. how do i make more columns?
matTest3=[]
for i in range(4):
    full_row=[]
    for j in range(9):
        full_row.append(0)
    matTest3.append(full_row)
for i in matTest3:
    print(i)
print("\n")
# yup that works,,,,,, god i hate python, c++ is better
# shit, how do you get rid of the "[]"and ","?
for i in matTest3:
   # for j in range(matTest3.count):
   for j in i:
      print(j, end=" ")
   #print("\n")
   print()
# YEAH, that was it. 
#           NOTE: so basically the print() function ads a "\n" at the end of everything automatically
#                 so you have to specify that you want a " " at the end
#           NOTE: vai ce urasc pythonul...
print()
for i in matTest3:
    for j in i:
        print(str(j).zfill(2), end=" ")
    print()
print()

# ok ok, lets do this with game objects.abs
matTest4 = []
for i in range(4):
    row=[]
    for j in range(9):
        row.append(Plot())
    matTest4.append(row)
for i in matTest4:
    for j in i:
        print(str(j.display_value).zfill(2), end=" ")
    print()
