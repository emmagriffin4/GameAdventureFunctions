#gamefunctions.py
#2/16/2025
#Emma Griffin
import math
import random

#this function prints the how much of an item was purchased and the leftover money
    #after purchasing
def purchase_item(itemPrice, startingMoney, quantityToPurchase=1): #parameters are price, money, and quanitity
    if quantityToPurchase * itemPrice <= startingMoney:
        num_purchased = quantityToPurchase
        leftover_money = startingMoney - (itemPrice * quantityToPurchase) 
    else:
       num_purchased = startingMoney / itemPrice
       leftover_money = startingMoney - (itemPrice * (startingMoney / itemPrice))
    if num_purchased < 1:
        print('Not enough money')
    else:
        print(num_purchased)
        print(leftover_money)

#this function returns a random monster with random health, power, and money
def new_random_monster(): #no required parameters
    dragon_dict = {'Name': "A Dragon", 'Health': 200, 'Power': 100, 'Money': 500, 'Description':
                   """You see a dragon in the distance flying near a mountain. You make """
                    """sure to go the opposite direction."""}

    print(dragon_dict['Name'])
    print(dragon_dict['Description'])
    print('Health:', dragon_dict['Health'])
    print('Power:', dragon_dict['Power'])
    print('Money:', dragon_dict['Money'])

    siren_dict = {'Name': "A siren", 'Health': 25, 'Power': 20, 'Money': 50, 'Description':
                   """You hear a beautiful song near the water and go to explore... """}

    print(siren_dict['Name'])
    print(siren_dict['Description'])
    print('Health:', siren_dict['Health'])
    print('Power:', siren_dict['Power'])
    print('Money:', siren_dict['Money'])

    centaur_dict = {'Name': "A centaur", 'Health': 50, 'Power': 25, 'Money': 20, 'Description':
                   """You discover a group of centaurs hunting in the woods. Their village """
                    """must be nearby."""}

    print(centaur_dict['Name'])
    print(centaur_dict['Description'])
    print('Health:', centaur_dict['Health'])
    print('Power:', centaur_dict['Power'])
    print('Money:', centaur_dict['Money'])

#the print_welcome function prints the given name
    #with a width of 20 and says Hello
def print_welcome(name: str, width: int=20): #parameters are name and width
        print(f'{"Hello, " + name + "!":^{width}}')

#print_shop_menu prints items and prices with a border around it
def print_shop_menu(item1Name:str, item1Price:float, item2Name:str, item2Price:float):
    #parameters are the item names and associated prices
    price1_str = str(f"{item1Price:.2f}")
    price2_str = str(f"{item2Price:.2f}")
    #prices are converted to strings in order to
    #add the $ next to it
    print('/' + '-'*22 + '\\')
    print(f'| {item1Name:<12}{"$" + price1_str:>8} |')
    print(f'| {item2Name:<12}{"$" + price2_str:>8} |')
    print('\\' + '-' * 22 + '/')
    
                   
#Function 1, call 1 (shows basic example)
purchase_item(1.23, 10, 3)
print()

#Function 1, call 2 (shows default value of quantityToPurchase is 1)
purchase_item (3.41, 21.12)
print()

#Function 1, call 3 (shows what happens if not enough money)
purchase_item (5.0,4.0)
print()

#Function 2, call 1
new_random_monster()
print()

#Function 3, call 1 (long name)
print_welcome("Daenerys") 
print()

#Function 3, call 2 (short name)
print_welcome("Jon")
print()

#Function 3, call 3
print_welcome("Catelyn")
print()

#Function 4, call 1
print_shop_menu("Wheat", 16.50, "Bread", 5.00)
print()

#Function 4, call 2 (numbers not formatted initally with two decimals)
print_shop_menu("Pear", 2.497, "Banana", 3)
print()

#Function 4, call 3
print_shop_menu("Mana Potion", 10, "Wand", 20.50 )

