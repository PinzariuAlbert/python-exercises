import os
clear = lambda: os.system('cls')

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
               break
            else:
               print("Invalid option. Please try again.")
     elif(command=="continue" or command == "CONTINUE" or command=="2"):
        print("You will continue from your save!") 
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
