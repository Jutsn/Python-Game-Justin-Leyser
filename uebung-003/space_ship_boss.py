import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from enemy import Enemy
from shot import Shot
from space_ship_enemy import SpaceShip

class SpaceShipBoss(SpaceShip):
    def __init__(self,):
        super().__init__()

        self.shots: list[Shot] = []   # Active shots
        self.rng = 700      # Shot range in frames
        self.dmg = 1        # Damage per shot
        self.cad = 40       # Cadence: frames between shots
        self.shotspd = 2    # Shot speed (pixels per frame, upward)
        self._cad_counter = 0   # Countdown to next shot
    
  
