from ast import Dict
import os
import pygame
from settings import BLACK, RED, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, ASSET_DIR

pygame.font.init()
pop_up_font = pygame.font.SysFont(None, 40)
player_hp_font = pygame.font.SysFont(None, 40)
game_over_font = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 40)
your_score_name_tag_font = pygame.font.SysFont(None, 40)
highscore_font = pygame.font.SysFont(None, 42)
shop_font = pygame.font.SysFont(None, 30)


POWER_UP_TEXT_COL = RED
HEALTH_TEXT_COL = BLACK
GAME_OVER_TEXT_COL = BLACK
SCORE_TEXT_COL = BLACK
SHOP_TEXT_COL = WHITE

pop_up_text = "Stats"
player_health_name_tag_text = "Health"
player_health_text = str(2)
game_over_text = "Game Over"
score_name_tag_text = "Score"
score_text = str(0)
high_score_name_tag_text = "Highscore"
high_score_text = str(0)

is_pop_up_showing = False
start_time = 0
pop_up_time = 3

# Upgrade Cards
card_1_text = "Item 1"
card_2_text = "Item 2"
card_3_text = "Item 3"
costs_1_text = "Costs 1"
costs_2_text = "Costs 2"
costs_3_text = "Costs 3"

item_card_image = pygame.image.load(os.path.join(ASSET_DIR, "card2.png"))

# Card 1 Rect
card_1_pos_x = SCREEN_WIDTH/2 - item_card_image.width/2
card_1_pos_y = SCREEN_HEIGHT/2 - item_card_image.height
card_1_rect = pygame.Rect(card_1_pos_x, card_1_pos_y, item_card_image.width, item_card_image.height)
# Card 2 Rect
card_2_pos_x = SCREEN_WIDTH/4 - item_card_image.width/2
card_2_pos_y = SCREEN_HEIGHT/2 - item_card_image.height
card_2_rect = pygame.Rect(card_2_pos_x, card_2_pos_y, item_card_image.width, item_card_image.height)
# Card 3 Rect
card_3_pos_x = SCREEN_WIDTH * 0.75 - item_card_image.width/2
card_3_pos_y = SCREEN_HEIGHT/2 - item_card_image.height
card_3_rect = pygame.Rect(card_3_pos_x, card_3_pos_y, item_card_image.width, item_card_image.height)

card_rects = [card_1_rect, card_2_rect, card_3_rect]


def draw_UI(screen, game_state):

    draw_player_health(screen)

    draw_score(screen)

    if (is_pop_up_showing == True):
       draw_pop_up_text(screen)

    if game_state == "game_over":
        draw_game_over_window(screen)

    if game_state == "shopping":
        draw_shop_window(screen)



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
      
# Update UI Content
def update_player_health_ui(health: int):
    global player_health_text 
    player_health_text = str(health)

def update_score_ui(score: int):
    global score_text 
    score_text = str(score)

def update_high_score_ui(high_score: int):
    global high_score_text 
    high_score_text = str(high_score)

def update_item_cards_ui(text_1, text_2, text_3):
    global card_1_text,card_2_text,card_3_text
    card_1_text = text_1
    card_2_text = text_2
    card_3_text = text_3

# Draw - Helper functions
def draw_player_health(screen):
    player_hp_tag_surface = player_hp_font.render(player_health_name_tag_text, True, HEALTH_TEXT_COL)
    player_hp_surface = player_hp_font.render(player_health_text, True, HEALTH_TEXT_COL)
    screen.blit(player_hp_tag_surface, (5,5))
    screen.blit(player_hp_surface, (player_hp_tag_surface.width/2 - player_hp_surface.width/2 + 5, player_hp_tag_surface.height + 5))

def draw_score(screen):
    score_tag_surface = score_font.render(score_name_tag_text, True, SCORE_TEXT_COL)
    score_surface = score_font.render(score_text, True, SCORE_TEXT_COL)
    screen.blit(score_tag_surface, (SCREEN_WIDTH - score_tag_surface.width - 5, 5))
    screen.blit(score_surface, (SCREEN_WIDTH - score_tag_surface.width/2 - score_surface.width/2 - 5, score_tag_surface.height + 5))

def draw_pop_up_text(screen):
    global is_pop_up_showing
    pop_up_surface = pop_up_font.render(pop_up_text, True, POWER_UP_TEXT_COL)
    screen.blit(pop_up_surface, (SCREEN_WIDTH/5, SCREEN_HEIGHT/4*3))
    is_pop_up_showing = run_pop_up_timer()

def draw_game_over_window(screen):
    # Draw Game Over text
    game_over_surface = game_over_font.render(game_over_text, True, GAME_OVER_TEXT_COL)
    game_over_pos_x = SCREEN_WIDTH/2 - game_over_surface.width/2
    game_over_pos_y = SCREEN_HEIGHT/3
    screen.blit(game_over_surface, (game_over_pos_x, game_over_pos_y))

    # Draw HighScore name tag
    high_score_tag_surface = highscore_font.render(high_score_name_tag_text, True, SCORE_TEXT_COL)
    tag_pos_x = SCREEN_WIDTH/2 - high_score_tag_surface.width/2
    tag_pos_y = game_over_pos_y + game_over_surface.height + 5
    screen.blit(high_score_tag_surface, (tag_pos_x, tag_pos_y))

    # Draw HighScore number
    high_score_surface = highscore_font.render(high_score_text, True, SCORE_TEXT_COL)
    score_pos_x = SCREEN_WIDTH/2 - high_score_surface.width/2
    score_pos_y = tag_pos_y + high_score_tag_surface.height + 5
    screen.blit(high_score_surface, (score_pos_x, score_pos_y))   

    # Draw "Your Score" name tag
    score_tag_surface = your_score_name_tag_font.render("Your Score", True, SCORE_TEXT_COL)
    tag_pos_x = SCREEN_WIDTH/2 - score_tag_surface.width/2
    tag_pos_y = score_pos_y + score_tag_surface.height + 5
    screen.blit(score_tag_surface, (tag_pos_x, tag_pos_y))
    
    # Draw Score number
    score_surface = your_score_name_tag_font.render(score_text, True, SCORE_TEXT_COL)
    score_pos_x = SCREEN_WIDTH/2 - score_surface.width/2
    score_pos_y = tag_pos_y + score_surface.height + 5
    screen.blit(score_surface, (score_pos_x, score_pos_y))


def draw_shop_window(screen):

    # Draw Card 1 (Middle)
    screen.blit(item_card_image, card_1_rect)

    # Draw Item 1 Text
    item_1_surface = shop_font.render(card_1_text, True, SHOP_TEXT_COL)
    text_1_pos_x = card_1_pos_x + item_card_image.width/2 - item_1_surface.width/2
    text_1_pos_y = card_1_pos_y + item_card_image.height/2 - item_1_surface.height/2
    screen.blit(item_1_surface, (text_1_pos_x, text_1_pos_y))

    # Draw Card 2 (Left)
    screen.blit(item_card_image, card_2_rect)

    # Draw Item 2 Text
    item_2_surface = shop_font.render(card_2_text, True, SHOP_TEXT_COL)
    text_2_pos_x = card_2_pos_x + item_card_image.width/2 - item_2_surface.width/2
    text_2_pos_y = card_2_pos_y + item_card_image.height/2 - item_2_surface.height/2
    screen.blit(item_2_surface, (text_2_pos_x, text_2_pos_y))

    # Draw Card 3 (Right)
    screen.blit(item_card_image, card_3_rect)

    # Draw Item 3 Text
    item_3_surface = shop_font.render(card_3_text, True, SHOP_TEXT_COL)
    text_3_pos_x = card_3_pos_x + item_card_image.width/2 - item_3_surface.width/2
    text_3_pos_y = card_3_pos_y + item_card_image.height/2 - item_3_surface.height/2
    screen.blit(item_3_surface, (text_3_pos_x, text_3_pos_y))
    

