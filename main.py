import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
x, y = 400, 300
a, b = 400, 300

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  x -= 5
    if keys[pygame.K_RIGHT]: x += 5
    if keys[pygame.K_UP]:    y -= 5
    if keys[pygame.K_DOWN]:  y += 5
    if keys[pygame.K_a]:  a -= 5
    if keys[pygame.K_d]: a += 5
    if keys[pygame.K_w]:    b -= 5
    if keys[pygame.K_s]:  b += 5

    screen.fill((11, 13, 16))
    pygame.draw.rect(screen, (255, 107, 53), (x, y, 40, 40))
    pygame.draw.rect(screen, (255, 107, 53), (a, b, 40, 40))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()