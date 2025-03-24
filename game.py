#game.py
#3/23/2025
#Emma Griffin

import gamefunctions
import random

player_name = input("Enter your name: ")
welcome_message = gamefunctions.print_welcome(player_name)
print(welcome_message)

def mainLoop():
    userHP = 30
    userGold = 10
    while True: 
        print(f'You are in a town.\nCurrent HP: {userHP}, Current Gold: {userGold}\n')
        print('What would you like to do?')
        print(f'1) Leave town (Fight a monster)\n2) Sleep (Restore HP for 5 gold)\n3) Quit\n')
        userChoice = input("Enter a number to make your selection: ")
        if userChoice == "1":
            userHP, userGold = gamefunctions.fight_monster(userHP, userGold)
        elif userChoice == "2":
            userHP, userGold = gamefunctions.sleep(userHP, userGold)
        elif userChoice == "3":
            print("Thanks for playing, goodbye!")
            break
        else:
            print(f"\nInvalid choice. Please select 1, 2, or 3.\n")
mainLoop()
