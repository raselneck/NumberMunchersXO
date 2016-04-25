import pygame, sys
from Input import xo_input

class MainScreen:

    def __init__(self, manager, screen):
        self.stateManager = manager
        self.window = screen
        pass

    def start(self):
        print "Start MainScreen"
        
    def update(self):
        if (xo_input.btn_check): self.stateManager.switchGameState("GameScreen")
    
    def draw(self):
        pygame.draw.rect(self.window, (0, 255, 0), (50, 50, 50, 50), 0)
    
    def final(self):
        print "final"