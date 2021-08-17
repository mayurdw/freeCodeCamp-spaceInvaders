import pygame

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


def player(x, y):
    screen.blit(playerImage, (x, y))


# Game loop
running = True
while running:
    # Background
    screen.fill((64, 56, 64))
    # Player
    player(playerX, playerY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Last call
    pygame.display.update()
