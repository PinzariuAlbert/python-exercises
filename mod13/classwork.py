with open("cat.txt", "a") as cat_file:
    cat_file.write("This is new stuff cats.\n")
with open("cat.txt", "a") as file:
    file.write("newer stuff.\n")
with open("cat.txt", "r") as file:
    data = file.read()
    print(data)
    #there is also read.line()
    #aaand read.lines() which stores lines in a list