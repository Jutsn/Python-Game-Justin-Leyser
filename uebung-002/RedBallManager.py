import pygame
from RedBall import RedBall
import random



balls = []

def register_red_ball():
	ball_pos = pygame.Vector2(random.randrange(5,595), 70)
	balls.append(RedBall(ball_pos))

def update_red_balls():
	for ball in balls:
		ball.update()
		if not ball.alive:
			balls.remove(ball)
			register_red_ball()


def draw_red_balls(screen):
	for ball in balls:
		ball.draw(screen)

