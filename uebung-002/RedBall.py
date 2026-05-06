import pygame



class RedBall:

	# ---- Farben (Rot, Grün, Blau, [Alpha]) ----
	BALL_COL = (255, 0, 0)

	# ---- Falling Red Balls  ----
	
	ball_sprite_radius = 10
	ball_col_width = ball_sprite_radius * 2
	ball_col_height = ball_sprite_radius * 2
	ball_movement_y = 0.0
	speed = 2

#init,update,draw
	def __init__(self, ball_pos):
		self.position = ball_pos
		self.ball_movement_y = 0.0
		self.rect = pygame.Rect(ball_pos.x, ball_pos.y,
                           self.ball_col_width,
                           self.ball_col_height)
		self.alive = True
	
	def update(self):
		# Falling Red Ball: Gravitation + Bewegung
		self.rect.y += self.speed


	def draw(self, screen):
		pygame.draw.circle(screen, self.BALL_COL, self.rect.center, self.ball_sprite_radius)

#die
	def die(self):
		self.alive = False
		
