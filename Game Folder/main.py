import time
import pygame
import sys
from pygame import mixer

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

    def playerMovement(self, didJump, turnedLeft):

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
    mixer.init()
    mixer.music.load('assets/music/soundtrack/soundtrack_op.wav')
    mixer.music.play(-1)

    # GAME VARIABLES:
    gameActive = False
    didLose = False
    didJump = False
    turnedLeft = False
    firstLevel = False
    secondLevel = False
    isFirstCoinCollected = False
    isSecondCoinCollected = False
    isThirdCoinCollected = False

    # IMPORTING ASSETS:
    jumpSound = mixer.Sound('assets/music/sounds/jump.wav')
    coinSound = mixer.Sound('assets/music/sounds/coin.wav')
    deathSound = mixer.Sound('assets/music/sounds/death.wav')

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

    bitcoinRect1 = bitcoin.get_rect()
    bitcoinRect2 = bitcoin.get_rect()
    bitcoinRect3 = bitcoin.get_rect()

    spikesSmallUp = pygame.image.load('assets/enviroment/spikes.png').convert_alpha()
    spikesSmallUp = pygame.transform.scale(spikesSmallUp, (100, 96)).convert_alpha()
    spikesLongDown = pygame.image.load('assets/enviroment/spikes_long.png').convert_alpha()
    spikesLongDown = pygame.transform.scale(spikesLongDown, (100, 311)).convert_alpha()
    spikesLongDown = pygame.transform.flip(spikesLongDown, False, True)
    spikesLongUp = pygame.image.load('assets/enviroment/spikes_long.png').convert_alpha()
    spikesLongUp = pygame.transform.scale(spikesLongUp, (100, 311)).convert_alpha()

    boulder = pygame.image.load('assets/enviroment/boulder.png').convert_alpha()
    boulder = pygame.transform.scale(boulder, (180, 180))

    boulderRect1 = boulder.get_rect()
    boulderRect2 = boulder.get_rect()
    boulderRect3 = boulder.get_rect()

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

    def resetCoinRects(self):
        self.bitcoinRect1.topleft = (0, 0)
        self.bitcoinRect2.topleft = (0, 0)
        self.bitcoinRect3.topleft = (0, 0)

    def resetSpikesRects(self):
        self.spikesLongUpRect1.topleft = (0, 0)
        self.spikesLongUpRect2.topleft = (0, 0)
        self.spikesLongUpRect3.topleft = (0, 0)
        self.spikesLongDownRect1.topleft = (0, 0)
        self.spikesLongDownRect2.topleft = (0, 0)
        self.spikesLongDownRect3.topleft = (0, 0)

    def setSpikesLevel1Rects(self):
        self.spikesLongUpRect1 = self.spikesLongUp.get_rect()
        self.spikesLongUpRect1.topleft = (350, 610)
        self.spikesLongDownRect1 = self.spikesLongDown.get_rect()
        self.spikesLongDownRect1.topleft = (350, -30)
        self.spikesLongUpRect2 = self.spikesLongUp.get_rect()
        self.spikesLongUpRect2.topleft = (670, 480)
        self.spikesLongDownRect2 = self.spikesLongDown.get_rect()
        self.spikesLongDownRect2.topleft = (670, -30)
        self.spikesLongUpRect3 = self.spikesLongUp.get_rect()
        self.spikesLongUpRect3.topleft = (970, 520)
        self.spikesLongDownRect3 = self.spikesLongDown.get_rect()
        self.spikesLongDownRect3.topleft = (970, -30)

    def setBouldersLevel2Rects(self):
        

    def drawFirstLevel(self, isFirstCoinCollected, isSecondCoinCollected, isThirdCoinCollected):

        self.setSpikesLevel1Rects()

        self.screen.blit(self.level1Background, (0, 0))

        if not isThirdCoinCollected:
            self.screen.blit(self.bitcoin, (995, 330))
            self.bitcoinRect3.topleft = (995, 330)

        if isThirdCoinCollected and not isFirstCoinCollected:
            self.screen.blit(self.bitcoin, (375, 330))
            self.bitcoinRect1.topleft = (375, 330)

        if isFirstCoinCollected and not isSecondCoinCollected:
            self.screen.blit(self.bitcoin, (695, 330))
            self.bitcoinRect2.topleft = (695, 330)

        self.screen.blit(self.spikesLongUp, (350, 580))
        self.screen.blit(self.spikesLongDown, (350, -30))

        self.screen.blit(self.spikesLongUp, (670, 480))
        self.screen.blit(self.spikesLongDown, (670, -30))

        self.screen.blit(self.spikesLongUp, (970, 500))
        self.screen.blit(self.spikesLongDown, (970, -20))

    def drawSecondLevel(self, isFirstCoinCollected, isSecondCoinCollected, isThirdCoinCollected):
        self.screen.blit(self.level1Background, (0, 0))

        if not isThirdCoinCollected:
            self.screen.blit(self.bitcoin, (995, 330))
            self.bitcoinRect3.topleft = (995, 330)

        if isThirdCoinCollected and not isFirstCoinCollected:
            self.screen.blit(self.bitcoin, (375, 330))
            self.bitcoinRect1.topleft = (375, 330)

        if isFirstCoinCollected and not isSecondCoinCollected:
            self.screen.blit(self.bitcoin, (695, 330))
            self.bitcoinRect2.topleft = (695, 330)

        self.screen.blit(self.boulder, (100, 100))

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
                        self.secondLevel = True

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE and self.gameActive and self.didJump == False:
                        if self.player.vectY > 0:
                            self.jumpSound.play()
                            self.didJump = True

            if not self.gameActive:
                if not self.didLose:
                    self.drawMenu()
                elif self.didLose:
                    self.drawPlayerLost()

            # FIRST LEVEL
            if self.gameActive:
                if self.firstLevel:
                    self.drawFirstLevel(self.isFirstCoinCollected, self.isSecondCoinCollected, self.isThirdCoinCollected)

                    self.viewPlayer.drawPlayer(self.screen)
                    self.viewModelPlayer.playerMovement(self.didJump, self.turnedLeft)
                    if self.player.playerRect.colliderect(self.spikesLongDownRect1)\
                            or self.player.playerRect.colliderect(self.spikesLongUpRect1)\
                            or self.player.playerRect.colliderect(self.spikesLongUpRect2)\
                            or self.player.playerRect.colliderect(self.spikesLongDownRect2)\
                            or self.player.playerRect.colliderect(self.spikesLongUpRect3)\
                            or self.player.playerRect.colliderect(self.spikesLongDownRect3):
                        self.deathSound.play()
                        self.gameActive = False
                        self.didLose = True
                        self.isFirstCoinCollected = False
                        self.isSecondCoinCollected = False
                        self.isThirdCoinCollected = False
                        self.resetCoinRects()

                    if self.player.playerRect.colliderect(self.bitcoinRect1):
                        self.isFirstCoinCollected = True
                        self.coinSound.play()
                        self.bitcoinRect1.topleft = (0, 0)

                    if self.player.playerRect.colliderect(self.bitcoinRect2):
                        self.isSecondCoinCollected = True
                        self.coinSound.play()
                        self.bitcoinRect2.topleft = (0, 0)

                    if self.player.playerRect.colliderect(self.bitcoinRect3):
                        self.isThirdCoinCollected = True
                        self.coinSound.play()
                        self.bitcoinRect3.topleft = (0, 0)

                    if self.isFirstCoinCollected and self.isSecondCoinCollected and self.isThirdCoinCollected:
                        self.firstLevel = False
                        self.secondLevel = True
                        self.resetCoinRects()
                        self.resetSpikesRects()

                # SECOND LEVEL
                if self.secondLevel:
                    self.drawSecondLevel(self.isFirstCoinCollected, self.isSecondCoinCollected,
                                        self.isThirdCoinCollected)

                    self.viewPlayer.drawPlayer(self.screen)
                    self.viewModelPlayer.playerMovement(self.didJump, self.turnedLeft)

                    # if self.player.playerRect.colliderect(self.spikesLongDownRect1) \
                    #         or self.player.playerRect.colliderect(self.spikesLongUpRect1) \
                    #         or self.player.playerRect.colliderect(self.spikesLongUpRect2) \
                    #         or self.player.playerRect.colliderect(self.spikesLongDownRect2) \
                    #         or self.player.playerRect.colliderect(self.spikesLongUpRect3) \
                    #         or self.player.playerRect.colliderect(self.spikesLongDownRect3):
                    #     self.deathSound.play()
                    #     self.gameActive = False
                    #     self.didLose = True
                    #     self.isFirstCoinCollected = False
                    #     self.isSecondCoinCollected = False
                    #     self.isThirdCoinCollected = False
                    #     self.resetCoinRects()

                    if self.player.playerRect.colliderect(self.bitcoinRect1):
                        self.isFirstCoinCollected = True
                        self.coinSound.play()
                        self.bitcoinRect1.topleft = (0, 0)

                    if self.player.playerRect.colliderect(self.bitcoinRect2):
                        self.isSecondCoinCollected = True
                        self.coinSound.play()
                        self.bitcoinRect2.topleft = (0, 0)

                    if self.player.playerRect.colliderect(self.bitcoinRect3):
                        self.isThirdCoinCollected = True
                        self.coinSound.play()
                        self.bitcoinRect3.topleft = (0, 0)

                    if self.isFirstCoinCollected and self.isSecondCoinCollected and self.isThirdCoinCollected:
                        self.secondLevel = True

            pygame.display.update()


# GAME START
game = GAME()
game.playGame()
