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
    
    gameButton = None
    instructionsButton = None
    highScoresButton = None
    aboutButton = None

    def __init__(self, manager, screen):
        self.stateManager = manager
        self.window = screen

        self.uiContainer = UIContainer(self.window)
        
        width = 150
        height = 20
        # Start game button
        self.gameButton = self.uiContainer.add_button()
        self.gameButton.rect = pygame.Rect(640 - (width/2), 300 - (height/2), width, height)
        self.gameButton.text = "Start Game"
        
        # Instructions button
        self.instructionsButton = self.uiContainer.add_button()
        self.instructionsButton.rect = pygame.Rect(640 - (width/2), 330 - (height/2), width, height)
        self.instructionsButton.text = "Instructions"
        
        # High Scores button
        self.highScoresButton = self.uiContainer.add_button()
        self.highScoresButton.rect = pygame.Rect(640 - (width/2), 360 - (height/2), width, height)
        self.highScoresButton.text = "High Scores"
        
        # About button
        # High Scores button
        self.aboutButton = self.uiContainer.add_button()
        self.aboutButton.rect = pygame.Rect(640 - (width/2), 390 - (height/2), width, height)
        self.aboutButton.text = "About"
        
        self.gameButton.baseColour = self.instructionsButton.baseColour = self.highScoresButton.baseColour = self.aboutButton.baseColour = (0, 0, 0)
        self.gameButton.hoverColour = self.instructionsButton.hoverColour = self.highScoresButton.hoverColour = self.aboutButton.hoverColour = (255, 255, 255)
        self.gameButton.clickColour = self.instructionsButton.clickColour = self.highScoresButton.clickColour = self.aboutButton.clickColour = (128, 128, 128)
        
        self.gameButton.hoverFill = self.instructionsButton.hoverFill = self.highScoresButton.hoverFill = self.aboutButton.hoverFill = 1

        pass

    def start(self):
        pass
   
    def update(self):
        if xo_input.btn_check or self.gameButton.was_pressed():
            self.stateManager.switchGameState("GameScreen")
        if xo_input.btn_check or self.instructionsButton.was_pressed():
            self.stateManager.switchGameState("InstructionsScreen")
        if xo_input.btn_check or self.highScoresButton.was_pressed():
            self.stateManager.switchGameState("HighScoreScreen")
        if xo_input.btn_check or self.aboutButton.was_pressed():
            self.stateManager.switchGameState("AboutScreen")
        self.uiContainer.update()
    
    def draw(self):
        # UI needs to be drawn LAST
        self.uiContainer.draw()
    
    def final(self):
        pass