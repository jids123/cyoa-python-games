import time
from games import cave, forest, sheriff, house, survival
from othercodes import othercodes

name = input("Your name, please? \n")
print("Welcome! Start your adventure, here are your options " + name)
while True:
    time.sleep(2)
    mainInput = input("'forest' - The Forest \n"
                      "'house' - Escape the house \n"
                      "'cave' - Caveman's Journey \n"
                      "'survival' - Survival Island \n"
                      "'sheriff' - Sheriff of the West \n"
                      "'exit' - Exit game \n").lower().strip()
    othercodes.confirmation(name)
    choice = input("(1) yes (2) no \n")

    if choice == "1" and mainInput == "forest":
        forest.startforestgame()
    elif choice == "1" and mainInput == "house":
        house.starthousegame()
    elif choice == "1" and mainInput == "cave":
        cave.startcavegame()
    elif choice == "1" and mainInput == "survival":
        survival.startsurvivalgame()
    elif choice == "1" and mainInput == "sheriff":
        sheriff.startsheriffgame()
    elif choice == "1" and mainInput == "exit":
        exit()
    elif choice == "2":
        print("okay")
    else:
        print("There are only two options. I'll forgive you but you need...\n"
              "to wait for 5 seconds...")
        time.sleep(5)
