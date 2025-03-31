#gamefunctions.py
#Updated 3/23/2025
#Emma Griffin

"""This module consists of various gamefunctions for a text-based game.

The game functions included in this module are purchase_item,
new_random_monster, print_welcome, and print_shop_menu."""

import math
import random

def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int=1):
    """
    Allows the player to purchase an item (or items).
    Parameters:
        itemPrice (float): The price of the item.
        startingMoney (float): The amount of money the player has before purchasing.
        quantityToPurchase (int=1): How many items the player needs to purchase, with the default being 1.
    Returns:
        num_purchased: Returns the amount of items the player was able to purchase.
        leftover_money: Returns the money leftover aftering purchasing said amount of items.
    """
    if quantityToPurchase * itemPrice <= startingMoney:
        num_purchased = quantityToPurchase
        leftover_money = startingMoney - (itemPrice * quantityToPurchase) 
    else:
       num_purchased = startingMoney / itemPrice
       leftover_money = startingMoney - (itemPrice * (startingMoney / itemPrice))
    if num_purchased < 1:
        num_purchased = 0
    return num_purchased, leftover_money

def new_random_monster():
    """
    Generates a random monster that the player might encounter.
    Parameters:
        None
    Returns:
        monster: Returns the name, description, and health, power, and money stats of the selected monster.
    """
    monsters = [ {'name': 'Dragon',
                  'description': 'You see a dragon flying near a mountain.',
                  'health_range': random.randint(20, 50),
                  'power_range': random.randint(5, 15),
                  'money_range': random.randint(300, 500) },
                 {'name': 'Siren',
                  'description': 'You hear a beautiful song near the water.',
                  'health_range': random.randint(15, 30),
                  'power_range': random.randint(3, 8),
                  'money_range': random.randint(30, 50) },
                 {'name': 'Centaur',
                  'description': 'You discover a lone centaur hunting in the woods.',
                  'health_range': random.randint(30, 40),
                  'power_range': random.randint(5, 10),
                  'money_range': random.randint(20, 40) } ]
    selected_monster = random.choice(monsters)
    health = selected_monster['health_range']
    power = selected_monster['power_range']
    money = selected_monster['money_range']
    monster = {'name': selected_monster['name'],
               'description': selected_monster['description'],
               'health': health,
               'power': power,
               'money': money}
    return monster

def print_welcome(name: str, width: int=20):
    """
    Prints a welcome sign with the players name.
    Parameters:
        name (str): The player's name
        width (int=20): The width of the welcome sign, the default is 20.
    Returns:
        Newline
    """
    print(f'\n{"Hello, " + name + "!":^{width}}',end='')
    return "\n"

def print_shop_menu(item1Name:str, item1Price:float, item2Name:str, item2Price:float):
    """
    Displays a shop menu with items and their associated prices.
    Parameters:
        item1Name (str): The name of the first item to be displayed.
        item1Price (float): The associated price of item1.
        item2Name (str): The name of the second item to be displayed.
        item2Price (float): The associated price of item2.
    Returns:
        Newline
    """
    price1_str = str(f"{item1Price:.2f}")
    price2_str = str(f"{item2Price:.2f}")
    print('/' + '-'*22 + '\\')
    print(f'| {item1Name:<12}{"$" + price1_str:>8} |')
    print(f'| {item2Name:<12}{"$" + price2_str:>8} |')
    print('\\' + '-' * 22 + '/', end='')
    return "\n"

def displayFightStatistics(userHP, monsterHP):
    """
    Displays the users and monsters health during the fight
    Parameters:
        userHP: the players health
        monsterHP: the monsters health
    Returns:
        None
    """
    print(f"\nYour HP: {userHP}, Monster's HP: {monsterHP}")
       
def getUserFightOptions():
    """
    Displays a menu during a monster fight in which the player can chose to keep fighting, use an item, or run away
    Parameters:
        None
    Returns:
        user chocie
    """
    print("What would you like to do?")
    print("1) Attack\n2) Use item\n3) Run away\n")
    while True:
        userOption = input("Enter 1, 2, or 3: ")
        if userOption == "1":
            return "fight"
        elif userOption == "2":
            return "use"
        elif userOption == "3":
            return "run"
        else:
            print("Invalid. Please select 1 or 2.")

def fight_monster(userHP, userGold, selected_item):
    """
    This function contains the code for a monster fight. The user and monster both deal random power
    and have random health.
    Parameters:
        userHP (str): The health of the user
        userGold (str): The amount of gold the user has
    Returns:
        userHP: The users HP after the fight is complete or the user has fled
        userGold: The amount of gold the user has, updated if the user defeats the monster and wins gold
    """
    monster_encounter = new_random_monster()
    monsterHP = monster_encounter['health']
    monster_damage = monster_encounter['power']
    if selected_item is not None and selected_item.get("type") == "weapon" and selected_item.get("currentDurability") > 0:
        user_damage = random.randint(5,10)
        print(f'\nYou are fighting a {monster_encounter['name']} (HP:{monsterHP}) with your sword!\nYour damage is increased!')
    else:
        user_damage = random.randint(1,4)
        print(f'\nYou are fighting a {monster_encounter['name']} (HP: {monsterHP}) without a weapon!\nYou both take your first hits!')
    while userHP > 0 and monsterHP > 0:
        monsterHP -= user_damage
        userHP -= monster_damage
        displayFightStatistics(userHP, monsterHP)
        if userHP <= 0:
            print(f"You have been defeated by the {monster_encounter['name']}!\n")
            break
        elif monsterHP <= 0:
            print(f"Congratulations! You have defeated the {monster_encounter['name']}!\n")
            userGold += random.randint (10, 20) #User earns a random amount of gold if they win
            selected_item['currentDurability'] = 0
            break
        choice = getUserFightOptions()
        if choice == "run":
            print (f'\nYou ran away.\n')
            break
        elif choice == "use":
            print(f"\nYour inventory:")
            for index, item in enumerate(inventory):
                print(f"{index+1}) {item['name']} - Type: {item['type']}")
            item_choice = int(input("Enter the number of the item to use: "))
            if item_choice > 0 and item_choice <= len(inventory):
                item = inventory[item_choice - 1]
            if item['name'].lower() == 'magic rock':
                print(f'\nYou used the magic rock and defeated the monster!\n')
                monsterHP = 0
                userGold += random.randint (10, 20)
                break
            else:
                if item['type'] == "weapon" and item['currentDurability'] > 0:
                    user_damage = random.randint(5, 10)
                    print(f'Your damage has increased!')              
    return userHP, userGold, selected_item

def sleep(userHP, userGold):
    """
    This function allows the player to gain 10 HP for 5 gold
    Parameters:
        userHP: the amount of HP the player has before sleeping
        userGold: the amount of gold the player has before sleeping
    Returns:
        userHP: the amount of HP the player has after sleeping
        userGold: the amount of gold the player has after sleeping
    """
    if userGold >= 5:
        userGold -= 5
        userHP += 10
        print (f"You slept and restored 10 HP. You have {userHP} HP and {userGold} gold.\n")
    else:
        print(f"\nNot enough gold to sleep.\n")
    return userHP, userGold

inventory = [
        {"name": "Map", "type": "tool", "description": "A map of the area."},
        {"name": "Magic rock", "type": "misc.", "note": "Can be used to kill a monster instantly!"}
            ]

def equip_item(inventory, item_type="weapon"):
    itemsToEquip = [item for item in inventory if item["type"] == item_type]
    if not itemsToEquip:
        print(f"No {item_type}s in inventory")
        return None
    print(f'Select a {item_type} to equip: ')
    for index, item in enumerate(itemsToEquip):
        print(f'{index+1}) {item["name"]} (Durability: {item["currentDurability"]})')
    userEquip = int(input(f'Enter the number to equip (0 to cancel) '))
    if userEquip == 0:
        return None
    elif 0 < userEquip <= len(itemsToEquip):
        selected_item = itemsToEquip[userEquip - 1]
        print(f'Equipped {selected_item["name"]}.')
        return selected_item
    else:
        print("Invalid selection")
        return None
    pass
    
def test_functions():
    num_purchased, leftover_money = purchase_item(1.23, 10, 3)
    print(num_purchased)
    print(leftover_money)
    print()
    num_purchased, leftover_money = purchase_item(3.41, 21.12)
    print(num_purchased)
    print(leftover_money)
    print()
    num_purchased, leftover_money = purchase_item(5.0, 4.0)
    print(num_purchased)
    print(leftover_money)
    print()
    my_monster = new_random_monster()
    print(my_monster['name'])  
    print(my_monster['description'])  
    print(my_monster['health'])
    print(my_monster['power'])
    print(my_monster['money'])
    print()
    my_monster = new_random_monster()
    print(my_monster['name'])  
    print(my_monster['description'])  
    print(my_monster['health'])
    print(my_monster['power'])
    print(my_monster['money'])
    print()
    my_monster = new_random_monster()
    print(my_monster['name'])  
    print(my_monster['description'])  
    print(my_monster['health'])
    print(my_monster['power'])
    print(my_monster['money'])
    print()
    print_welcome("Daenerys") 
    print()
    print_welcome("Jon")
    print()
    print_welcome("Catelyn")
    print()
    print_shop_menu("Wheat", 16.50, "Bread", 5.00)
    print()
    print_shop_menu("Pear", 2.497, "Banana", 3)
    print()
    print_shop_menu("Mana Potion", 10, "Wand", 20.50 )


if __name__ == "__main__":
    test_functions()

