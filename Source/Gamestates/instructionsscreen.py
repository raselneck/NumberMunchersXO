import pygame, sys
from input import xo_input
from UI.uicontainer import UIContainer
from UI.button import Button
from messagewindow import MessageWindow

class InstructionsScreen:

    def __init__(self, manager, screen):
        self.stateManager = manager
        self.window = screen

        self.uiContainer = UIContainer(self.window)
        self.uiContainer.verticalStride = 0

        self.screenInfo = pygame.display.Info()

        self.titleFont = pygame.font.SysFont("monospace", 75, bold=True)
        self.scoreFont = pygame.font.SysFont("monospace", 45)
        self.textColour = (128, 128, 128)

        self.initiateReset = False

        # Create the message box
        centerX = self.screenInfo.current_w / 2
        centerY = self.screenInfo.current_h / 2

        # Button sizes
        width = 170
        height = 40

        # Back button
        self.backButton = self.uiContainer.add_button("Back")
        self.backButton.rect = pygame.Rect(
            (110 - (width / 2), self.screenInfo.current_h - 50 - (height / 2), width, height))

        self.backButton.baseColour = (0, 0, 0)

        hoverFill = 1
        hoverColour = (255, 255, 255)
        clickColour = (128, 128, 128)
        for button in self.uiContainer.components:
            if isinstance(button, Button):
                button.hoverColour = hoverColour
                button.clickColour = clickColour
                button.hoverFill = hoverFill
                button.font = pygame.font.SysFont("monospace", 30)
        pass

    def start(self):
        pass
        
    def update(self):
        if xo_input.escape or self.backButton.was_pressed():
            self.stateManager.switchGameState("MainScreen")

        self.uiContainer.update()
    
    def draw(self):
        self.uiContainer.draw()

        self.drawTextCentered("Instructions", self.titleFont, 0, -300)
        self.drawTextCentered("To play Number Munchers you have ", self.scoreFont, 0, -250)
        self.drawTextCentered("to \"munch\" on the multiples of", self.scoreFont, 0, -200)
        self.drawTextCentered("the fraction shown at the top ", self.scoreFont, 0, -150)
        self.drawTextCentered("of the screen until you get them", self.scoreFont, 0, -100)
        self.drawTextCentered(" all. When all of the fraction", self.scoreFont, 0, -50)
        self.drawTextCentered(" multiples on the screen are ", self.scoreFont, 0, 0)
        self.drawTextCentered(" munched on a new fraction and ", self.scoreFont, 0, 50)
        self.drawTextCentered("board will be made. You will keep ", self.scoreFont, 0, 100)
        self.drawTextCentered("playing until you get three wrong ", self.scoreFont, 0, 150)
        self.drawTextCentered("fractions in a level. The higher ", self.scoreFont, 0, 200)
        self.drawTextCentered("your score the better. ", self.scoreFont, 0, 250)
        pass
    
    def final(self):
        pass

    def drawTextCentered(self, text, font, offsetX, offsetY):
        label = font.render(text, 1, self.textColour)
        text_width, text_height = font.size(text)
        self.window.blit(label, ((self.screenInfo.current_w/2) - (text_width/2) + offsetX, (self.screenInfo.current_h/2) - (text_height/2) + offsetY))