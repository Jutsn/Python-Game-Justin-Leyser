import pygame
from Projectiles import Bullet 
enemies = []

class EnemyManager:

	def register_enemy():
		enemy_pos = pygame.Vector2(400, 70)
		enemies.append(Enemy(enemy_pos))
	def update_enemies():
		for enemy in enemies:
			enemy.update()
			if enemy.alive == False: 
				enemies.remove(enemy)
	def draw_enemies(screen):
		for enemy in enemies:
			enemy.draw(screen)

class Enemy():
#init,update,draw
	def __init__(self, enemy_pos):
		self.position = enemy_pos
		self.rect = pygame.Rect(self.position.x, self.position.y , 40, 40)
		self.alive = True
		#self.last_shot_time = 0
		#self.cooldown = 300
	
	def update(self):
		self.input()
		self.clamp_enemy_pos()
		self.rect.topleft = self.position

	def draw(self, screen):
		pygame.draw.rect(screen, (255, 107, 53), self.rect)
#input
	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT]: self.move_left()
		if keys[pygame.K_RIGHT]: self.move_right()
		if keys[pygame.K_UP]: self.move_up()
		if keys[pygame.K_DOWN]: self.move_down()
#move

	def move_left(self):
		self.position.x -= 5
	def move_right(self):
		self.position.x += 5
	def move_up(self):
		self.position.y -= 5
	def move_down(self):
		self.position.y += 5
#clamp position
	def clamp_enemy_pos(self):
		if self.position.y >= 250: 
			self.position.y = 250
		if self.position.y <= 10:
			self.position.y = 10
		if self.position.x <= 10: 
			self.position.x = 10
		if self.position.x >= 750: 
			self.position.x = 750
#die
	def die(self):
		self.alive = False
		EnemyManager.register_enemy()
	