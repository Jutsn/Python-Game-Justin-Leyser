import pygame
from Projectiles import ProjectileManager
from Player import PlayerController
from Enemies import Enemy
import CollisionSystem
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
player = PlayerController()
enemy = Enemy()
coll_Man = CollisionSystem
proj_Man = ProjectileManager

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   #game-logic
    player.update()
    enemy.update()
    proj_Man.update_bullets()
    coll_Man.handle_collisions(enemy)

  #render
    screen.fill((11, 13, 16))
    player.draw(screen)
    enemy.draw(screen)
    proj_Man.draw_bullets(screen)
   
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


    