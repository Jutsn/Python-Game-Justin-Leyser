import pygame

POWER_UP_TEXT_COL = (255, 0, 0)
GAME_OVER_TEXT_COL = (0, 0, 0)
pop_up_text = "Stats"
player_health_text = "Health: " + str(2)
game_over_text = "Game Over"

is_pop_up_showing = False
start_time = 0
pop_up_time = 3
game_over=False


def draw_UI(screen, SCREEN_WIDTH, SCREEN_HEIGHT, game_state):
    global is_pop_up_showing
    if (is_pop_up_showing == True):
       pop_up_font = pygame.font.SysFont(None, 48)
       pop_up_surface = pop_up_font.render(pop_up_text, True, POWER_UP_TEXT_COL)
       screen.blit(pop_up_surface, (SCREEN_WIDTH/5, SCREEN_HEIGHT/4*3))
       is_pop_up_showing = run_pop_up_timer()

    player_hp_font = pygame.font.SysFont(None, 48)
    player_hp_surface = player_hp_font.render(player_health_text, True, POWER_UP_TEXT_COL)
    screen.blit(player_hp_surface, (5,5))

    if game_state == "game_over":
        game_over_font = pygame.font.SysFont(None, 48)
        game_over_surface = game_over_font.render(game_over_text, True, GAME_OVER_TEXT_COL)
        screen.blit(game_over_surface, (SCREEN_WIDTH/3, SCREEN_HEIGHT/3))

           

def show_pop_up_UI(text: str):
    global pop_up_text, is_pop_up_showing, start_time
    pop_up_text = text
    is_pop_up_showing = True
    start_time = pygame.time.get_ticks()


def run_pop_up_timer():
    elapsed = (pygame.time.get_ticks() - start_time) / 1000
    remaining = pop_up_time - elapsed

    if remaining <= 0:
        return False
    else:
        return True
      

def update_player_health_ui(health: int):
    global player_health_text 
    player_health_text = "Health: " + str(health)