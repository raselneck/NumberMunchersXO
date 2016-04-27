import pygame, sys
from input import xo_input

class GameScreen:

    def __init__(self, manager, screen):
        self.stateManager = manager
        self.window = screen
        pass

    def start(self):
        print "Start GameScreen"
        
    def update(self):
        if (xo_input.btn_check):
            self.stateManager.switchGameState("MainScreen")
    
    def draw(self):
        pygame.draw.rect(self.window, (255, 255, 255), (50, 50, 50, 50), 0)
    
    def final(self):
        print "final"