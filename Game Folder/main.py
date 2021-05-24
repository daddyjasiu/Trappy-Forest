import pygame
import sys

############################################################
# MODEL/DAO
############################################################

# GAME INIT:
pygame.init()
pygame.display.set_caption('Trappy Forest')
width = 1400
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# GAME VARIABLES:
gameActive = False

# IMPORTING ASSETS:
menuBackground = pygame.image.load('assets/menu/menuBG.jpg')
menuBackground = pygame.transform.scale(menuBackground, (1400, 720))

menuWelcome = pygame.image.load('assets/menu/welcome.png')
menuPressReturn = pygame.image.load('assets/menu/press_return.png')

############################################################
# VIEW-MODEL
############################################################



############################################################
# VIEW
############################################################
def drawMenu():
    screen.blit(menuBackground, (0, 0))
    screen.blit(menuWelcome, (65, 100))
    screen.blit(menuPressReturn, (200, 400))

def drawFirstLevel():
    screen.fill((255, 255, 255))

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
