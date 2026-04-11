import pygame
from Projectiles import ProjectileManager
from Player import PlayerController
from Enemy import Enemy
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
player = PlayerController()
enemy = Enemy()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    enemy.update()
    ProjectileManager.update_bullets()
    screen.fill((11, 13, 16))
    player.draw(screen)
    enemy.draw(screen)
    ProjectileManager.draw_bullets(screen)
    
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


    