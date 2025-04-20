#mapmode.py
#4/20/2025
#Emma Griffin

from wanderingMonster import new_wandering_monster
import pygame

GRID_SIZE = 10
TILE_SIZE = 32
SCREEN_SIZE = GRID_SIZE * TILE_SIZE

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

TOWN_POS = (0, 0)

map_state = {
    'player_pos': [0, 0],
    'monsters' : [],
    'move_counter': 0
}

def start_map_mode():
    """
    Starts the map mode for the player to interact with
    No parameters or returns
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Map Navigation")

    clock = pygame.time.Clock()
    running = True

    player_x, player_y = map_state['player_pos']

    if not map_state['monsters']:
        occupied = {tuple(map_state['player_pos']), TOWN_POS}
        monster1 = new_wandering_monster(occupied)
        occupied.add(monster1.location)
        monster2 = new_wandering_monster(occupied)
        map_state['monsters'] = [monster1, monster2]

    def draw_grid():
        screen.fill(WHITE)
        for x in range(0, SCREEN_SIZE, TILE_SIZE):
            for y in range(0, SCREEN_SIZE, TILE_SIZE):
                rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, BLACK, rect, 1)

        town_rect = pygame.Rect(TOWN_POS[0]*TILE_SIZE, TOWN_POS[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.circle(screen, GREEN, town_rect.center, TILE_SIZE//3)

        for monster in map_state['monsters']:
            mx, my = monster.location
            m_rect = pygame.Rect(mx*TILE_SIZE, my*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.circle(screen, monster.color, m_rect.center, TILE_SIZE//3)

        player_rect = pygame.Rect(player_x * TILE_SIZE, player_y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, BLUE, player_rect)

    while running:
        draw_grid()
        pygame.display.flip()

        moved = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player_y > 0:
                    player_y -= 1
                    moved = True
                elif event.key == pygame.K_DOWN and player_y < GRID_SIZE - 1:
                    player_y += 1
                    moved = True
                elif event.key == pygame.K_LEFT and player_x > 0:
                    player_x -= 1
                    moved = True
                elif event.key == pygame.K_RIGHT and player_x < GRID_SIZE - 1:
                    player_x += 1
                    moved = True

                map_state['player_pos'] = [player_x, player_y]
                
                if moved:
                    map_state['player_pos'] = [player_x, player_y]
                    map_state['move_counter'] += 1

                    if map_state['move_counter'] % 2 == 0:
                        occupied = {monster.location for monster in map_state['monsters']}
                        occupied.add(TOWN_POS)
                        for monster in map_state['monsters']:
                            monster.move(occupied)

                    if (player_x, player_y) == TOWN_POS:
                        pygame.quit()
                        return 'town'

                    for monster in map_state['monsters']:
                        if (player_x, player_y) == monster.location:
                            map_state['current_monster'] = monster
                            map_state['player_pos'] = [player_x, player_y]
                            pygame.quit()
                            return 'monster'
                
                map_state['player_pos'] = [player_x, player_y]



        clock.tick(30)
