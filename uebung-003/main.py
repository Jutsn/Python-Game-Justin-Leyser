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

import pygame
import os
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK
from player import Player
from level import Level, Obstacle
import UIManager
import ScoreManager
import ShopManager


def main():
    # ------------------------------------------------------------------ #
    #  Initialize pygame                                                 #
    # ------------------------------------------------------------------ #
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("RealFakeGame")
    clock = pygame.time.Clock()

    #Load Highscore
    ScoreManager.load_high_score()

    #define game states
    play_state = "playing"
    game_over_state = "game_over"
    shop_state = "shopping"
    game_state = play_state
    
    # ------------------------------------------------------------------ #
    #  Setup — create player and load level (ofApp::setup)   #
    # ------------------------------------------------------------------ #
    player: Player
    level: Level
    level_index = 1

    def start_run():
        nonlocal  player, level, level_index
        player = Player()
        player.setup(
                        x=SCREEN_WIDTH // 2,           # Center of screen
                        y=SCREEN_HEIGHT - 50,           # Near bottom of screen
                        dx=0,
                        dy=0,
                        image_prefix="player_stage",
                        anim_speed=1,
                        hp=2,
                        )
        player.set_might(rng=700, dmg=1, cad=55, shotspd=3)
        level_index = 1
        level = Level()
        level.load("lvl001.rfg")

    start_run()

    # Proceed with next level
    def start_next_level():
        nonlocal level, level_index
        level_index += 1
        path = os.path.join("lvl00" + str(level_index) + ".rfg")
        level = Level()
        level.load(path)
    

    #Input
    mouse_clicked = False

    

    # ------------------------------------------------------------------ #
    #  Game loop                                                         #
    # ------------------------------------------------------------------ #
    running = True
    while running:

        # -------------------------------------------------------------- #
        #  Event handling                                                 #
        # -------------------------------------------------------------- #
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

                    
                    
                    

        # -------------------------------------------------------------- #
        #  Update                                                        #
        # -------------------------------------------------------------- #
        if game_state == play_state:
            player.step()
            level.step()

            # Update obstacles
            for obs in level.obstacles:
                obs.step()

            # Update Enemies and score
            for enemy in level.enemies:
                enemy.step(pygame.Vector2(player.pos.x,player.pos.y))

                if (enemy.is_alive() == False):
                    ScoreManager.add_score(1)
                    

            # Remove dead enemies
            level.enemies = [e for e in level.enemies if e.is_alive()]

            # Finish level when all Enemies are dead
            if len(level.enemies) == 0:
                ScoreManager.try_update_highscore()
                game_state = shop_state

            # Check collisions (enemies vs shots vs obstacles vs player)
            for obs in level.obstacles:
                if (obs.collision_with_player(player.get_rect())):
                    level.obstacles.remove(obs)
                    player.power_up_might(obs.length)
                    UIManager.show_pop_up_UI("Temporary Stat Boost")
                for enemy in level.enemies:
                    if (obs.collision_with_enemy(enemy.get_rect())):
                        level.enemies.remove(enemy)
                        #level.obstacles.remove(obs)

            for enemy in level.enemies:
                if enemy.collision_with_player(player.get_rect()):
                    level.enemies.remove(enemy)
                    player.get_damage(enemy.damage)
                    UIManager.update_player_health_ui(player.hp)
                for shot in player.shots:
                    if enemy.collision_with_shot(shot.get_rect()):
                        enemy.get_damage(1)
                        shot.life = 0
            
            # Check player.hp <= 0 for death / game_state_transition
            if player.hp <= 0:
                ScoreManager.try_update_highscore()
                game_state = game_over_state


        if game_state == game_over_state:
            if mouse_clicked:
                start_run()
                game_state = play_state


        if game_state == shop_state:
            ShopManager.set_shop_offer(player)

            if mouse_clicked:
                mouse_pos = pygame.mouse.get_pos()
                ShopManager.check_for_interaction(mouse_pos)
            
            upgrade_bought = ShopManager.check_if_upgrade_is_bought()

            if upgrade_bought == True:
                ShopManager.reset_shop()
                start_next_level()
                game_state = play_state

                       
        # -------------------------------------------------------------- #
        #  Draw                                                          #
        # -------------------------------------------------------------- #
        screen.fill(BLACK)

        # Draw level background first
        level.draw(screen)

        # TODO: Draw enemies
        for enemy in level.enemies:
            enemy.draw(screen)
        # TODO: Draw obstacles
        for obs in level.obstacles:
            obs.draw(screen)

        # Draw player (also draws its shots internally)
        player.draw(screen)

        # TODO: Draw UI
        UIManager.draw_UI(screen, game_state)

        
        pygame.display.flip()
        clock.tick(FPS)

    # ------------------------------------------------------------------ #
    #  Cleanup                                                           #
    # ------------------------------------------------------------------ #
    pygame.quit()




if __name__ == "__main__":
    main()
