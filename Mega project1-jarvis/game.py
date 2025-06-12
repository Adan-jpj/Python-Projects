import pygame
import sys

# Initialize Pygame
pygame.init()

# Game Window
WIDTH, HEIGHT = 809, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Shadow Fight")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_RED = (255, 150, 150)
LIGHT_BLUE = (150, 150, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Fighters
fighter1 = pygame.Rect(100, 250, 50, 100)
fighter2 = pygame.Rect(650, 250, 50, 100)

# Health
fighter1_health = 100
fighter2_health = 100

# Attack states
fighter1_attacking = False
fighter2_attacking = False
attack_cooldown = 20
f1_cooldown = 0
f2_cooldown = 0

# Draw health bars
def draw_health():
    pygame.draw.rect(screen, RED, (50, 50, fighter1_health * 2, 20))
    pygame.draw.rect(screen, BLUE, (WIDTH - 250, 50, fighter2_health * 2, 20))

# Game loop
while True:
    screen.fill(WHITE)

    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_b]:
        fighter1.x -= 5
    if keys[pygame.K_d]:
        fighter1.x += 5
    if keys[pygame.K_LEFT]:
        fighter2.x -= 5
    if keys[pygame.K_RIGHT]:
        fighter2.x += 5

    # Fighter 1 attack (space)
    if keys[pygame.K_SPACE] and f1_cooldown == 0:
        fighter1_attacking = True
        f1_cooldown = attack_cooldown

    # Fighter 2 attack (right shift)
    if keys[pygame.K_RSHIFT] and f2_cooldown == 0:
        fighter2_attacking = True
        f2_cooldown = attack_cooldown

    # Attack collision
    if fighter1_attacking and fighter1.colliderect(fighter2):
        fighter2_health -= 10
        fighter1_attacking = False
    if fighter2_attacking and fighter2.colliderect(fighter1):
        fighter1_health -= 10
        fighter2_attacking = False

    # Reduce cooldown
    if f1_cooldown > 0:
        f1_cooldown -= 1
    if f2_cooldown > 0:
        f2_cooldown -= 1

    # Draw fighters
    pygame.draw.rect(screen, RED, fighter1)
    pygame.draw.rect(screen, BLUE, fighter2)

    # Draw attack effect
    if fighter1_attacking:
        pygame.draw.rect(screen, LIGHT_RED, (fighter1.x + 50, fighter1.y + 20, 20, 20))
    if fighter2_attacking:
        pygame.draw.rect(screen, LIGHT_BLUE, (fighter2.x - 20, fighter2.y + 20, 20, 20))

    # Draw health bars
    draw_health()

    # Win/Lose condition
    if fighter1_health <= 0:
        print("Fighter 2 Wins!")
        pygame.quit()
        sys.exit()

    if fighter2_health <= 0:
        print("Fighter 1 Wins!")
        pygame.quit()
        sys.exit()

    # Update screen
    pygame.display.update()
    clock.tick(FPS)
