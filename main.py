import pygame
import random

# Init pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Title & Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo-flying.png")
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load("battleship.png")
playerX = 370
playerY = 480
playerXChange = 0

# Alien
alienImage = pygame.image.load("alien.png")
alienX = random.randint(10, 726)
alienY = random.randint(74, 140)
alienXChange = 0.1
alienYChange = 40

# Alien
bulletImage = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletXChange = 0
bulletYChange = 0.20
# Ready - Bullet is not fired
# Fire - Bullet is fired & travelling
bulletState = "ready"


def player(x, y):
    screen.blit(playerImage, (x, y))


def alien(x, y):
    screen.blit(alienImage, (x, y))


def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))


# Game loop
running = True
while running:
    # Background
    screen.fill((64, 56, 64))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXChange = -0.3
            if event.key == pygame.K_RIGHT:
                playerXChange = + 0.3
            if event.key == pygame.K_SPACE:
                if bulletState == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXChange = 0

    # Alien movement
    playerX += playerXChange
    if playerX <= 10:
        playerX = 10
    elif playerX >= 726:
        playerX = 726

    # Enemy movement
    alienX += alienXChange
    if alienX <= 10:
        alienXChange = 0.3
        alienY += alienYChange
    elif alienX >= 726:
        alienXChange = -0.3
        alienY += alienYChange

    #  bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"
    if bulletState is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletYChange

    # Player
    player(playerX, playerY)
    alien(alienX, alienY)

    # Last call
    pygame.display.update()
