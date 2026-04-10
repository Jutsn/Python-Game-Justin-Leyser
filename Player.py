import pygame
from Projectiles import ProjectileManager

class PlayerController(): 
	def __init__(self):
		self.position = pygame.Vector2(400, 300)

	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]: self.position.x -= 5
		if keys[pygame.K_d]: self.position.x += 5
		if keys[pygame.K_w]: self.position.y -= 5
		if keys[pygame.K_s]: self.position.y += 5
		if self.position.y <= 300: 
			self.position.y = 300
		if self.position.y >= 550:
			self.position.y = 550

		if keys[pygame.K_SPACE]:
			ProjectileManager.register_player_bullet(self.position)

	def draw(self, screen):
		pygame.draw.rect(screen, (255, 107, 53), (self.position.x, self.position.y , 40, 40))


	
		