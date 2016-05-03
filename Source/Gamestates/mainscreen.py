import pygame
from input import xo_input
from UI.uicontainer import UIContainer
from UI.button import Button

class MainScreen:
    """
    Defines the main menu screen
    """
    def __init__(self, manager, screen):
        self.stateManager = manager
        self.window = screen

        self.uiContainer = UIContainer(self.window)
        self.uiContainer.horizontalStride = 0

        self.screenInfo = pygame.display.Info()
        
        # Button sizes and positions
        width = 170
        height = 40
        cx = self.screenInfo.current_w / 2
        cy = self.screenInfo.current_h / 2
        bx = cx - (width / 2)
        padding = 20
        dy = padding / 2 + height

        # Start game button
        self.gameButton = self.uiContainer.add_button("Start Game", bx, 0, width, height)
        self.gameButton.rect.y = cy - height * 2 - padding / 2

        # Instructions button
        self.instructionsButton = self.uiContainer.add_button("Instructions", bx, 0, width, height)
        self.instructionsButton.rect.y = self.gameButton.rect.y + dy

        # High Scores button
        self.highScoresButton = self.uiContainer.add_button("High Scores", bx, 0, width, height)
        self.highScoresButton.rect.y = self.instructionsButton.rect.y + dy

        # About button
        self.aboutButton = self.uiContainer.add_button("About", bx, 0, width, height)
        self.aboutButton.rect.y = self.highScoresButton.rect.y + dy

        # Set button colors
        baseColor = (0, 0, 0)
        hoverColor = (255, 255, 255)
        clickColor = (128, 128, 128)
        hoverFill = 1
        for button in self.uiContainer.components:
            if isinstance(button, Button):
                button.baseColour = baseColor
                button.hoverColour = hoverColor
                button.clickColour = clickColor
                button.hoverFill = hoverFill

    def start(self):
        pass

   
    def update(self):
        if self.gameButton.was_pressed():
            self.stateManager.switchGameState("GameScreen")
        if self.instructionsButton.was_pressed():
            self.stateManager.switchGameState("InstructionsScreen")
        if self.highScoresButton.was_pressed():
            self.stateManager.switchGameState("HighScoreScreen")
        if self.aboutButton.was_pressed():
            self.stateManager.switchGameState("AboutScreen")

        self.uiContainer.update()
    
    def draw(self):
        # UI needs to be drawn LAST
        self.uiContainer.draw()
    
    def final(self):
        pass