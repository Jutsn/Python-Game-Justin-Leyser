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
player_jump_power = 5


# ---- Bouncing circle (aus dem "Boing boing"-Beispiel) ----
circle_x = 300.0
circle_y = 50.0
circle_radius = 10
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

# Player: Collisions-Check 
def Check_For_Player_Collision(rect):
    if player.colliderect(rect):
        return True
    else:
        return False

# Player: Clamping auf X-Achse
def Clamp_player_pos():
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

            if event.key == pygame.K_w and is_grounded or event.key == pygame.K_SPACE and is_grounded:
                player_movement_y = -player_jump_power 
                is_grounded = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_moving_left = False
            elif event.key == pygame.K_d:
                player_moving_right = False

        

    # ---- Update ----
    # Player: Bewegung + Gravitation
    if player_moving_right:
        player.x += 3
    elif player_moving_left:
        player.x -= 3

    player_movement_y += gravity
    player.y += player_movement_y
       

    # Player: An den Seiten stoppen
    Clamp_player_pos()

    # Player: Mit Hindernissen kollidieren 
    for obs in obstacles:
        if (Check_For_Player_Collision(obs)):
            if (player.bottom - obs.top <= 10):
                player.bottom = obs.top
                is_grounded = True
                player_movement_y = 0
            elif (player.bottom - obs.top >= 10):
                player_movement_y = 0.1
        

    # Bouncing circle: Gravitation + Bewegung
    circle_movement_y += gravity
    circle_x += circle_movement_x
    circle_y += circle_movement_y

    # Bouncing circle: Am Boden abprallen
    if circle_y >= SCREEN_HEIGHT - 20 - circle_radius:
        circle_movement_y = -circle_movement_y

    # Bouncing circle: An den Seiten abprallen
    if circle_x <= circle_radius or circle_x >= SCREEN_WIDTH - circle_radius:
        circle_movement_x = -circle_movement_x

    # ---- Draw ----
    screen.fill(BACKGROUND_COL)

    # Obstacles zeichnen
    for obs in obstacles:
        pygame.draw.rect(screen, GROUND_COL, obs)

    # Bouncing circle zeichnen
    pygame.draw.circle(screen, CIRCLE_COL, (int(circle_x), int(circle_y)), circle_radius)

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

