import pygame

class Enemy():
	def __init__(self):
		self.position = pygame.Vector2(400, 300)
		self.last_shot_time = 0
		self.cooldown = 300
	
	def update(self):
		self.input()

	def draw(self, screen):
		pygame.draw.rect(screen, (255, 107, 53), (self.position.x, self.position.y , 40, 40))

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT]: self.move_left()
		if keys[pygame.K_RIGHT]: self.move_right()
		if keys[pygame.K_UP]: self.move_up()
		if keys[pygame.K_DOWN]: self.move_down()


	def move_left(self):
		self.position.x -= 5
	def move_right(self):
		self.position.x += 5
	def move_up(self):
		self.position.y -= 5
	def move_down(self):
		self.position.y += 5