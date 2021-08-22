import pygame
import random
import math

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
alienImage = []
alienX = []
alienY = []
alienXChange = []
alienYChange = []
num_of_aliens = 6

for i in range(num_of_aliens):
    alienImage.append(pygame.image.load("alien.png"))
    alienX.append(random.randint(10, 726))
    alienY.append(random.randint(74, 140))
    alienXChange.append(0.1)
    alienYChange.append(40)

# Alien
bulletImage = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletXChange = 0
bulletYChange = 0.20
# Ready - Bullet is not fired
# Fire - Bullet is fired & travelling
bulletState = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 20
textY = 20


def show_score(x, y):
    score = font.render(f"Score : {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImage, (x, y))


def alien(x, y, index):
    screen.blit(alienImage[index], (x, y))


def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))


def isCollision(alien_x, alien_y, bullet_x, bullet_y):
    distance = math.pow(alien_x - alien_y, 2) + math.pow(bullet_x - bullet_y, 2)
    if distance <= 729:
        return True
    else:
        return False


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

    #  bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"
    if bulletState == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletYChange

        # Enemy movement
    for i in range(num_of_aliens):
        alienX[i] += alienXChange[i]
        if alienX[i] <= 10:
            alienXChange[i] = 0.3
            alienY[i] += alienYChange[i]
        elif alienX[i] >= 726:
            alienXChange[i] = -0.3
            alienY[i] += alienYChange[i]

        collision = isCollision(alienX[i], alienY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bulletState = "ready"
            score_value += 1
            alienX[i] = random.randint(10, 726)
            alienY[i] = random.randint(74, 140)
        alien(alienX[i], alienY[i], i)

    # Player
    player(playerX, playerY)
    show_score(textX, textY)

    # Last call
    pygame.display.update()
