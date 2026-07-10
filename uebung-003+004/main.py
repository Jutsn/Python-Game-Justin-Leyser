# main.py
# Game loop for RealFakeGame.
#
# Controls:
#   Mouse X  — move player left/right
#   ESC      — quit
#
# This skeleton provides:
#   - Player that follows mouse and auto-fires shots
#   - Level with background image
#   - Parsed (but inactive) enemies and obstacles

from threading import local
import pygame
import os
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK, ASSET_DIR
from player import Player
from level import Level, Obstacle
import collision_manager
import ui_manager
import score_manager
import shop_manager
import money_manager



def main():
    # ------------------------------------------------------------------ #
    #  Initialize pygame                                                 #
    # ------------------------------------------------------------------ #
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("RealFakeGame")
    clock = pygame.time.Clock()

    #Load Highscore
    score_manager.load_high_score()


    #Define game states
    play_state = "playing"
    game_over_state = "game_over"
    win_state = "win_state"
    shop_state = "shopping"
    game_state = play_state
    
    # ------------------------------------------------------------------ #
    #  Setup — create player, load level, set background music                                   #
    # ------------------------------------------------------------------ #
    player: Player
    level: Level
    level_index: int
    def start_new_game():
        nonlocal  player, level, level_index

        player = create_player()

        level_index = 1
        level = load_level(level_index)

        reset_ui()
        load_background_music_of_level()

    def create_player() -> Player:
        player = Player()
        player.setup(
                        x=SCREEN_WIDTH // 2,           # Center of screen
                        y=SCREEN_HEIGHT - 50,           # Near bottom of screen
                        dx=0,
                        dy=0,
                        image_prefix="player",
                        anim_speed=1,
                        hp=3,
                        )
        
        player.set_might(rng=200, dmg=1, cad=55, shotspd=2)
        return player
    def reset_ui():
        ui_manager.update_player_health_ui(player.hp)
        score_manager.reset_score()
        money_manager.reset_money()
    def load_background_music_of_level():
        m_path = os.path.join(ASSET_DIR, level.music_name)
        try:
            background_music = pygame.mixer.music.load(m_path)
            # Lautstärke auf 50% setzen
            pygame.mixer.music.set_volume(0.5)
            # Musik abspielen
            pygame.mixer.music.play(-1)
        except pygame.error:
                print(f"Warning: could not load music {m_path}")
    # ------------------------------------------------------------------ #
    # Level Progression
    # ------------------------------------------------------------------ #
    # Loads specific level by Index
    def load_level(level_index: int) -> Level:
        level = Level()
        path = os.path.join("lvl00" + str(level_index) + ".rfg")
        level.load(path)
        return level
    # Check If Next Level-File exists
    def check_for_next_level() -> bool:
        next_level = level_index + 1
        path = os.path.join(ASSET_DIR, "lvl00" + str(next_level) + ".rfg")
        return os.path.exists(path)
    # Proceed with next level
    def start_next_level():
        nonlocal level, level_index
        level_index += 1
        level = load_level(level_index)
        load_background_music_of_level()

    
    # ------------------------------------------------------------------ #
    #  Input                                                             #
    # ------------------------------------------------------------------ #
    def handle_input():
        running = True
        mouse_clicked = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_clicked = True    
            else: mouse_clicked = False

        return running, mouse_clicked
    # ------------------------------------------------------------------ #
    #  Update                                                            #
    # ------------------------------------------------------------------ #
    def update():
        nonlocal game_state, play_state, win_state, shop_state, game_over_state
        if game_state == play_state:
           ui_manager.clear_boss_health_bars() 
           player.step()
           level.step()

           # Update obstacles
           for obs in level.obstacles:
               obs.step()

           # Update Enemies and score
           for enemy in level.enemies:
               enemy.step(pygame.Vector2(player.pos.x,player.pos.y))

               if (enemy.is_alive() == False):
                   score_manager.add_score(1)
                   money_manager.add_money(1)
               
           # Remove dead enemies
           level.enemies = [e for e in level.enemies if e.is_alive()]

           # Finish level when all Enemies are dead
           if len(level.enemies) == 0:
               score_manager.try_update_highscore()
               if check_for_next_level() == True:
                   game_state = shop_state
               elif check_for_next_level() == False:
                   game_state = win_state

           # Check collisions (enemies vs shots vs obstacles vs player)
           collision_manager.check_for_collisions(level, player)
           
           # Check player.hp <= 0 for death / game_state_transition
           if player.hp <= 0:
               score_manager.try_update_highscore()
               game_state = game_over_state

        # Game Over
        if game_state == game_over_state:
            # Restart Game
            if mouse_clicked:
                start_new_game()
                game_state = play_state
        
        # Game Won
        if game_state == win_state:
            # Restart Game
            if mouse_clicked:
                start_new_game()
                game_state = play_state
        
        # Shop State
        if game_state == shop_state:
            shop_manager.set_shop_offer(player)

            if mouse_clicked:
                mouse_pos = pygame.mouse.get_pos()
                shop_manager.check_for_interaction(mouse_pos)
            
            upgrade_bought = shop_manager.check_if_upgrade_is_bought()

            if upgrade_bought == True:
                shop_manager.reset_shop()
                start_next_level()
                game_state = play_state
    # ------------------------------------------------------------------ #
    #  Render                                                           #
    # ------------------------------------------------------------------ #
    def render():
         screen.fill(BLACK)

         # Draw level background first
         level.draw(screen)

         # TODO: Draw enemies
         for enemy in level.enemies:
             enemy.draw(screen)
             if enemy.max_hp > 1:
                ui_manager.register_boss_health_bar(enemy)

         # TODO: Draw obstacles
         for obs in level.obstacles:
             obs.draw(screen)

         # Draw player (also draws its shots internally)
         player.draw(screen)

         # TODO: Draw UI
         ui_manager.draw_UI(screen, game_state)
         
         pygame.display.flip()
         clock.tick(FPS)

    # ------------------------------------------------------------------ #
    #  Game loop                                                         #
    # ------------------------------------------------------------------ #
    start_new_game()
    running = True
    while running:
        running, mouse_clicked = handle_input()
        update()
        render()

    pygame.quit()





if __name__ == "__main__":
    main()
