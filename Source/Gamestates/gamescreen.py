import pygame, sys
from input import xo_input
from UI.uicontainer import UIContainer
from fraction import *

class GameScreen:
    def __init__(self, manager, screen):
        self.stateManager = manager
        self.window = screen

        self.uiContainer = UIContainer(self.window)
        self.uiContainer.horizontalStride = 5
        self.initializedUI = False

        self.titleFont = pygame.font.SysFont("monospace", 45, bold=True)
        self.scoreFont = pygame.font.SysFont("monospace", 20)
        self.textColour = (128, 128, 128)

        self.screenInfo = pygame.display.Info()
        pass

    def start(self):
        if not self.initializedUI:
            # Button sizes
            padding = 10
            side_margin = 50
            top_margin = 150
            width = (self.screenInfo.current_w - (padding * 5) - (side_margin * 2)) / 5
            height = (self.screenInfo.current_h - (padding * 5) - (top_margin)) / 5

            for i in range(0, 5):
                for j in range(0, 5):
                    button = self.uiContainer.add_button()
                    # button.rect = pygame.Rect((padding * (i + 1)) + (width * i), (padding * (j + 1)) + (height * j), width, height)
                    button.rect = pygame.Rect((padding * i) + (width * i) + side_margin, (padding * j) + (height * j) + top_margin, width, height)

            self.initializedUI = True

        self.fractionAnswers = []
        self.equalFractions = []
        self.answer = frac_random()

        for x in range(1, 30):
            self.fractionAnswers.append(frac_random())
            self.equalFractions.append(self.fractionAnswers[x - 1].get_equal_fraction())
            self.right_fracs, self.wrong_fracs = create_goal(self.answer)
        
    def update(self):
        if (xo_input.btn_cross):
            self.stateManager.switchGameState("MainScreen")

        self.uiContainer.update()
    
    def draw(self):
        pygame.draw.rect(self.window, (255, 255, 255), (50, 50, 50, 50), 0)
        self.drawText("Find these multiples: " + str(self.answer), self.titleFont, 0, (-self.screenInfo.current_h/2) + 50)
        # UI needs to be drawn LAST
        self.uiContainer.draw()
    
    def final(self):
        pass

    def drawText(self, text, font, offsetX, offsetY):
        label = font.render(text, 1, self.textColour)
        text_width, text_height = font.size(text)
        self.window.blit(label, ((self.screenInfo.current_w/2) - (text_width/2) + offsetX, (self.screenInfo.current_h/2) - (text_height/2) + offsetY))