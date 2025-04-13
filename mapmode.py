#mapmode.py
#4/13/2025
#Emma Griffin


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
MONSTER_POS = (5, 5)

map_state = {
    'player_pos': [0, 0],
    'visited_monster': False
}

def start_map_mode():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Map Navigation")

    clock = pygame.time.Clock()
    running = True

    player_x, player_y = map_state['player_pos']
    visited_monster = map_state['visited_monster']

    def draw_grid():
        screen.fill(WHITE)
        for x in range(0, SCREEN_SIZE, TILE_SIZE):
            for y in range(0, SCREEN_SIZE, TILE_SIZE):
                rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, BLACK, rect, 1)

        town_rect = pygame.Rect(TOWN_POS[0]*TILE_SIZE, TOWN_POS[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.circle(screen, GREEN, town_rect.center, TILE_SIZE//3)

        monster_rect = pygame.Rect(MONSTER_POS[0]*TILE_SIZE, MONSTER_POS[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.circle(screen, RED, monster_rect.center, TILE_SIZE//3)

        player_rect = pygame.Rect(player_x * TILE_SIZE, player_y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, BLUE, player_rect)

    while running:
        draw_grid()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player_y > 0:
                    player_y -= 1
                elif event.key == pygame.K_DOWN and player_y < GRID_SIZE - 1:
                    player_y += 1
                elif event.key == pygame.K_LEFT and player_x > 0:
                    player_x -= 1
                elif event.key == pygame.K_RIGHT and player_x < GRID_SIZE - 1:
                    player_x += 1

                map_state['player_pos'] = [player_x, player_y]

                if (player_x, player_y) == TOWN_POS:
                    pygame.quit()
                    return 'town'

                if (player_x, player_y) == MONSTER_POS and not visited_monster:
                    map_state['visited_monster'] = True
                    map_state['player_pos'] = [player_x, player_y]
                    pygame.quit()
                    return 'monster'

        clock.tick(30)

