# player.py
# Player entity — follows mouse X, auto-fires shots.

import pygame
from entity import Entity
from shot import Shot


class Player(Entity):
    """The player ship. Follows mouse X position and auto-fires shots."""

    def __init__(self):
        super().__init__()
        self.shots: list[Shot] = []   # Active shots

        # Weapon stats (matching C++ defaults)
        self.rng = 100      # Shot range in frames
        self.dmg = 1        # Damage per shot
        self.cad = 50       # Cadence: frames between shots
        self.shotspd = 1    # Shot speed (pixels per frame, upward)

        self.rng_power_up = 5
        self.dmg_power_up = 5
        self.cad_power_up = 25
        self.shotspd_power_up = 5

        self._cad_counter = 0   # Countdown to next shot
        self.start_time = 0
        self.power_up_time = 15
        self.power_up_active = False
    # ------------------------------------------------------------------ #
    #  setup — place player near bottom of screen                        #
    # ------------------------------------------------------------------ #
    def setup(
        self,
        x: float,
        y: float,
        dx: float,
        dy: float,
        image_prefix: str,
        anim_speed: int,
        hp: int,
    ):
        """Initialize the player."""
        super().setup(x, y, dx, dy, image_prefix, anim_speed, hp)
        self._cad_counter = self.cad

    # ------------------------------------------------------------------ #
    #  set_might — configure weapon stats (mirrors C++ setMight)         #
    # ------------------------------------------------------------------ #
    def set_might(self, rng: int, dmg: int, cad: int, shotspd: int):
        """Configure weapon stats. Called from main after setup."""
        self.rng = rng
        self.dmg = dmg
        self.cad = cad
        self.shotspd = shotspd
        self._cad_counter = cad

    def upgrade_might(self, upgrade_type):
        """Upgrade weapon stats. Called from ShopManager when Shopping Upgrades."""
        if upgrade_type == "+100 Range":
            self.rng += 100
            print(str(self.rng))
        if upgrade_type == "+1 Damage":
            self.dmg += 1
            print(str(self.dmg))
        if upgrade_type == "+10% Fire Rate":
            self.cad -= 5
            print(str(self.cad))
        if upgrade_type == "+1 Shot Speed":
            self.shotspd += 1
            print(str(self.shotspd))
    
    def power_up_might(self, duration):
        """Upgrade weapon stats. Called from main when collecting Obstacle."""
        self.rng += self.rng_power_up
        self.dmg += self.dmg_power_up
        self.cad -= self.cad_power_up
        self.shotspd += self.shotspd_power_up
        self.power_up_time = duration
        self.start_time = pygame.time.get_ticks()
        self.power_up_active = True

    def reset_power_up(self):
        """Reset Upgrade stats. Called from player when timer is cleared."""
        self.rng -= self.rng_power_up
        self.dmg -= self.dmg_power_up
        self.cad += self.cad_power_up
        self.shotspd -= self.shotspd_power_up

    def run_power_up_timer(self):
        self.elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
        self.remaining = self.power_up_time - self.elapsed

        if self.remaining <= 0:
            self.power_up_active = False
            self.reset_power_up()
        

     

    # ------------------------------------------------------------------ #
    #  step — move, track mouse X, fire shots, update shots              #
    # ------------------------------------------------------------------ #
    def step(self):
        """Per-frame update: move, fire when cadence allows, update shots."""
        # Move by direction (in case dir is set)
        super().step()

        # Player X follows mouse X position
        mouse_x, _ = pygame.mouse.get_pos()
        self.pos.x = mouse_x

        # Cadence countdown — fire a shot when it reaches 0
        self._cad_counter -= 1
        if self._cad_counter <= 0:
            self._cad_counter = self.cad
            self.create_shot()

        # Step all active shots
        for shot in self.shots:
            shot.step()

        # Remove dead shots
        self.shots = [s for s in self.shots if s.is_alive()]

        # Start Power-Up Timer
        if (self.power_up_active):
           self.run_power_up_timer()


    # ------------------------------------------------------------------ #
    #  create_shot — spawn a new shot above the player                   #
    # ------------------------------------------------------------------ #
    def create_shot(self):
        """Create a shot 10px above the player, moving upward."""
        shot = Shot()
        shot.setup(
            x=self.pos.x,
            y=self.pos.y - 10,      # 10 px above player
            dx=0,
            dy=-self.shotspd,        # Moving upward (negative Y)
            image_prefix="Shot",
            anim_speed=1,
            hp=1,
            rng=self.rng,
            dmg=self.dmg,
        )
        self.shots.append(shot)

    # ------------------------------------------------------------------ #
    #  draw — draw player and all shots                                  #
    # ------------------------------------------------------------------ #
    def draw(self, screen: pygame.Surface):
        """Draw the player and all active shots."""
        # Draw shots first (behind player)
        for shot in self.shots:
            shot.draw(screen)
        # Draw player
        super().draw(screen)

    
