import pygame
from Projectiles import ProjectileManager
from Player import PlayerController
from Enemies import EnemyManager
import CollisionManager
import ScoreManager

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
player = PlayerController()
enemy_Man = EnemyManager
enemy_Man.register_enemy()
coll_Man = CollisionManager
proj_Man = ProjectileManager
scor_Man = ScoreManager


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   #game-logic
    player.update()
    enemy_Man.update_enemies()
    proj_Man.update_bullets()
    coll_Man.handle_collisions()

  #render
    screen.fill((11, 13, 16))
    player.draw(screen)
    enemy_Man.draw_enemies(screen)
    proj_Man.draw_bullets(screen)
    ScoreManager.drawScore(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


    