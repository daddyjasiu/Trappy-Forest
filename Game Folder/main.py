import pygame
import sys

############################################################
# MODEL/DAO
############################################################

class MODEL_PLAYER:
    def __init__(self):
        self.vectX = 100
        self.vectY = 100
        self.velocityY = -5
        self.playerSpriteIdle1 = pygame.image.load('assets/heroes/3 Dude_Monster/idle/1.png');
        self.playerSpriteIdle1 = pygame.transform.scale(self.playerSpriteIdle1, (45, 69))
        self.playerSpriteIdle1RECT = self.playerSpriteIdle1.get_rect()

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
            if(turnedLeft == False):
                self.player.playerSpriteIdle1 = pygame.transform.flip(self.player.playerSpriteIdle1, True, False)
                game.turnedLeft = True

        if keys[pygame.K_d] and self.player.vectX < 1400 - 45:
            self.player.vectX += 5
            if (turnedLeft == True):
                self.player.playerSpriteIdle1 = pygame.transform.flip(self.player.playerSpriteIdle1, True, False)
                game.turnedLeft = False


        if (didJump == True):
            self.player.vectY -= self.player.velocityY
            self.player.velocityY -= 1
            print(self.player.velocityY)
            if (self.player.velocityY < -25):
                game.didJump = False
                self.player.velocityY = 25
        if(didJump == False and self.player.vectY < 720-69):
            if(self.player.velocityY > -25):
                self.player.velocityY -= 1
            self.player.vectY -= self.player.velocityY
            if(self.player.vectY >= 720-69):
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
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Trappy Forest')
        width = 1400
        height = 720
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

    # GAME VARIABLES:
    gameActive = False
    didJump = False
    turnedLeft = False

    # IMPORTING ASSETS:
    menuBackground = pygame.image.load('assets/menu/menuBG.jpg')
    menuBackground = pygame.transform.scale(menuBackground, (1400, 720))
    menuWelcome = pygame.image.load('assets/menu/welcome.png')
    menuPressReturn = pygame.image.load('assets/menu/press_return.png')

    def drawMenu(self):
        self.screen.blit(self.menuBackground, (0, 0))
        self.screen.blit(self.menuWelcome, (65, 100))
        self.screen.blit(self.menuPressReturn, (200, 400))

    def drawFirstLevel(self):
        self.screen.fill((255, 255, 0))
        self.player = MODEL_PLAYER()
        self.viewModelPlayer = VIEW_MODEL_PLAYER(self.player)
        self.viewPlayer = VIEW_PLAYER(self.viewModelPlayer)

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
                        self.drawFirstLevel()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE and self.player.vectY > 0 and self.gameActive and self.didJump == False:
                        self.didJump = True

            if not self.gameActive:
                self.drawMenu()
            if self.gameActive:
                self.screen.fill((255, 255, 0))
                self.viewPlayer.drawPlayer(self.screen)
                self.viewModelPlayer.playerMovement(self.didJump, self.turnedLeft)

            pygame.display.update()


# GAME START
game = GAME()
game.playGame()
