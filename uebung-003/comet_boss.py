import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from enemy import Enemy

class CometBoss(Enemy):
    def __init__(self,):
        super().__init__()
        self.moving_right = False


    def step(self, target_pos: pygame.Vector2):
        if self.is_alive():
            if self.pos.y <= 0:
                direction = pygame.Vector2(0,1)
            else:
                # Calculate direction toward target (not applied — stub)
                direction = target_pos - self.pos
                # TODO: Normalize direction, apply speed, move toward target
                direction = direction.normalize()

            self.pos += direction * self.speed

            # countdown for Red Flash when hit
            if self.flash_timer > 0:
                self.flash_timer -= 1


   