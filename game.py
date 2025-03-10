#game.py
#3/8/2025
#Emma Griffin

import gamefunctions

player_name = input("Enter your name: ")
welcome_message = gamefunctions.print_welcome(player_name)
print(welcome_message)
print("Items for purchase")
print(gamefunctions.print_shop_menu('Sword', 10, 'Apple', 5))
purchase_choice = input("What would you like to purchase? ")
if purchase_choice.lower() == "apple":
    result = gamefunctions.purchase_item(5.00, 10.00)
    print("Amount purchased:",result[0])
    print(f'Leftover money: ${result[1]:.2f}')
elif purchase_choice.lower() == "sword":
    result = gamefunctions.purchase_item(10.00,10.00)
    print("Amount purchased:",result[0])
    print(f'Leftover money: ${result[1]:.2f}')
print()
monster_encounter = gamefunctions.new_random_monster()
print(monster_encounter['description'])
print(f'About this monster:')
print(f'  Name: {monster_encounter['name']}')
print(f'  Health: {monster_encounter['health']}')
print(f'  Power: {monster_encounter['power']}')
print(f'  Money: {monster_encounter['money']}')


        
