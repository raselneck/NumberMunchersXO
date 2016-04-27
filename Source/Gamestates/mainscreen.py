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
    testButton = None

    def __init__(self, manager, screen):
        self.stateManager = manager
        self.window = screen

        self.uiContainer = UIContainer(self.window)
        button = self.uiContainer.add_button()
        button.rect = pygame.Rect(640, 300, 100, 20)
        button.text = "Start Game"
        self.testButton = button
        pass

    def start(self):
        pass
   
    def update(self):
        if xo_input.btn_check or self.testButton.was_pressed():
            self.stateManager.switchGameState("GameScreen")
        self.uiContainer.update()
    
    def draw(self):
        # UI needs to be drawn LAST
        self.uiContainer.draw()
    
    def final(self):
        pass