import pygame

TEXT_COL = (255, 0, 0)
stats = "Stats"
showStatUI = False
timestamp = 0
power_up_ui_timer = 5

def draw_UI(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    global showStatUI
    if (showStatUI == True):
       font = pygame.font.SysFont(None, 48)
       stat_surface = font.render(stats, True, TEXT_COL)
       screen.blit(stat_surface, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
       if (pygame.time.get_ticks() >= timestamp):
           showStatUI = False
     

def show_Power_Up_UI():
    global stats, showStatUI, timestamp
    stats = "Temporary Stat Boost"
    showStatUI = True
    timestamp = pygame.time.get_ticks() + power_up_ui_timer*1000