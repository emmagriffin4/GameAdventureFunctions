#wanderingMonster.py
#4/20/2025
#Emma Griffin

import random

GRID_WIDTH = 10
GRID_HEIGHT = 10
TOWN_POS = (0,0)


class WanderingMonster:

    RED = (255, 0, 0)
    BROWN = (150, 75, 0)
    TEAL = (64, 224, 208)
    
    monster_types = {
        "dragon": RED,
        "siren": TEAL,
        "centaur": BROWN}

    def __init__(self, monster_type, location, gold, health, power):
        """
        Initialize tje information of the class
        Parameters:
            self: references itself
            monster_type(str): the type of monster
            location: the location of the monster
            gold (str): the amount of money the monster has
            health (str): the health of the monster
            power (str): the power of the monster
        Returns:
            None
        """
        self.monster_type = monster_type.lower()
        self.color = WanderingMonster.monster_types[monster_type]
        self.location = location
        self.gold = gold
        self.health = health
        self.power = power

    def move(self, occupied_positions):
        """
        Moves the monster in a random direction
        Parameters:
            self: itself
            occupied_postions: ensures the monster doesn't move onto an occupied spot
        Returns:
            None
        """
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        random.shuffle(directions)

        for x, y in directions:
            new_x = self.location[0] + x
            new_y = self.location [1] + y
            new_loc = (new_x, new_y)
            if (0 <= new_x < GRID_WIDTH and
                0 <= new_y < GRID_HEIGHT and
                new_loc != TOWN_POS and
                new_loc not in occupied_positions):
                self.location = new_loc
                break

def new_random_monster():
    """
    Generates a random monster that the player might encounter
    (originally in gamefunctions.py)
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


def new_wandering_monster(existing_locations):
    """
    Generates a new random wandering monster
    Parameters:
        existing_locations: the existing location of the monster
    Returns:
        WanderingMonster(...): returns the information of the monster
    """ 
    data = new_random_monster() 
    monster_type = data['name'].lower() 
    gold = data['money']
    health = data.get('health')
    power = data.get('power')
    

    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        location = (x, y)
        if location != TOWN_POS and location not in existing_locations:
            break
    
    return WanderingMonster(monster_type, location, gold, health, power)
    
