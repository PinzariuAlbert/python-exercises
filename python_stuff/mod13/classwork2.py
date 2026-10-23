with open("shopping.txt", "w") as awa:
    awa.write("milk\nbread\neggs")
with open("shopping.txt", "a") as awa:
    awa.write("\napples")

with open("shopping.txt", "r") as awaw:
    grocery_list=awaw.readlines()
    print(f"Items on the list: {len(grocery_list)}")
    for line in grocery_list:
        print(line, end="")