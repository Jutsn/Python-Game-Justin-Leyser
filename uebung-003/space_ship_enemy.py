import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from enemy import Enemy
from shot import Shot

class SpaceShip(Enemy):
    def __init__(self,):
        super().__init__()
        self.moving_right = False

        self.shots: list[Shot] = []   # Active shots
        self.rng = 700      # Shot range in frames
        self.dmg = 1        # Damage per shot
        self.cad = 100       # Cadence: frames between shots
        self.shotspd = 2    # Shot speed (pixels per frame, upward)
        self._cad_counter = 0   # Countdown to next shot
    
  

    def step(self, target_pos: pygame.Vector2):
        if self.is_alive():
            
            if self.pos.y <= 100:
                direction = pygame.Vector2(0,1)
                
            else:
                # Calculate direction toward target (not applied — stub)
                shot_direction = target_pos - self.pos
                # TODO: Normalize direction, apply speed, move toward target
                shot_direction = shot_direction.normalize()
                # Cadence countdown — fire a shot when it reaches 0
                self._cad_counter -= 1
                if self._cad_counter <= 0:
                    self._cad_counter = self.cad
                    self.create_shot()
                    print("Shot created")

                # Step all active shots
                for shot in self.shots:
                    shot.step()

                # Remove dead shots
                self.shots = [s for s in self.shots if s.is_alive()]

                if self.pos.x <= 50:
                    self.moving_right = True
                if self.pos.x >= SCREEN_WIDTH - 50:
                    self.moving_right = False

                if self.moving_right == True:
                    direction = pygame.Vector2(1,0)
                elif self.moving_right== False:
                    direction = pygame.Vector2(-1,0)

            self.pos += direction * self.speed


    # ------------------------------------------------------------------ #
    #  create_shot — spawn a new shot beneath the boss                   #
    # ------------------------------------------------------------------ #
    def create_shot(self):
        """Create a shot 10px above the player, moving upward."""
        shot = Shot()
        shot.setup(
            x=self.pos.x,
            y=self.pos.y + self.get_rect().height + 10,      # 10 px beneath the boss
            dx=0,
            dy= self.shotspd,        # Moving upward (negative Y)
            image_prefix="Shot",
            anim_speed=1,
            hp=1,
            rng=self.rng,
            dmg=self.dmg,
        )
        self.shots.append(shot)
    
    # ------------------------------------------------------------------ #
    #  draw — draw boss and all shots                                  #
    # ------------------------------------------------------------------ #
    def draw(self, screen: pygame.Surface):
        """Draw the boss and all active shots."""
        # Draw shots first (behind player)
        for shot in self.shots:
            shot.draw(screen)
        # Draw player
        super().draw(screen)