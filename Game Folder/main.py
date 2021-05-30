import time

import pygame
import sys

############################################################
# MODEL/DAO
############################################################

class MODEL_PLAYER:
    def __init__(self):
        self.vectX = 70
        self.vectY = 300
        self.velocityY = -5
        self.playerSpriteIdle1 = pygame.image.load('assets/heroes/3 Dude_Monster/idle/1.png').convert_alpha()
        self.playerSpriteIdle1 = pygame.transform.scale(self.playerSpriteIdle1, (45, 69)).convert_alpha()
        self.playerRect = self.playerSpriteIdle1.get_rect()
        self.playerRect.topleft = (70, 300)
############################################################
# VIEW-MODEL
############################################################

class VIEW_MODEL_PLAYER:
    def __init__(self, playerData):
        self.player = playerData

    def getPlayerSpriteIdle(self):
        return self.player.playerSpriteIdle1

    def getPlayerX(self):
        return self.player.vectX

    def getPlayerY(self):
        return self.player.vectY

    def playerMovement(self, didJump, turnedLeft, firstLevel):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.player.vectX > 0:
            self.player.vectX -= 5
            self.player.playerRect.x -= 5

            if(turnedLeft == False):
                self.player.playerSpriteIdle1 = pygame.transform.flip(self.player.playerSpriteIdle1, True, False)
                game.turnedLeft = True

        if keys[pygame.K_d] and self.player.vectX < 1400 - 45:
                    self.player.vectX += 5
                    self.player.playerRect.x += 5
                    if (turnedLeft == True):
                            self.player.playerSpriteIdle1 = pygame.transform.flip(self.player.playerSpriteIdle1, True, False)
                            game.turnedLeft = False


        if (didJump == True ):
            self.player.vectY -= self.player.velocityY
            self.player.playerRect.y -= self.player.velocityY
            self.player.velocityY -= 1
            if (self.player.velocityY < -25):
                game.didJump = False
                self.player.velocityY = 25
        if(didJump == False and self.player.vectY < 720-130):
            if(self.player.velocityY > -25):
                self.player.velocityY -= 1
            self.player.vectY -= self.player.velocityY
            self.player.playerRect.y -= self.player.velocityY
            if(self.player.vectY >= 720-130):
                self.player.velocityY = 25


############################################################
# VIEW
############################################################

class VIEW_PLAYER:
    def __init__(self, p):
        self.viewModelPlayer = p

    def drawPlayer(self, sc):
        self.screen = sc
        self.screen.blit(self.viewModelPlayer.getPlayerSpriteIdle(),
                         (self.viewModelPlayer.getPlayerX(), self.viewModelPlayer.getPlayerY()))


class GAME:

    # GAME INIT:
    pygame.init()
    pygame.display.set_caption('Trappy Forest')
    width = 1400
    height = 720
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    # GAME VARIABLES:
    gameActive = False
    didLose = False
    didJump = False
    turnedLeft = False
    firstLevel = False

    # IMPORTING ASSETS:
    menuBackground = pygame.image.load('assets/menu/menuBG.jpg').convert()
    menuBackground = pygame.transform.scale(menuBackground, (1400, 720)).convert()
    menuWelcome = pygame.image.load('assets/menu/welcome.png').convert()
    menuWelcome = pygame.transform.scale(menuWelcome, (1300, 133)).convert()
    menuPressReturn = pygame.image.load('assets/menu/press_return.png').convert()
    menuPressReturn = pygame.transform.scale(menuPressReturn, (1100, 130)).convert()

    menuDied = pygame.image.load('assets/menu/you_died.png').convert()
    menuDied = pygame.transform.scale(menuDied, (1000, 156)).convert()
    menuPressReturnDied = pygame.image.load('assets/menu/restart_return.png').convert()
    menuPressReturnDied = pygame.transform.scale(menuPressReturnDied, (1100, 119)).convert()

    skyBackground = pygame.image.load('assets/enviroment/sky_backgroud.png').convert()
    level1Background = pygame.image.load('assets/enviroment/level1_background.png').convert()

    bitcoin = pygame.image.load('assets/enviroment/bitcoin.png').convert_alpha()
    bitcoin = pygame.transform.scale(bitcoin, (45, 69)).convert_alpha()

    bridgeLeft = pygame.image.load('assets/enviroment/bridge_left.png').convert_alpha()
    bridgeLeft = pygame.transform.scale(bridgeLeft, (140, 154)).convert_alpha()
    bridgeLeftRect = bridgeLeft.get_rect()
    bridgeLeftRect.topleft = (0, 50)

    bridgeRight = pygame.image.load('assets/enviroment/bridge_right.png').convert_alpha()
    bridgeRight = pygame.transform.scale(bridgeRight, (140, 154)).convert_alpha()
    bridgeRightRect = bridgeRight.get_rect()
    bridgeRightRect.topleft = (1265, 340)

    platformMid = pygame.image.load('assets/enviroment/bridge_mid_platform_triple.png').convert_alpha()
    platformMid = pygame.transform.scale(platformMid, (315, 42)).convert_alpha()
    platformMidRect = platformMid.get_rect()
    platformMidRect.topleft = (600, 300)
    platformLeftRect = platformMid.get_rect()
    platformLeftRect.topleft = (140, 141)

    platformRight = pygame.image.load('assets/enviroment/bridge_mid_platform.png').convert_alpha()
    platformRight = pygame.transform.scale(platformRight, (105, 42)).convert_alpha()
    platformRightRect = platformRight.get_rect()
    platformRightRect.topleft = (1167, 431)
    

    spikes = pygame.image.load('assets/enviroment/spikes.png').convert_alpha()
    spikes = pygame.transform.scale(spikes, (100, 96)).convert_alpha()
    
    spikesRect = spikes.get_rect()
    spikesRect.topleft = (450, 620)


    def drawMenu(self):
        self.screen.blit(self.menuBackground, (0, 0))
        self.screen.blit(self.menuWelcome, (50, 100))
        self.screen.blit(self.menuPressReturn, (150, 360))

    def drawPlayerLost(self):
        self.screen.blit(self.menuBackground, (0, 0))
        self.screen.blit(self.menuDied, (65, 100))
        self.screen.blit(self.menuPressReturnDied, (200, 400))

    def initPlayerAndAscreen(self):
        self.player = MODEL_PLAYER()
        self.viewModelPlayer = VIEW_MODEL_PLAYER(self.player)
        self.viewPlayer = VIEW_PLAYER(self.viewModelPlayer)

    def drawFirstLevel(self):
        self.screen.blit(self.level1Background, (0, 0))

        self.screen.blit(self.bitcoin, (240, 65))
        self.screen.blit(self.bitcoin, (732, 220))
        self.screen.blit(self.bitcoin, (1235, 355))

        self.screen.blit(self.bridgeLeft, (0, 50))
        self.screen.blit(self.platformMid, (140, 141))
        self.screen.blit(self.bridgeRight, (1265, 340))
        self.screen.blit(self.platformRight, (1167, 431))
        self.screen.blit(self.platformMid, (600, 300))

        self.screen.blit(self.spikes, (450, 580))


    ############################################################
    # GAME MAIN LOOP:
    ############################################################
    def playGame(self):
        while True:
            self.clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and not self.gameActive:
                        self.gameActive = True
                        self.didLose = False
                        self.turnedLeft = False
                        self.initPlayerAndAscreen()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE and self.gameActive and self.didJump == False:
                        if self.player.vectY > 0:
                            self.didJump = True

            if not self.gameActive:
                if not self.didLose:
                    self.drawMenu()
                elif self.didLose:
                    self.drawPlayerLost()
            if self.gameActive:
                self.drawFirstLevel()
                self.firstLevel = True
                self.viewPlayer.drawPlayer(self.screen)
                self.viewModelPlayer.playerMovement(self.didJump, self.turnedLeft, self.firstLevel)
                if self.player.playerRect.colliderect(self.spikesRect):
                    print("!COLLISION!")
                    self.gameActive = False
                    self.didLose = True


            pygame.display.update()


# GAME START
game = GAME()
game.playGame()
