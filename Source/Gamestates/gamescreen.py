import pygame, sys
from input import xo_input
from UI.uicontainer import UIContainer

class GameScreen:
    def __init__(self, manager, screen):
        self.stateManager = manager
        self.window = screen

        self.uiContainer = UIContainer(self.window)

        self.screenInfo = pygame.display.Info()

    def start(self):
        # Button sizes
        padding = 10
        width = (self.screenInfo.current_w-(padding*7))/5
        height = (self.screenInfo.current_h-(padding*7))/5

        for i in range(0,5):
            for j in range(0,5):
                button = self.uiContainer.add_button()
                button.rect = pygame.Rect((padding * (i + 1)) + (width * i), (padding * (j + 1)) + (height * j), width, height)
        
    def update(self):
        if (xo_input.btn_check):
            self.stateManager.switchGameState("MainScreen")
        
        self.uiContainer.update()
    
    def draw(self):
        pygame.draw.rect(self.window, (255, 255, 255), (50, 50, 50, 50), 0)
        # UI needs to be drawn LAST
        self.uiContainer.draw()
    
    def final(self):
        pass