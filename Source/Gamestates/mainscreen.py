import pygame
from input import xo_input
from UI.uicontainer import UIContainer

class MainScreen:
    """
    Defines the main menu screen
    """
    stateManager = None
    window = None
    uiContainer = None

    def __init__(self, manager, screen):
        self.stateManager = manager
        self.window = screen
        self.uiContainer = UIContainer(self.window)
        button = self.uiContainer.add_button()
        button.rect = pygame.Rect(50, 50, 50, 50)

    def start(self):
        print "Start MainScreen"
        
    def update(self):
        if (xo_input.btn_check):
            self.stateManager.switchGameState("GameScreen")
        self.uiContainer.update()
    
    def draw(self):
        pygame.draw.rect(self.window, (0, 255, 0), (50, 50, 50, 50), 0)
        self.uiContainer.draw()
    
    def final(self):
        print "final"