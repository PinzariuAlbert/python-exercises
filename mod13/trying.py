try: 
    with open("horse.txt", "r") as file:
        file_content = file.read()
        print(file_content)
except FileNotFoundError as e:
    print(e)
except IOError as e:
    print(e)