import pygame
from Projectiles import ProjectileManager
from Player import PlayerController
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
player = PlayerController();
enemyX, enemyY = 400, 300

running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
         
    #if keys[pygame.K_LEFT]:  enemyX -= 5
    #if keys[pygame.K_RIGHT]: enemyX += 5
    #if keys[pygame.K_UP]:    enemyY -= 5
    #if keys[pygame.K_DOWN]:  enemyY += 5


    player.update()
    ProjectileManager.update_bullets()
    screen.fill((11, 13, 16))
    player.draw(screen)
    ProjectileManager.draw_bullets(screen)
    
    #pygame.draw.rect(screen, (255, 107, 53), (enemyX, enemyY, 40, 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


    