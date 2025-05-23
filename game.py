#game.py
#5/4/2025
#Emma Griffin

import gamefunctions
import random
from mapmode import start_map_mode
from wanderingMonster import new_wandering_monster
import sys

def initial_menu():
    has_loaded_game = False
    load_choice = input('Would you like to load a previous game? (y/n) ')
    
    if load_choice.lower() == 'y':
        filename = input('Enter the save filename: ')
        game_data = gamefunctions.load_game(filename)
        
        if game_data:
            inventory = game_data['inventory']
            userHP = game_data['userHP']
            userGold = game_data['userGold']
        has_loaded_game = True
        
    else:
        print(f'Starting new game!')
        inventory = gamefunctions.inventory
        userHP = 30
        userGold = 10
        save_choice = input('Would you like to specifiy a filename? (y/n) ')
        if save_choice.lower() == 'y':
            filename = input('Enter your filename: ')
        elif save_choice.lower() == 'n':
            filename = 'Unnamed save'
        else:
            print('Invalid option')
        gamefunctions.save_game(userHP, userGold, inventory, filename)
        
        
    player_name = input("Enter your name: ")
    welcome_message = gamefunctions.print_welcome(player_name)
    print(welcome_message)
    
    return userHP, userGold, inventory, filename, has_loaded_game

def mainLoop(userHP, userGold, selected_item, inventory,filename):
    in_town = True
    
    while True:
        if in_town:
            print(f'You are in a town.\nCurrent HP: {userHP}, Current Gold: {userGold}\n')
            print('What would you like to do?')
            print(f'1) Leave town (Fight a monster)\n2) Sleep (Restore HP for 5 gold)\n3) View player menu\n4) Save and quit\n')
            userChoice = input("Enter a number to make your selection: ")
        else:
            userChoice == "1"
            
        if userChoice == "1":
            in_town = False
            result = start_map_mode() 
    
            if result == "monster":
                from mapmode import map_state
                monster = map_state['current_monster']
                outcome = gamefunctions.fight_monster(userHP, userGold, selected_item, inventory, monster)
                if isinstance(outcome, tuple) and len(outcome) == 4:
                    userHP, userGold, selected_item, inventory = outcome

                    if monster in map_state['monsters']:
                        map_state['monsters'].remove(monster)
                    
                    if not map_state['monsters']:
                        TOWN_POS = (0,0)
                        occupied = {tuple(map_state['player_pos']), TOWN_POS}
                        monster1 = new_wandering_monster(occupied)
                        occupied.add(monster1.location)
                        monster2 = new_wandering_monster(occupied)
                        map_state['monsters'] = [monster1, monster2]
                else:
                    print("Unexpected battle outcome")
                    
            elif result == "npc":
                from mapmode import map_state
                npc = map_state['current_npc']
                print(f'\nYou meet {npc.name}.\nThey say: "{npc.message}"\n')

            elif result == "town":
                print(f'Returned to town\n')
                in_town = True
            
        elif userChoice == "2":
            userHP, userGold = gamefunctions.sleep(userHP, userGold)
            
        elif userChoice == "3":
            userHP, userGold, selected_item, inventory, filename = playerMenu(userHP, userGold, selected_item, inventory, filename)
            
        elif userChoice == '4':
            gamefunctions.save_game(userHP, userGold, inventory, filename)
            sys.exit()
            
        else:
            print(f"\nInvalid choice. Please select 1, 2, or 3.\n")
            
    return userHP, userGold, selected_item, inventory, filename

def playerMenu(userHP, userGold, selected_item, inventory, filename):
    while True:
        print(f'\nWelcome to the player menu!')
        print(f'Current HP: {userHP}\nCurrent Gold: {userGold}')
        
        if selected_item and selected_item.get('type') == 'weapon':
            print(f'Equipped item: {selected_item["name"]} (Durability: {selected_item["currentDurability"]})\n')
        print(f'Options:\n1) See shop menu\n2) View inventory\n3) Exit player menu\n')
        userChoice2 = input("Enter a number to make your selection: ")
        
        if userChoice2 == '1': 
            gamefunctions.print_shop_menu("Sword", 10.00, "Axe", 12.00)
            item1Price = 10.00
            item2Price = 12.00
            shopChoice = input(f"\nWhat would you like to purchase? (Q to quit) ")
            if shopChoice.lower() == 'sword':
                if userGold >= item1Price:
                    userGold -= item1Price
                    inventory.append({"name": "Sword", "type": "weapon", "damage": 5, "currentDurability": 25})
                else:
                    print('Not enough money')
            elif shopChoice.lower() == 'axe':
                if userGold >= item2Price:
                    userGold -= item2Price
                    inventory.append({"name": "Axe", "type": "weapon", "damage": 8, "currentDurability": 20})
                else:
                    print('Not enough money')
            elif shopChoice == 'Q':
                print('No purchase made')
            else:
                print(f'\nInvalid choice.')
                
        elif userChoice2 == '2': 
            print(f'\nYour inventory:\n')
            for item in inventory:
                print(f'{item['name']} ({item['type']})')
                if item['type'] == 'weapon':
                    print(f"    Current {item['name']} durability: {item['currentDurability']}")
                    
        elif userChoice2 == '3':
            userHP, userGold, selected_item, inventory, filename = mainLoop(userHP, userGold, selected_item, inventory, filename)
            
        else:
            print(f'\nInvalid choice')
            
    return userHP, userGold, selected_item, inventory, filename

if __name__ == "__main__":
    userHP, userGold, inventory, filename, has_loaded_game = initial_menu()
    selected_item = None
    mainLoop(userHP, userGold, selected_item, inventory,filename)
