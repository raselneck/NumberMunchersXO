import pygame
from input import xo_input
from UI.uicontainer import UIContainer


class MainScreen:
    """
    Defines the main menu screen
    """
    def __init__(self, manager, screen):
        self.stateManager = manager
        self.window = screen

        self.uiContainer = UIContainer(self.window)
        
        self.screenInfo = pygame.display.Info()

        self.gameButton = None
        self.instructionsButton = None
        self.highScoresButton = None
        self.aboutButton = None

        pass

    def start(self):
        # Button sizes
        width = 150
        height = 20

        # Start game button
        self.gameButton = self.uiContainer.add_button()
        self.gameButton.rect = pygame.Rect((self.screenInfo.current_w / 2) - (width / 2),
                                           (self.screenInfo.current_h / 2) - 60 - (height / 2), width, height)
        self.gameButton.text = "Start Game"

        # Instructions button
        self.instructionsButton = self.uiContainer.add_button()
        self.instructionsButton.rect = pygame.Rect((self.screenInfo.current_w / 2) - (width / 2),
                                                   (self.screenInfo.current_h / 2) - 30 - (height / 2), width, height)
        self.instructionsButton.text = "Instructions"

        # High Scores button
        self.highScoresButton = self.uiContainer.add_button()
        self.highScoresButton.rect = pygame.Rect((self.screenInfo.current_w / 2) - (width / 2),
                                                 (self.screenInfo.current_h / 2) - (height / 2), width, height)
        self.highScoresButton.text = "High Scores"

        # About button
        # High Scores button
        self.aboutButton = self.uiContainer.add_button()
        self.aboutButton.rect = pygame.Rect((self.screenInfo.current_w / 2) - (width / 2),
                                            (self.screenInfo.current_h / 2) + 30 - (height / 2), width, height)
        self.aboutButton.text = "About"
        
        self.gameButton.baseColour = self.instructionsButton.baseColour = self.highScoresButton.baseColour = self.aboutButton.baseColour = (0, 0, 0)
        self.gameButton.hoverColour = self.instructionsButton.hoverColour = self.highScoresButton.hoverColour = self.aboutButton.hoverColour = (255, 255, 255)
        self.gameButton.clickColour = self.instructionsButton.clickColour = self.highScoresButton.clickColour = self.aboutButton.clickColour = (128, 128, 128)
        
        self.gameButton.hoverFill = self.instructionsButton.hoverFill = self.highScoresButton.hoverFill = self.aboutButton.hoverFill = 1

        self.gameButton.baseColour = self.instructionsButton.baseColour = self.highScoresButton.baseColour = self.aboutButton.baseColour = (0, 0, 0)
        self.gameButton.hoverColour = self.instructionsButton.hoverColour = self.highScoresButton.hoverColour = self.aboutButton.hoverColour = (255, 255, 255)
        self.gameButton.clickColour = self.instructionsButton.clickColour = self.highScoresButton.clickColour = self.aboutButton.clickColour = (128, 128, 128)

        self.gameButton.hoverFill = self.instructionsButton.hoverFill = self.highScoresButton.hoverFill = self.aboutButton.hoverFill = 1
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