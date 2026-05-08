import pygame

TEXT_COL = (255, 0, 0)
pop_up_text = "Stats"
show_pop_up_UI = False
start_time = 0
pop_up_time = 4

def draw_UI(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    global show_pop_up_UI
    if (show_pop_up_UI == True):
       font = pygame.font.SysFont(None, 48)
       stat_surface = font.render(pop_up_text, True, TEXT_COL)
       screen.blit(stat_surface, (SCREEN_WIDTH/5, SCREEN_HEIGHT/4*3))
       show_pop_up_UI = run_pop_up_timer()
           

def show_pop_up_UI(text: str):
    global pop_up_text, show_pop_up_UI
    pop_up_text = text
    show_pop_up_UI = True
    start_time = pygame.time.get_ticks()
    


def run_pop_up_timer():
    elapsed = (pygame.time.get_ticks() - start_time) / 1000
    remaining = pop_up_time - elapsed

    if remaining <= 0:
        return False
    else:
        return True
      

