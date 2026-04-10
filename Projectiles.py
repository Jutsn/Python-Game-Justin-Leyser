import pygame
bullets = []

class ProjectileManager():
	
	def register_player_bullet(player_position):
		bullets.append(Bullet(player_position))

	def update_bullets():
		for bullet in bullets:
			bullet.update()

	def draw_bullets(screen):
		for bullet in bullets:
			bullet.draw(screen)


class Bullet(): 
	def __init__(self, player_position):
		self.position = pygame.Vector2(player_position.x + 15, player_position.y)

	def update(self):
		self.position.y -= 3;

	def draw(self, screen):
		pygame.draw.rect(screen, (0, 255, 0), (self.position.x, self.position.y, 10, 10))