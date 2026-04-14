import pygame
from Projectiles import ProjectileManager


class PlayerController():

	def __init__(self):
		self.position = pygame.Vector2(400, 300)
		self.last_shot_time = 0
		self.cooldown = 300
	
	def update(self):
		self.input()
		self.clamp_player_pos()

	def draw(self, screen):
		pygame.draw.rect(screen, (255, 107, 53), (self.position.x, self.position.y , 40, 40))

#input
	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]: self.move_left()
		if keys[pygame.K_d]: self.move_right()
		if keys[pygame.K_w]: self.move_up()
		if keys[pygame.K_s]: self.move_down()
		if keys[pygame.K_SPACE]: self.check_shot_cooldown()
#clamp position
	def clamp_player_pos(self):
		if self.position.y <= 300: 
			self.position.y = 300
		if self.position.y >= 550:
			self.position.y = 550
		if self.position.x <= 10: 
			self.position.x = 10
		if self.position.x >= 750: 
			self.position.x = 750
#move
	def move_left(self):
		self.position.x -= 5
	def move_right(self):
		self.position.x += 5
	def move_up(self):
		self.position.y -= 5
	def move_down(self):
		self.position.y += 5
#shooting
	def check_shot_cooldown(self):
		current_time = pygame.time.get_ticks()
		if current_time - self.last_shot_time >= self.cooldown:
			self.shoot_bullet()
			self.last_shot_time = current_time

	def shoot_bullet(self):
		ProjectileManager.register_player_bullet(self.position)
		