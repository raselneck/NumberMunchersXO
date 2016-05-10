import pygame, sys
import random
from input import xo_input
from UI.uicontainer import UIContainer

gScore = 0

def getScore():
    global gScore
    return gScore

def setScore(score):
    global gScore
    gScore = score

def getRandomName():
    # Potential to get an easter egg random name
    if random.random() < 0.1:
        names = ["I_AM_COOL",
                 "I_AM_AWESOME",
                 "1337-HAXOR",
                 "ASH_KETCHUM",
                 "GARY_OAK",
                 "CARL SAGAN"]
        return names[random.randint(0, len(names) - 1)]
    return ""

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
        self.textFont = pygame.font.SysFont("monospace", 25)
        self.textColour = (128, 128, 128)

        self.screenInfo = pygame.display.Info()
        pass

    def start(self):
        global gScore
        if self.highscores.compareHighScores(gScore):
            if self.__selector is None:
                self.__selector = self.uiContainer.add_name_selector(10, 10)
                self.__selector.setName(getRandomName())
                self.__selector.rect = pygame.Rect(610, 537, 0, 0)
            else:
                self.__selector.enable()
            self.newHighScore = True
        else:
            self.newHighScore = False
            if self.__selector is not None:
                self.__selector.disable()

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
        if self.newHighScore:
            self.drawText("Please enter your name: ", self.textFont, -120, 150)
        self.uiContainer.draw()

    def final(self):
        if self.__selector is not None:
            self.__selector.setName("")

    def drawText(self, text, font, offsetX, offsetY):
        label = font.render(text, 1, self.textColour)
        text_width, text_height = font.size(text)
        text_x = (self.screenInfo.current_w/2) - (text_width/2) + offsetX
        text_y = (self.screenInfo.current_h/2) - (text_height/2) + offsetY
        self.window.blit(label, (text_x, text_y))
