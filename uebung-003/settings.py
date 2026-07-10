# settings.py
# Game constants and configuration.

import os
import pygame

pygame.font.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GOLD = (255,215,0)


#Fonts
SMALL_FONT = pygame.font.SysFont(None, 30)
MEDIUM_FONT = pygame.font.SysFont(None, 40)
BIG_MEDIUM_FONT = pygame.font.SysFont(None, 42)
BIG_FONT = pygame.font.SysFont(None, 50)

# Asset path (relative to main.py)
ASSET_DIR = os.path.join(os.path.dirname(__file__), "assets")
