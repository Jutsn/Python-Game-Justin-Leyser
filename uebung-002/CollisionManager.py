import pygame
import RedBallManager

# Falling Red Ball: Collisions-Check
def handle_red_ball_collisions(list1):
	for obs in list1:
		for ball in RedBallManager.balls:
			if obs.colliderect(ball.rect):
				ball.die()
				break
