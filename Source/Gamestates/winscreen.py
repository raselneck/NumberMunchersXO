import pygame, sys
from input import xo_input

class WinScreen:

    def __init__(self, manager, screen):
        self.stateManager = manager
        self.window = screen

        self.titleFont = pygame.font.SysFont("monospace", 75, bold=True)
        self.textColour = (128, 128, 128)

        self.screenInfo = pygame.display.Info()
        score = 0
        pass

    def start(self):
        pass

    def update(self):
        if (xo_input.btn_cross):
            self.stateManager.switchGameState("MainScreen")

    def draw(self):
        self.drawText("Game Over!", self.titleFont, 0, -50)
        self.drawText("Final Score: " + str(self.score), self.titleFont, 0, 50)

    def final(self):
        pass

    def drawText(self, text, font, offsetX, offsetY):
        label = font.render(text, 1, self.textColour)
        text_width, text_height = font.size(text)
        self.window.blit(label, ((self.screenInfo.current_w/2) - (text_width/2) + offsetX, (self.screenInfo.current_h/2) - (text_height/2) + offsetY))

def setScore(score):
    WinScreen.score = score
    pass