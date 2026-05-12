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
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK
from player import Player
from level import Level, Obstacle
import UIManager


def main():
    # ------------------------------------------------------------------ #
    #  Initialize pygame                                                 #
    # ------------------------------------------------------------------ #
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("RealFakeGame")
    clock = pygame.time.Clock()

    # ------------------------------------------------------------------ #
    #  Setup — create player and load level (ofApp::setup)   #
    # ------------------------------------------------------------------ #
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

    level = Level()
    level.load("lvl001.rfg")

   
    play_state = "playing"  # TODO: Add "title" and "gameover" states
    game_over_state = "game_over"
    game_state = play_state

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
                if game_state == game_over_state:
                    if event.key == pygame.K_SPACE:
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

                        level = Level()
                        level.load("lvl001.rfg")
                        game_state = play_state

        # -------------------------------------------------------------- #
        #  Update                                                        #
        # -------------------------------------------------------------- #
        if game_state == play_state:
            player.step()
            level.step()

            for obs in level.obstacles:
                obs.step()

            for enemy in level.enemies:
                enemy.step(pygame.Vector2(player.pos.x,player.pos.y))
            # Remove dead enemies
            level.enemies = [e for e in level.enemies if e.is_alive()]

            # TODO: Check collisions (shots vs enemies, enemies vs player)
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
            

            # TODO: Check player.hp <= 0 for death / game_state transition
            if player.hp <= 0:
                game_state = game_over_state

        
           
           
                

                        
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
        UIManager.draw_UI(screen, SCREEN_WIDTH, SCREEN_HEIGHT, game_state)

        


        pygame.display.flip()
        clock.tick(FPS)

    # ------------------------------------------------------------------ #
    #  Cleanup                                                           #
    # ------------------------------------------------------------------ #
    pygame.quit()


if __name__ == "__main__":
    main()
