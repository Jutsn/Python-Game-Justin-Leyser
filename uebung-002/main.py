import pygame

# ---- Bildschirm ----
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# ---- Farben (Rot, Grün, Blau, [Alpha]) ----
BACKGROUND_COL = (20, 100, 200)
GROUND_COL = (80, 70, 30)
PLAYER_COL = (30, 210, 76)
CIRCLE_COL = (200, 200, 255)
TEXT_COL = (255, 255, 255)

# ---- pygame starten ----
pygame.mixer.init() 
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jump & Run")
clock = pygame.time.Clock()

# ---- Player ----
player_start_x = 100.0
player_start_y = 100.0
player_sprite_radius = 20
player_col_width = player_sprite_radius * 2
player_col_height = player_sprite_radius * 2
player = pygame.Rect(player_start_x, player_start_y, player_col_width, player_col_height)
player_moving_left = False
player_moving_right = False
player_jumping = False
player_movement_y = 0.0
player_jump_power = 4.5
jumping_sound = pygame.mixer.Sound(r"D:\Games Programming\Python Game Justin Leyser\sounds\jump.wav")
jumping_sound.set_volume(1.0)

# ---- Bouncing circle (aus dem "Boing boing"-Beispiel) ----
circle_x = 300.0
circle_y = 50.0
circle_sprite_radius = 10
circle_col_width = circle_sprite_radius * 2
circle_col_height = circle_sprite_radius * 2
circle_col = pygame.Rect(circle_x, circle_y, circle_col_width, circle_col_height)
circle_movement_x = 1.0
circle_movement_y = 0.0
gravity = 0.1

# ---- Obstacles (Boden + Plattformen) ----
# Jedes Obstacle ist ein pygame.Rect(x, y, breite, hoehe)
obstacles = []

# Boden
ground = pygame.Rect(5, SCREEN_HEIGHT - 10, SCREEN_WIDTH - 10, 10)
obstacles.append(ground)

# Plattform 001
platform_1 = pygame.Rect(200, SCREEN_HEIGHT - 60, 200, 10)
obstacles.append(platform_1)

# ---- Status-Text ----
status = "Wheee!"

#pygame.mixer.find_channel()¶
# Player: Collisions-Check
def check_for_player_collision(rect):
    if player.colliderect(rect):
        return True
    else:
        return False


# Player: Clamping auf X-Achse
def clamp_player_pos():
    if player.x <= 5:
        player.x = 5
    if player.x >= SCREEN_WIDTH - player_col_width - 5:
        player.x = SCREEN_WIDTH - player_col_width - 5


# ============================================================
# Game Loop
# ============================================================

running = True
while running:

   # ---- Events ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_moving_left = True
            elif event.key == pygame.K_d:
                player_moving_right = True
           # Player: Springen        
            if event.key == pygame.K_w and is_grounded or event.key == pygame.K_SPACE and is_grounded:
                player_movement_y = -player_jump_power
                is_grounded = False
                jumping_sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_moving_left = False
            elif event.key == pygame.K_d:
                player_moving_right = False

  # ---- Update ----
   # Player: Bewegung
    if player_moving_right:
        player.x += 3
    elif player_moving_left:
        player.x -= 3

   # Player: Horizontale Kollisionen
    for obs in obstacles:
        if check_for_player_collision(obs):
            if player_moving_right:
                player.right = obs.left
            elif player_moving_left:
                player.left = obs.right
   # Player: Horizontales Clamping
    clamp_player_pos()

   # Player: Gravitation
    player_movement_y += gravity
    player.y += player_movement_y

   # Player: Vertikale Kollisionen
    for obs in obstacles:
        if check_for_player_collision(obs):
            if player_movement_y > 0:
                player.bottom = obs.top
                is_grounded = True
                player_movement_y = 0

            elif player_movement_y < 0:
                player.top = obs.bottom
                player_movement_y = 0

   # Player: Kollision mit Circle
    if check_for_player_collision(circle_col):
        status = "Ouch!"

   # Bouncing circle: Gravitation + Bewegung
    circle_movement_y += gravity
    circle_col.x += circle_movement_x
    circle_col.y += circle_movement_y

   # Bouncing circle: Am Boden abprallen
    if circle_col.y >= SCREEN_HEIGHT - 20 - circle_sprite_radius:
        circle_movement_y = -circle_movement_y

   # Bouncing circle: An den Seiten abprallen
    if circle_col.x <= circle_col_width or circle_col.x >= SCREEN_WIDTH - circle_col_width:
        circle_movement_x = -circle_movement_x

   # ---- Draw ----
    screen.fill(BACKGROUND_COL)

   # Obstacles zeichnen
    for obs in obstacles:
        pygame.draw.rect(screen, GROUND_COL, obs)

   # Bouncing circle zeichnen
    pygame.draw.circle(screen, CIRCLE_COL, circle_col.center, circle_sprite_radius)

   # Player zeichnen
    pygame.draw.circle(screen, PLAYER_COL, player.center, player_sprite_radius)

   # Text zeichnen
    font = pygame.font.SysFont(None, 24)
    text_surface = font.render(status, True, TEXT_COL)
    screen.blit(text_surface, (30, 30))

   # ---- Flip ----
    pygame.display.flip()
    clock.tick(60)

pygame.quit()