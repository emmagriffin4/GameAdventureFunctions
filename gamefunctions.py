#gamefunctions.py
#Updated 3/9/2025
#Emma Griffin
import math
import random

#after updating, this function will return the values of num_purchased and leftover_money
    #rather than printing
def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int=1): 
    if quantityToPurchase * itemPrice <= startingMoney:
        num_purchased = quantityToPurchase
        leftover_money = startingMoney - (itemPrice * quantityToPurchase) 
    else:
       num_purchased = startingMoney / itemPrice
       leftover_money = startingMoney - (itemPrice * (startingMoney / itemPrice))
    if num_purchased < 1:
        num_purchased = 0
    return num_purchased, leftover_money

#after updating, this function will return a monster, with random health, power, and money
def new_random_monster():
    monsters = [ {'name': 'A dragon',
                  'description': 'You see a dragon in the distance flying near a mountain. You make sure to go the opposite direction.',
                  'health_range': random.randint(100, 200),
                  'power_range': random.randint(50, 100),
                  'money_range': random.randint(300, 500) },
                 {'name': 'A siren',
                  'description': 'You hear a beautiful song near the water and go to explore..',
                  'health_range': random.randint(15, 30),
                  'power_range': random.randint(20, 30),
                  'money_range': random.randint(30, 50) },
                 {'name': 'A centaur',
                  'description': 'You discover a group of centaurs hunting in the woods. Their village must be nearby.',
                  'health_range': random.randint(40, 60),
                  'power_range': random.randint(20, 50),
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
    
                   
#Function 1, call 1 (shows basic example) -- UPDATED
num_purchased, leftover_money = purchase_item(1.23, 10, 3)
print(num_purchased)
print(leftover_money)
print()

#Function 1, call 2 (shows default value of quantityToPurchase is 1) -- UPDATED
num_purchased, leftover_money = purchase_item(3.41, 21.12)
print(num_purchased)
print(leftover_money)
print()

#Function 1, call 3 (shows what happens if not enough money) -- UPDATED
num_purchased, leftover_money = purchase_item(5.0, 4.0)
print(num_purchased)
print(leftover_money)
print()

#Function 2, call 1 -- UPDATED
my_monster = new_random_monster()
print(my_monster['name'])  
print(my_monster['description'])  
print(my_monster['health'])
print(my_monster['power'])
print(my_monster['money'])
print()

#Function 2, call 2 -- UPDATED
my_monster = new_random_monster()
print(my_monster['name'])  
print(my_monster['description'])  
print(my_monster['health'])
print(my_monster['power'])
print(my_monster['money'])
print()

#Function 2, call 3 -- UPDATED
my_monster = new_random_monster()
print(my_monster['name'])  
print(my_monster['description'])  
print(my_monster['health'])
print(my_monster['power'])
print(my_monster['money'])
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

