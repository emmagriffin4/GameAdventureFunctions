#game.py
#3/23/2025
#Emma Griffin

import gamefunctions
import random

player_name = input("Enter your name: ")
welcome_message = gamefunctions.print_welcome(player_name)
print(welcome_message)

def mainLoop(userHP, userGold, selected_item):
    while True: 
        print(f'You are in a town.\nCurrent HP: {userHP}, Current Gold: {userGold}\n')
        print('What would you like to do?')
        print(f'1) Leave town (Fight a monster)\n2) Sleep (Restore HP for 5 gold)\n3) View player menu\n')
        userChoice = input("Enter a number to make your selection: ")
        if userChoice == "1":
            userHP, userGold, selected_item = gamefunctions.fight_monster(userHP, userGold, selected_item)
        elif userChoice == "2":
            userHP, userGold = gamefunctions.sleep(userHP, userGold)
        elif userChoice == "3":
            break
        else:
            print(f"\nInvalid choice. Please select 1, 2, or 3.\n")
    return userHP, userGold, selected_item

def playerMenu():
    userHP, userGold, selected_item = mainLoop(30,10,None)
    while True:
        print(f'\nWelcome to the player menu!')
        print(f'Current HP: {userHP}\nCurrent Gold: {userGold}')
        if selected_item:
            print(f'Equipped item: {selected_item["name"]} (Durability: {selected_item["currentDurability"]})\n')
        print(f'Options:\n1) See shop menu\n2) View inventory\n3) Exit player menu\n4) Quit game\n')
        userChoice2 = input("Enter a number to make your selection: ")
        if userChoice2 == '1':
            gamefunctions.print_shop_menu("Sword", 10.00, "Axe", 12.00)
            item1Price = 10.00
            item2Price = 12.00
            shopChoice = input(f"\nWhat would you like to purchase? (Q to quit) ")
            if shopChoice.lower() == 'sword':
                if userGold >= item1Price:
                    userGold -= item1Price
                    gamefunctions.inventory.append({"name": "Sword", "type": "weapon", "damage": 5, "currentDurability": 25})
                else:
                    print('Not enough money')
            elif shopChoice.lower() == 'axe':
                if userGold >= item2Price:
                    userGold -= item2Price
                    gamefunctions.inventory.append({"name": "Axe", "type": "weapon", "damage": 8, "currentDurability": 20})
                else:
                    print('Not enough money')
            elif shopChoice == 'Q':
                print('No purchase made')
            else:
                print(f'\nInvalid choice.')
        elif userChoice2 == '2':
            print(f'\nYour inventory:\n')
            for item in gamefunctions.inventory:
                print(f'{item['name']} ({item['type']})')
            print()
            selected_item = gamefunctions.equip_item(gamefunctions.inventory)
            
        elif userChoice2 == '3':
            userHP, userGold = mainLoop(userHP, userGold,selected_item)
        elif userChoice2 == '4':
            print('Thanks for playing, goodbye!')
            break
        else:
            print(f'\nInvalid choice')
    return userHP, userGold, selected_item
            
playerMenu()
