import os
import json
clear = lambda: os.system('cls')
SAVE_FILE = "savegame.txt"
name=input("Enter your name: ")
age=input("Enter your age: ")

"""print("I think your name is "+ name + " and you are "+ age +" years old")"""

class Player():
   def __init__(self, name, items, room):
      self.name = name
      self.items = items
      self.room=room
   def move(self,room):
      self.room=room
   def collect_item(self, item):
      self.items.append(item)
   def show_items(self):
    for item in self.items:
        print(item.name)
class Room():
   def __init__(self, name, item=None):
      self.name = name
      self.item = item
class Item():
   def __init__(self, name, weight=1):
      self.name = name
      self.weight = weight

def read_file(filename):
    with open(filename, "r") as file:
        return file.read()
def save_game(player, rooms):
    data = {
        "player_name": player.name,
        "current_room": player.room.name,
        "inventory": [
            {
                "name": item.name,
                "weight": item.weight
            }
            for item in player.items
        ],
        "room_items": {
            room.name: (
                {
                    "name": room.item.name,
                    "weight": room.item.weight
                }
                if room.item is not None else None
            )
            for room in rooms.values()
        }
    }
    with open(SAVE_FILE, "w") as file:
        json.dump(data, file)
    print("Game saved!")
def load_game():
    try:
        with open(SAVE_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No saved game found.")
        return None, None
    entrance = Room("Entrance")
    basement = Room("Basement")
    lobby = Room("Lobby")
    kitchen = Room("Kitchen")

    rooms = {
        "entrance": entrance,
        "basement": basement,
        "lobby": lobby,
        "kitchen": kitchen
    }
    for room_name, item_data in data["room_items"].items():
        if item_data is not None:
            item = Item(
                item_data["name"],
                item_data["weight"]
            )
            rooms[room_name.lower()].item = item
    items = []
    for item_data in data["inventory"]:
        item = Item(
            item_data["name"],
            item_data["weight"]
        )
        items.append(item)
    room_name = data["current_room"]
    player = Player(
        data["player_name"],
        items,
        rooms[room_name.lower()]
    )
    print("Game loaded!")

    return player, rooms
def exit_def(): 
   print("Goodbye")
def item_add(requested):
   item_list.append(requested)
def item_show():
   print(item_list)

item_list=[]
if int(age)<12 : print("Access denied.")
else: 

    exit=False
    clear()
    try:
      with open("intro.txt", "r") as file:
        print(file.read())
    except FileNotFoundError:
         print("intro.txt was not found.")

    try:
      with open("instructions.txt", "r") as file:
        print(file.read())
    except FileNotFoundError:
      print("instructions.txt was not found.") 
    while(exit==False) :
     print(f"\nWelcome to the game,{name}\n")
     print("TITLE\n\n")
     print("1. START")
     print("2. COTINUE")
     print("3. ADD ITEM")
     print("4. SHOW ITEMS")
     print("5. OPTIONS")
     print("6. LOPETA")
     command= input("What command would you like to execute? ")
     if(command=="start" or command=="START" or command=="1"):
         print("You started the game!!")
         key = Item("Key", 1)
         potion= Item("Potion", 2)
         coin = Item("Coin", 1)

         entrance = Room("Entrance", key)
         basement = Room("Basement", potion)
         lobby = Room("Lobby", coin)
         kitchen = Room("Kitchen")
         rooms = {
            "entrance": entrance,
            "basement": basement,
            "lobby": lobby,
            "kitchen": kitchen
            }
         player = Player(name,[], entrance)
         while(True):
            print("Commands:")
            print(f"Current room: {player.room.name}")
            print("1. Move to another room 2. Collect an item\n"+"3. Show items 4. Show room information\n"+"5. Quit")
            command = input("Choose an option: ").strip()

            if command == "1":
               print("Available rooms:")
               for room_name in rooms:
                   print(f" {room_name}")
               destination = input("Enter the room name: ")

               if destination in rooms:
                  player.move(rooms[destination])
               else:
                  print("Room not found.")

            elif command == "2":
               if(player.room.item !=None):
                  player.collect_item(player.room.item)
                  player.room.item=None
               else:
                  print("There is no item here.")

            elif command == "3":
               player.show_items()

            elif command == "4":
               print(f"Room: {player.room.name}")
               if(player.room.item!=None):
                  print(f"Item here: {player.room.item.name}")
               else: print("There room is empty.")
            elif command == "5":
               print(f"Goodbye, {player.name}!")
               save_game(player, rooms)
               break
            else:
               print("Invalid option. Please try again.")
     elif(command=="continue" or command == "CONTINUE" or command=="2"):
      print("You will continue from your save!")
      try:
         player, rooms = load_game()
         print( f"Welcome back, {player.name}!")
         while (True):
            print("Commands:")
            print(f"Current room: "f"{player.room.name}")
            print("1. Move to another room 2. Collect an item\n"+"3. Show items 4. Show room information\n"+"5. Quit")
            command = input( "Choose an option: " )
            if command == "1":
                     print("Available rooms:")
                     for room_name in rooms:
                        print(f" {room_name}")
                     destination = input("Enter the room name: ")

                     if destination in rooms:
                        player.move(rooms[destination])
                     else:
                        print("Room not found.")

            elif command == "2":
               if(player.room.item !=None):
                  player.collect_item(player.room.item)
                  player.room.item=None
               else:
                  print("There is no item here.")

            elif command == "3":
               player.show_items()

            elif command == "4":
               print(f"Room: {player.room.name}")
               if(player.room.item!=None):
                  print(f"Item here: {player.room.item.name}")
               else: print("There room is empty.")
            elif command == "5":
               print(f"Goodbye, {player.name}!")
               save_game(player, rooms)
               break
            else:
               print("Invalid option. Please try again.")

      except FileNotFoundError:
                print("No saved game found.") 
     elif(command=="add item" or command == "ADD ITEM" or command=="3"):
        item=input("What item would you like to add? ")
        item_add(item)
     elif(command=="show items" or command == "SHOW ITEMS" or command=="4"):
        item_show()
     elif(command=="options" or command == "OPTIONS" or command=="5"):
        print("This is the options menu")  
     elif(command=="lopeta" or command == "LOPETA" or command=="6"):
        exit_def()
        exit=True
