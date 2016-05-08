import pygame, sys
from input import xo_input

gScore = 0

def setScore(score):
    global gScore
    gScore = score
    pass

class WinScreen:
    def __init__(self, manager, screen, highscores):
        self.stateManager = manager
        self.window = screen
        self.highscores = highscores
        self.newHighScore = False

        self.titleFont = pygame.font.SysFont("monospace", 75, bold=True)
        self.textColour = (128, 128, 128)

        self.screenInfo = pygame.display.Info()
        pass

    def start(self):
        global gScore
        self.newHighScore = self.highscores.compareHighScores(gScore)
        pass

    def update(self):
        if (xo_input.btn_cross):
            self.stateManager.switchGameState("MainScreen")

    def draw(self):
        self.drawText("Game Over!", self.titleFont, 0, -50)
        self.drawText("Final Score: " + str(gScore), self.titleFont, 0, 50)

    def final(self):
        pass

    def drawText(self, text, font, offsetX, offsetY):
        label = font.render(text, 1, self.textColour)
        text_width, text_height = font.size(text)
        text_x = (self.screenInfo.current_w/2) - (text_width/2) + offsetX
        text_y = (self.screenInfo.current_h/2) - (text_height/2) + offsetY
        self.window.blit(label, (text_x, text_y))
