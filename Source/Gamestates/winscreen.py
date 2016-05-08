import pygame, sys
from input import xo_input
from UI.uicontainer import UIContainer

gScore = 0

def getScore():
    global gScore
    return gScore

def setScore(score):
    global gScore
    gScore = score

class WinScreen:
    def __init__(self, manager, screen, highscores):
        self.stateManager = manager
        self.window = screen
        self.highscores = highscores
        self.newHighScore = False

        self.uiContainer = UIContainer(self.window)
        self.uiContainer.horizontalStride = 0
        self.uiContainer.verticalStride = 0
        self.__selector = None

        self.titleFont = pygame.font.SysFont("monospace", 75, bold=True)
        self.textColour = (128, 128, 128)

        self.screenInfo = pygame.display.Info()
        pass

    def start(self):
        global gScore
        if self.highscores.compareHighScores(gScore):
            self.__selector = self.uiContainer.add_name_selector(10, 10)
            self.__selector.setName("I_AM_COOL")
            print "New high score!"
        else:
            print "No new high score :/"

    def update(self):
        if xo_input.btn_check:
            if self.__selector is not None:
                global gScore
                self.highscores.addHighScore(gScore, self.__selector.getName())
            self.stateManager.switchGameState("MainScreen")
        self.uiContainer.update()

    def draw(self):
        global gScore
        self.drawText("Game Over!", self.titleFont, 0, -50)
        self.drawText("Final Score: " + str(gScore), self.titleFont, 0, 50)
        self.uiContainer.draw()

    def final(self):
        pass

    def drawText(self, text, font, offsetX, offsetY):
        label = font.render(text, 1, self.textColour)
        text_width, text_height = font.size(text)
        text_x = (self.screenInfo.current_w/2) - (text_width/2) + offsetX
        text_y = (self.screenInfo.current_h/2) - (text_height/2) + offsetY
        self.window.blit(label, (text_x, text_y))
