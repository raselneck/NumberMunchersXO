import pygame, sys
from input import xo_input

class HighScoreScreen:

    def __init__(self, manager, screen):
        self.stateManager = manager
        self.window = screen
        pass

    def start(self):
        pass
        
    def update(self):
        if (xo_input.btn_check):
            self.stateManager.switchGameState("MainScreen")
    
    def draw(self):
        pass
    
    def final(self):
        pass