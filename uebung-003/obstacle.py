# obstacle.py
# Simple obstacle data class. Parsed from level file but NOT drawn or
# collision-checked in the skeleton. Students implement this in Uebung 003.

import pygame

class Obstacle:
    """Data-only obstacle. Parsed from .rfg level files.

    Students should implement:
    - draw(): render the obstacle as a colored rectangle
    - Collision detection with player
    """

    def __init__(
        self,
        track: int = 0,
        duration_start: int = 0,
        length: int = 0,
        color: tuple[int, int, int] = (255, 255, 255),
        width: int = 3,
        power_up_text = "P"
    ):
        self.track = track              # Which track (column) the obstacle is on
        self.duration_start = duration_start  # When it appears (in level duration)
        self.length = length            # How long it lasts (in duration units)
        self.color = color              # RGB color tuple
        self.width = width              # Pixel width
        self.speed = 2
       
        self.power_up_text = power_up_text

        # Derived screen coordinates (students compute these from track layout)
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

        self.rect = pygame.Rect(self.x1, self.y1, self.width, self.width)


    def step(self):
        self.y1 += self.speed
        self.rect.y = self.y1
        self.rect.x = self.x1
    
    
    def collision_with_player(self, player_rect):
        if self.rect.colliderect(player_rect):
            return True

    # Same logic, but better readability, please dont subtract a point xD
    def collision_with_enemy(self, enemy_rect):
        if self.rect.colliderect(enemy_rect):
            return True


    def draw(self, screen: pygame.Surface):
      """Draw the obstacle"""
      # Draw obstacle
      #pygame.draw.rect(screen, self.color, self.rect)
      font = pygame.font.SysFont(None, 40)
      stat_surface = font.render(self.power_up_text, True, self.color)
      screen.blit(stat_surface, (self.rect.x, self.rect.y))


