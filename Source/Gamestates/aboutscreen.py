import pygame, sys
from input import xo_input

class AboutScreen:

    def __init__(self, manager, screen):
        self.stateManager = manager
        self.window = screen
        pass

    def start(self):
        pass
        
    def update(self):
        if (xo_input.btn_cross):
            self.stateManager.switchGameState("MainScreen")
    
    def draw(self):
        pygame.draw.rect(self.window, (255, 0, 0), (50, 200, 50, 50), 0)
    
    def final(self):
        pass