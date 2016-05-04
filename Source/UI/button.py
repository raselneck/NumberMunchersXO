import pygame
from uicomponent import UIComponent
from input import xo_input

class Button(UIComponent):
    """
    Defines a UI button.
    """

    def __init__(self, container):
        """
        Creates a new button.

        :param container: The parent UI container.
        """
        UIComponent.__init__(self, container)
        self.selectable = True
        self.__canBeDown = True
        self.__isHovering = False
        self.__isDown = False
        self.__wasPressed = False
        self.__simulatePress = False

        self.font = pygame.font.SysFont("monospace", 15)
        self.text = "Default String"
        self.textColour = (255, 255, 255)
        
        self.baseColour = (255, 0, 0)
        self.hoverColour = (0, 255, 0)
        self.clickColour = (0, 0, 255)
        
        # 0 For filled block colour
        # 1 For outline of colour
        self.baseFill = 0
        self.hoverFill = 0
        self.clickFill = 0

    def disable(self):
        """
        Disables this button.
        """
        UIComponent.disable(self)
        self.__canBeDown = False
        self.__isHovering = False
        self.__isDown = False
        self.__wasPressed = False
        self.__simulatePress = False

    def was_pressed(self):
        """
        Checks to see if this button was pressed.

        :return: True if the button was pressed, false if not.
        """
        return self.__wasPressed

    def simulate_press(self):
        """
        Simulates this button being pressed.
        """
        self.__simulatePress = True

    def update(self):
        """
        Updates this button.
        """

        # Ensure people can't drag over the button with the mouse button already down
        if not self.__isHovering:
            self.__canBeDown = True
            if xo_input.mouse_left_down:
                self.__canBeDown = False
        else:
            if not xo_input.mouse_left_down:
                self.__canBeDown = True

        # Check if the mouse is hovering over us
        #mouseX = xo_input.mouse_x
        #mouseY = xo_input.mouse_y
        #bAlignedX = (mouseX >= self.rect.left) and (mouseX <= self.rect.right)
        #bAlignedY = (mouseY >= self.rect.top) and (mouseY <= self.rect.bottom)
        #self.__isHovering = bAlignedX and bAlignedY

        # Check if the mouse is down on us
        if self.__canBeDown:
            # Check if we were pressed
            if self.__isDown: # and xo_input.mouse_left_up:
                self.__wasPressed = True
            else:
                self.__wasPressed = False
            # Update actual down state
            self.__isDown = self.__isHovering # and xo_input.mouse_left_down

        # If we're simulating a press, just set our flag to true
        if self.__simulatePress:
            self.__simulatePress = False
            self.__wasPressed = True

    def draw(self):
        """
        Draws this button.
        """
        if self.__isDown:
            pygame.draw.rect(self.container.get_window(), self.clickColour, self.rect, self.clickFill)
        elif self.__isHovering or self.selected:
            pygame.draw.rect(self.container.get_window(), self.hoverColour, self.rect, self.hoverFill)
        else:
            pygame.draw.rect(self.container.get_window(), self.baseColour, self.rect, self.baseFill)
        
        label = self.font.render(self.text, 1, self.textColour)
        text_width, text_height = self.font.size(self.text)
        self.container.get_window().blit(label, (self.rect.centerx - (text_width/2), self.rect.centery - (text_height/2)))
