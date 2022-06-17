
import sys
import os
import random
import time

player = {"location":"","health":100,"items":[]}

def print_slow(str, delay = 0.1):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def reset_console():
    print("\n")
    os.system('cls||clear')

def fprint(str,delay = 0):
    print("\n"+str)
    time.sleep(delay)

def sprint(str,delay = 0):
    print(str)
    time.sleep(delay)

# class NPC:
#     def __int__(self,name,location):
#         self.name = name
#         self.location = location
#     def talk(self):
#         if player["location"] == self.location:
#             fprint(f"A {self.name} emerges from the shadows.")
#             fprint("Stay where you are!")
#     def move(self):
#         available_locations = ["fireplace"]
#         self.location = random.choice(available_locations)
#
#
# stranded_person = NPC["Stranded person","fireplace"]


class NPC:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def talk(self):
        game_functions.fprint(f"A {self.name} emerges from the shadows.")
        game_functions.fprint("'Hisssss! Stay away from me!'")

    def move(self):
        available_locations = ["entry", "cavern", "hallway", "pit"]
        self.location = random.choice(available_locations)


goblin = NPC("goblin", "hallway")

# def start():
#     fprint("You wake up stranded on the shore of an island",2)
#     print("Someone opens the door.What do you do ?")
#     while True:
#         action = input("\n> ")
#         if action == "speak":
#             fprint("You try to speak with the person who opened the door..They ignore you")
#         elif action == "beg" or action == "scream":
#             fprint("The person punches you. You fall down and some tears fall from your eyes.")
#         elif action == "search" or action == "look":
#             fprint("You feel a pile of bones.Will you search in them?")
#             action1 = input("\n> ").lower()
#             if action1 == "yes":
#                 fprint("You find a bone that looks sharp and you add it to your inventory")
#             elif action1 == "no":
#                 fprint("You choose not to search.")
#         else:
#             fprint("Invalid action.\nYou sit in total darkness wondering if there's a way out.")


def start():
    global player
    print(f"\n Health: {player['health']}")
    fprint("You wake up stranded on the shore of an island",2)
    fprint("Ahead you can see some shelter and a makeshift fireplace. Will you continue ?")
    while True:
        action = input("\n> ").lower()
        if action == "yes":
            fireplace()
        elif action == "no":
            fprint("You look around and you see nothing else to do.")
        else:
            fprint("Invalid action.\nYou sit around soaked wondering if there's anything you can do.")

def fireplace():
    global player
    print(f"\n Health: {player['health']}")
    fprint("You reach the fireplace.This doesn't seem to be made recently.",2)
    fprint("You feel nauseaus.Your head is spinning and you are hungry.")
    fprint("You see multiple types of mushroomes growing on a nearby tree, do you eat them?")
    while True:
        action = input("\n> ").lower()
        if action == "yes":
            mushroom_eat = random.choice([True,False])
            if mushroom_eat == True:
                fprint("You eat the mushrooms.You feel weird.")
                player['health'] -= random.randint(1,20)
                print(f"\n Health: {player['health']}")
            if mushroom_eat == False:
                fprint("You feel better,you don't feel as hungry anymore, this gave you a boost of hope.")
                player['health'] += random.randint(1, 5)
        elif action == "no":
            fprint("You look around and you see nothing else to do.")
        else:
            fprint("Invalid action.\nYou sit in total darkness wondering if there's a way out.")

def hallway():
    pass

def pit():
    pass


start()


#
# input("Would you like to play ; Yes or No :")
#
#
#
#
# print(f"You wake on a ship..you feel your hands tied together..")
#
# while True:
#     choice1 = input('What do you do?: ')
#     if choice1 == "right":
#         print("you've chosen choice1")
#         continue
#     elif choice1 == "left":
#         print("you've chosen choice1")
#         continue
#     elif choice1 == "":
#         print("you've chosen choice1")
#
#
# print("Event 2: Someone opens the trap door")
#
# if choice1 == input(""):
#     print("you've chosen choice1")
# elif choice2 == input(""):
#     print("you've chosen choice1")
# elif choice3 == input(""):
#     print("you've chosen choice1")