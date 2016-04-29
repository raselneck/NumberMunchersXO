import pygame
from uicomponent import UIComponent
from input import xo_input

class Button(UIComponent):
    """
    Defines a UI button.
    """
    __canBeDown = True
    __isHovering = False
    __isDown = False
    __wasPressed = False

    def __init__(self, container):
        """
        Creates a new button.

        :param container: The parent UI container.
        """
        UIComponent.__init__(self, container)
        self.selectable = True

        self.font = pygame.font.SysFont("monospace", 15)
        self.text = "Default String"

    def was_pressed(self):
        """
        Checks to see if this button was pressed.

        :return: True if the button was pressed, false if not.
        """
        return self.__wasPressed

    def update(self):
        """
        Updates this button.
        """
        mouseX = xo_input.mouse_x
        mouseY = xo_input.mouse_y

        # Ensure people can't drag over the button with the mouse button already down
        if not self.__isHovering:
            self.__canBeDown = True
            if xo_input.mouse_left_down:
                self.__canBeDown = False
        else:
            if not xo_input.mouse_left_down:
                self.__canBeDown = True

        # Check if the mouse is hovering over us
        bAlignedX = (mouseX >= self.rect.left) and (mouseX <= self.rect.right)
        bAlignedY = (mouseY >= self.rect.top) and (mouseY <= self.rect.bottom)
        self.__isHovering = bAlignedX and bAlignedY

        # Check if the mouse is down on us
        if self.__canBeDown:
            # Check if we were pressed
            if self.__isDown and xo_input.mouse_left_up:
                self.__wasPressed = True
            else:
                self.__wasPressed = False

            # Update actual down state
            self.__isDown = self.__isHovering and xo_input.mouse_left_down

    def draw(self):
        """
        Draws this button.
        """
        if self.__isDown:
            pygame.draw.rect(self.container.get_window(), (255, 0, 0), self.rect, 0)
        elif self.__isHovering:
            pygame.draw.rect(self.container.get_window(), (0, 0, 255), self.rect, 0)
        else:
            pygame.draw.rect(self.container.get_window(), (0, 255, 0), self.rect, 0)\
        
        label = self.font.render(self.text, 1, (255, 255, 255))
        text_width, text_height = self.font.size(self.text)
        self.container.get_window().blit(label, (self.rect.centerx - (text_width/2), self.rect.centery - (text_height/2)))
