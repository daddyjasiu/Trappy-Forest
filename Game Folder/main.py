import pygame
import sys

############################################################
# GAME INIT:
############################################################
pygame.init()
width = 400
height = 600
screen = pygame.display.set_mode((width, height))

############################################################
# GAME MAIN LOOP:
############################################################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
