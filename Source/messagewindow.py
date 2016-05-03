import pygame, sys, textwrap
from input import xo_input
from UI.uicontainer import UIContainer

class MessageWindow:
    
    def __init__(self, window, message, width, height, x, y):
        self.message = message
        self.window = window
        
        self.width = width
        self.height = height
        self.X = x
        self.Y = y
        self.topleft = [x - width/2, y - height/2]
        
        self.uiContainer = UIContainer(self.window)
        
        self.baseColour = (16, 16, 16)
        self.borderColour = (255, 255, 255)
        
        self.textColour = (128, 128, 128)
        self.textFont = pygame.font.SysFont("monospace", 20)
        
        self.padding = 20;
        pass
    
    def addButton(self, text, pos, size):
        button = self.uiContainer.add_button()
        button.rect = pygame.Rect([self.X + pos[0], self.Y + pos[1]], size)
        button.text = text
        return button
    
    def update(self):
        # Update the UI
        self.uiContainer.update()
        pass
        
    def draw(self):
        # Draw the background for the window
        pygame.draw.rect(self.window, self.baseColour, pygame.Rect(self.topleft, (self.width, self.height)), 0)
        
        # Draw the border for the window
        pygame.draw.rect(self.window, self.borderColour, pygame.Rect(self.topleft, (self.width, self.height)), 1)
        
        # Render the message
        self.drawText(self.message, self.textFont, 0, 0)
        
        # Draw the UI
        self.uiContainer.draw()
        pass
        
    def drawText(self, text, font, offsetX, offsetY):
        # Only works with a fixed-width font
        # Python text-wrap takes a character width for wrapping, not a pixel width
        # Which is dumb
        charWidth = (self.width - self.padding)/(font.size('a')[0]) 
        wrappedText = textwrap.wrap(text, charWidth)
        
        counter = 0;
        for line in wrappedText:
            label = font.render(line, 1, self.textColour)
            text_width, text_height = font.size(line)
            self.window.blit(label, ((self.width/2) - (text_width/2) + offsetX + self.topleft[0], self.padding - (text_height/2) + offsetY + self.topleft[1] + (counter * text_height)))
            counter += 1