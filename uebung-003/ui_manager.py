import os
from enemy import Enemy
import entity
import pygame
from settings import BLACK, RED, WHITE, GOLD, SMALL_FONT, MEDIUM_FONT, BIG_MEDIUM_FONT, BIG_FONT, SCREEN_WIDTH, SCREEN_HEIGHT, ASSET_DIR

# Parameter Declaration
# region Parameter Declaration
# region Game_UI
# Font
POP_UP_FONT = MEDIUM_FONT
PLAYER_HP_FONT = MEDIUM_FONT
GAME_OVER_FONT = BIG_FONT
YOU_WON_FONT = BIG_FONT
SCORE_FONT = MEDIUM_FONT
MONEY_FONT = MEDIUM_FONT
YOURSCORE_NAMETAG_FONT = MEDIUM_FONT
HIGHSCORE_FONT = BIG_MEDIUM_FONT
SHOP_FONT = SMALL_FONT
RESTART_FONT = SMALL_FONT

# Text Color
POWER_UP_TEXT_COL = RED
HEALTH_TEXT_COL = BLACK
GAME_OVER_TEXT_COL = BLACK
YOU_WON_TEXT_COL = GOLD
SCORE_TEXT_COL = BLACK
MONEY_TEXT_COL = BLACK
SHOP_TEXT_COL = WHITE

# UI_content
pop_up_text = "Stats"
player_health_name_tag_text = "HP"
player_health_text = str(2)
game_over_text = "Game Over"
you_won_text = "You Won!"
score_name_tag_text = "Score"
score_text = str(0)
high_score_name_tag_text = "Highscore"
high_score_text = str(0)
money_name_tag_text = "$"
money_text = str(0)
restart_text = "Click to Restart"

# pop_up_timer
is_pop_up_showing = False
start_time = 0
pop_up_time = 3

# Boss_healthbars
boss_health_bars = []

BOSS_BAR_WIDTH = 60
BOSS_BAR_HEIGHT = 6
BOSS_BAR_OFFSET_Y = 25
#endregion Game_UI
#region Shop_UI
card_1_text = "Item 1"
card_2_text = "Item 2"
card_3_text = "Item 3"
card_1_value = "+1"
card_2_value = "+10%"
card_3_value = "+1"
costs_1_text = "Costs 1"
costs_2_text = "Costs 2"
costs_3_text = "Costs 3"

item_card_image = pygame.image.load(os.path.join(ASSET_DIR, "card1.png"))

# Card 1 Rect
card_1_pos_x = SCREEN_WIDTH/2 - item_card_image.width/2
card_1_pos_y = SCREEN_HEIGHT/2 - item_card_image.height
card_1_rect = pygame.Rect(card_1_pos_x, card_1_pos_y, item_card_image.width, item_card_image.height)
# Card 2 Rect
card_2_pos_x = SCREEN_WIDTH * 0.20 - item_card_image.width/2
card_2_pos_y = SCREEN_HEIGHT/2 - item_card_image.height
card_2_rect = pygame.Rect(card_2_pos_x, card_2_pos_y, item_card_image.width, item_card_image.height)
# Card 3 Rect
card_3_pos_x = SCREEN_WIDTH * 0.80 - item_card_image.width/2
card_3_pos_y = SCREEN_HEIGHT/2 - item_card_image.height
card_3_rect = pygame.Rect(card_3_pos_x, card_3_pos_y, item_card_image.width, item_card_image.height)

card_rects = [card_1_rect, card_2_rect, card_3_rect]
#endregion Shop_UI
# endregion Parameter Declaration

# Draw - Main function
#region
def draw_UI(screen, game_state: str):

    draw_player_health(screen)

    draw_money(screen)
    draw_score(screen)

    draw_boss_health_bars(screen)

    if (is_pop_up_showing == True):
       draw_pop_up_text(screen)

    if game_state == "game_over":
        draw_game_over_window(screen)

    if game_state == "win_state":
        draw_win_screen(screen)

    if game_state == "shopping":
        draw_shop_window(screen)
#endregion

# Draw - Helper functions
# region                       
def draw_player_health(screen):
    
    player_hp_tag_surface = PLAYER_HP_FONT.render(player_health_name_tag_text, True, HEALTH_TEXT_COL)
    player_hp_surface = PLAYER_HP_FONT.render(player_health_text, True, HEALTH_TEXT_COL)

    screen.blit(player_hp_tag_surface, (5,5))
    ancor_point_x = 5 + player_hp_tag_surface.width/2
    screen.blit(player_hp_surface, (ancor_point_x - player_hp_surface.width/2, 5 + player_hp_tag_surface.height))
def draw_score(screen):
    score_tag_surface = SCORE_FONT.render(score_name_tag_text, True, SCORE_TEXT_COL)
    score_surface = SCORE_FONT.render(score_text, True, SCORE_TEXT_COL)
    screen.blit(score_tag_surface, (SCREEN_WIDTH - score_tag_surface.width - 5, 5))
    screen.blit(score_surface, (SCREEN_WIDTH - score_tag_surface.width/2 - score_surface.width/2 - 5, score_tag_surface.height + 5))
def draw_money(screen):
    money_tag_surface = MONEY_FONT.render(money_name_tag_text, True, MONEY_TEXT_COL)
    money_surface = MONEY_FONT.render(money_text, True, SCORE_TEXT_COL)
    screen.blit(money_tag_surface, (24 - money_tag_surface.width/2, 65 + 10))
    screen.blit(money_surface, (24 - money_surface.width/2, 75 + money_tag_surface.height + 5))
def draw_pop_up_text(screen):
    global is_pop_up_showing
    pop_up_surface = POP_UP_FONT.render(pop_up_text, True, POWER_UP_TEXT_COL)
    screen.blit(pop_up_surface, (SCREEN_WIDTH/5, SCREEN_HEIGHT/4*3))
    is_pop_up_showing = run_pop_up_timer()
def draw_game_over_window(screen):
    # Draw Game Over text
    game_over_surface = GAME_OVER_FONT.render(game_over_text, True, GAME_OVER_TEXT_COL)
    game_over_pos_x = SCREEN_WIDTH/2 - game_over_surface.width/2
    game_over_pos_y = SCREEN_HEIGHT/3
    screen.blit(game_over_surface, (game_over_pos_x, game_over_pos_y))

    # Draw HighScore name tag
    high_score_tag_surface = HIGHSCORE_FONT.render(high_score_name_tag_text, True, SCORE_TEXT_COL)
    tag_pos_x = SCREEN_WIDTH/2 - high_score_tag_surface.width/2
    tag_pos_y = game_over_pos_y + game_over_surface.height + 5
    screen.blit(high_score_tag_surface, (tag_pos_x, tag_pos_y))

    # Draw HighScore number
    high_score_surface = HIGHSCORE_FONT.render(high_score_text, True, SCORE_TEXT_COL)
    score_pos_x = SCREEN_WIDTH/2 - high_score_surface.width/2
    score_pos_y = tag_pos_y + high_score_tag_surface.height + 5
    screen.blit(high_score_surface, (score_pos_x, score_pos_y))   

    # Draw "Your Score" name tag
    score_tag_surface = YOURSCORE_NAMETAG_FONT.render("Your Score", True, SCORE_TEXT_COL)
    tag_pos_x = SCREEN_WIDTH/2 - score_tag_surface.width/2
    tag_pos_y = score_pos_y + score_tag_surface.height + 5
    screen.blit(score_tag_surface, (tag_pos_x, tag_pos_y))
    
    # Draw Score number
    score_surface = YOURSCORE_NAMETAG_FONT.render(score_text, True, SCORE_TEXT_COL)
    score_pos_x = SCREEN_WIDTH/2 - score_surface.width/2
    score_pos_y = tag_pos_y + score_tag_surface.height + 5
    screen.blit(score_surface, (score_pos_x, score_pos_y))

    # Draw Restart text
    restart_surface = RESTART_FONT.render("Click to Restart",True,GAME_OVER_TEXT_COL)
    restart_pos_x = SCREEN_WIDTH / 2 - restart_surface.width / 2
    restart_pos_y = SCREEN_HEIGHT - restart_surface.height - 50
    screen.blit(restart_surface, (restart_pos_x, restart_pos_y))
def draw_shop_window(screen):
    # =====================================================
    # CARD 1
    # =====================================================
    screen.blit(item_card_image, card_1_rect)

    # Value Text
    value_1_surface = SHOP_FONT.render(str(card_1_value), True, SHOP_TEXT_COL)
    value_1_pos_x = card_1_pos_x + item_card_image.width / 2 - value_1_surface.width / 2
    value_1_pos_y = card_1_pos_y + item_card_image.height / 2 - 30
    screen.blit(value_1_surface, (value_1_pos_x, value_1_pos_y))

    # Item Text
    item_1_surface = SHOP_FONT.render(card_1_text, True, SHOP_TEXT_COL)
    text_1_pos_x = card_1_pos_x + item_card_image.width / 2 - item_1_surface.width / 2
    text_1_pos_y = card_1_pos_y + item_card_image.height / 2
    screen.blit(item_1_surface, (text_1_pos_x, text_1_pos_y))

    # Cost Text
    cost_1_surface = SHOP_FONT.render("Costs: " + str(costs_1_text), True, SHOP_TEXT_COL)
    cost_1_pos_x = card_1_pos_x + item_card_image.width / 2 - cost_1_surface.width / 2
    cost_1_pos_y = card_1_pos_y + item_card_image.height + 10
    screen.blit(cost_1_surface, (cost_1_pos_x, cost_1_pos_y))


    # =====================================================
    # CARD 2
    # =====================================================
    screen.blit(item_card_image, card_2_rect)

    # Value Text
    value_2_surface = SHOP_FONT.render(str(card_2_value), True, SHOP_TEXT_COL)
    value_2_pos_x = card_2_pos_x + item_card_image.width / 2 - value_2_surface.width / 2
    value_2_pos_y = card_2_pos_y + item_card_image.height / 2 - 30
    screen.blit(value_2_surface, (value_2_pos_x, value_2_pos_y))

    # Item Text
    item_2_surface = SHOP_FONT.render(card_2_text, True, SHOP_TEXT_COL)
    text_2_pos_x = card_2_pos_x + item_card_image.width / 2 - item_2_surface.width / 2
    text_2_pos_y = card_2_pos_y + item_card_image.height / 2
    screen.blit(item_2_surface, (text_2_pos_x, text_2_pos_y))

    # Cost Text
    cost_2_surface = SHOP_FONT.render("Costs: " + str(costs_2_text), True, SHOP_TEXT_COL)
    cost_2_pos_x = card_2_pos_x + item_card_image.width / 2 - cost_2_surface.width / 2
    cost_2_pos_y = card_2_pos_y + item_card_image.height + 10
    screen.blit(cost_2_surface, (cost_2_pos_x, cost_2_pos_y))


    # =====================================================
    # CARD 3
    # =====================================================
    screen.blit(item_card_image, card_3_rect)

    # Value Text
    value_3_surface = SHOP_FONT.render(str(card_3_value), True, SHOP_TEXT_COL)
    value_3_pos_x = card_3_pos_x + item_card_image.width / 2 - value_3_surface.width / 2
    value_3_pos_y = card_3_pos_y + item_card_image.height / 2 - 30
    screen.blit(value_3_surface, (value_3_pos_x, value_3_pos_y))

    # Item Text
    item_3_surface = SHOP_FONT.render(card_3_text, True, SHOP_TEXT_COL)
    text_3_pos_x = card_3_pos_x + item_card_image.width / 2 - item_3_surface.width / 2
    text_3_pos_y = card_3_pos_y + item_card_image.height / 2
    screen.blit(item_3_surface, (text_3_pos_x, text_3_pos_y))

    # Cost Text
    cost_3_surface = SHOP_FONT.render("Costs: " + str(costs_3_text), True, SHOP_TEXT_COL)
    cost_3_pos_x = card_3_pos_x + item_card_image.width / 2 - cost_3_surface.width / 2
    cost_3_pos_y = card_3_pos_y + item_card_image.height + 10
    screen.blit(cost_3_surface, (cost_3_pos_x, cost_3_pos_y))
def draw_win_screen(screen):
    # Draw Game Over text
    you_won_surface = YOU_WON_FONT.render(you_won_text, True, YOU_WON_TEXT_COL)
    game_over_pos_x = SCREEN_WIDTH/2 - you_won_surface.width/2
    game_over_pos_y = SCREEN_HEIGHT/3
    screen.blit(you_won_surface, (game_over_pos_x, game_over_pos_y))

    # Draw HighScore name tag
    high_score_tag_surface = HIGHSCORE_FONT.render(high_score_name_tag_text, True, SCORE_TEXT_COL)
    tag_pos_x = SCREEN_WIDTH/2 - high_score_tag_surface.width/2
    tag_pos_y = game_over_pos_y + you_won_surface.height + 5
    screen.blit(high_score_tag_surface, (tag_pos_x, tag_pos_y))

    # Draw HighScore number
    high_score_surface = HIGHSCORE_FONT.render(high_score_text, True, SCORE_TEXT_COL)
    score_pos_x = SCREEN_WIDTH/2 - high_score_surface.width/2
    score_pos_y = tag_pos_y + high_score_tag_surface.height + 5
    screen.blit(high_score_surface, (score_pos_x, score_pos_y))   

    # Draw "Your Score" name tag
    score_tag_surface = YOURSCORE_NAMETAG_FONT.render("Your Score", True, SCORE_TEXT_COL)
    tag_pos_x = SCREEN_WIDTH/2 - score_tag_surface.width/2
    tag_pos_y = score_pos_y + score_tag_surface.height + 5
    screen.blit(score_tag_surface, (tag_pos_x, tag_pos_y))
    
    # Draw Score number
    score_surface = YOURSCORE_NAMETAG_FONT.render(score_text, True, SCORE_TEXT_COL)
    score_pos_x = SCREEN_WIDTH/2 - score_surface.width/2
    score_pos_y = tag_pos_y + score_surface.height + 5
    screen.blit(score_surface, (score_pos_x, score_pos_y))

    # Draw Restart text
    restart_surface = RESTART_FONT.render(restart_text,True,YOU_WON_TEXT_COL)
    restart_pos_x = SCREEN_WIDTH / 2 - restart_surface.width / 2
    restart_pos_y = SCREEN_HEIGHT - restart_surface.height - 50
    screen.blit(restart_surface, (restart_pos_x, restart_pos_y))
def draw_boss_health_bars(screen):

    for boss in boss_health_bars:

        percentage = boss.hp / boss.max_hp
        percentage = max(0.0, min(1.0, percentage))

        x = boss.pos.x - BOSS_BAR_WIDTH / 2
        y = boss.pos.y - BOSS_BAR_OFFSET_Y

        pygame.draw.rect(
            screen,
            BLACK,
            (x, y, BOSS_BAR_WIDTH, BOSS_BAR_HEIGHT)
        )

        pygame.draw.rect(
            screen,
            RED,
            (
                x,
                y,
                BOSS_BAR_WIDTH * percentage,
                BOSS_BAR_HEIGHT
            )
        )

        pygame.draw.rect(
            screen,
            WHITE,
            (x, y, BOSS_BAR_WIDTH, BOSS_BAR_HEIGHT),
            1
        )
# endregion

# Update UI Content - public functions
#region
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
    player_health_text = str(health)
def update_money_ui(money: int):
    global money_text 
    money_text = str(money)
def update_score_ui(score: int):
    global score_text 
    score_text = str(score)
def update_high_score_ui(high_score: int):
    global high_score_text 
    high_score_text = str(high_score)
def update_item_cards_ui(upgrade_1: dict, upgrade_2: dict, upgrade_3: dict):
    global card_1_text,card_2_text,card_3_text,card_1_value,card_2_value,card_3_value,costs_1_text,costs_2_text,costs_3_text
    card_1_text = upgrade_1["text"]             
    card_2_text = upgrade_2["text"]             
    card_3_text = upgrade_3["text"] 
    card_1_value = upgrade_1["value_text"]
    card_2_value = upgrade_2["value_text"]
    card_3_value = upgrade_3["value_text"]
    costs_1_text = upgrade_1["cost"]
    costs_2_text = upgrade_2["cost"]
    costs_3_text = upgrade_3["cost"]
def clear_boss_health_bars():
    global boss_health_bars
    boss_health_bars.clear()
def register_boss_health_bar(boss: Enemy):
    boss_health_bars.append(boss)
#endregion