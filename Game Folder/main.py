import pygame
import sys

############################################################
# GAME FUNCTIONS:
############################################################
def drawMenu():
    background = pygame.image.load('assets/menu/menuBG.jpg')
    background = pygame.transform.scale(background, (1400, 720))

    welcomeSign = pygame.image.load('assets/menu/welcome.png')
    returnSign = pygame.image.load('assets/menu/press_return.png')

    screen.blit(background, (0, 0))
    screen.blit(welcomeSign, (65, 100))
    screen.blit(returnSign, (200, 400))

def drawFirstLevel():
    screen.fill((255, 255, 255))

############################################################
# GAME INIT:
############################################################
pygame.init()
pygame.display.set_caption('Trappy Forest')
width = 1400
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

############################################################
# GAME VARIABLES:
############################################################
gameActive = False

############################################################
# GAME MAIN LOOP:
############################################################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not gameActive:
                gameActive = True
            if event.key == pygame.K_ESCAPE and not gameActive:
                pygame.quit()
                sys.exit()

        if not gameActive:
            drawMenu()
        if gameActive:
            drawFirstLevel()

    pygame.display.update()
    clock.tick(120)
