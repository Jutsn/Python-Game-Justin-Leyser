import pygame
import os
import RedBallManager
import CollisionManager

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
rbm = RedBallManager
cM = CollisionManager
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
jumping_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "sounds", "jump.wav"))
jumping_sound.set_volume(1.0)
player_sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites", "sprite_40.png"))
image = pygame.Surface([32, 32])

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
# Plattform 002
platform_2 = pygame.Rect(30, SCREEN_HEIGHT - 220, 100, 10)
obstacles.append(platform_2)
# Plattform 003
platform_3 = pygame.Rect(100, SCREEN_HEIGHT - 140, 100, 10)
obstacles.append(platform_3)
# Plattform 004
platform_4 = pygame.Rect(400, SCREEN_HEIGHT - 140, 100, 10)
obstacles.append(platform_4)
# Plattform 005
platform_5 = pygame.Rect(470, SCREEN_HEIGHT - 220, 100, 10)
obstacles.append(platform_5)

# ---- Status-Text ----
status = "Wheee!"
show_time = 1
show_time_stamp = 0
count = 0
score = "Score:"

# ---- Game-Timer ----
game_time = 20
game_over = False

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
rbm.register_red_ball()
while running:

    if pygame.time.get_ticks()/1000 >= game_time:
        game_over = True
        
    

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
    if not game_over:
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
            show_time_stamp = pygame.time.get_ticks()/1000
        elif (pygame.time.get_ticks()/1000 >= show_time + show_time_stamp):
            status = "Wheee!"

       # Player: Kollision mit Red Balls
        for ball in rbm.balls:
            if check_for_player_collision(ball):
                count += 1
                ball.die()
    
       # Red Balls
        rbm.update_red_balls()
        cM.handle_red_ball_collisions(obstacles)  

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

    rbm.draw_red_balls(screen)     

   # Player zeichnen
    screen.blit(player_sprite, player.topleft)

   # Text zeichnen
    font = pygame.font.SysFont(None, 24)
    status_surface = font.render(status, True, TEXT_COL)
    count_surface = font.render(str(count), True, TEXT_COL)
    screen.blit(status_surface, (30, 30))
    screen.blit(count_surface, (540, 30))

    if game_over:
        score = "Score: " + str(count)
        font = pygame.font.SysFont(None, 48)
        score_surface = font.render(score, True, TEXT_COL)
        screen.blit(score_surface, (240, 150))

   # ---- Flip ----
    pygame.display.flip()
    clock.tick(60)

pygame.quit()