import pygame
pygame.font.init()

score = 0
font = pygame.font.SysFont("Times New Roman", 22)

def adjustScore():
    global score 
    score += 1

def drawScore(screen):
    text_surface = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text_surface, (50, 50))