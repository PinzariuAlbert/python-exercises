
while(True):
    name=input("file name: ")
    try: 
       with open(f"{name}.txt", "r") as file:
        contents= file.read()
        print(contents)
        break
    except FileNotFoundError: print("File not found, try again")