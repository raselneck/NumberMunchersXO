import pygame
from uicomponent import UIComponent
from input import xo_input

class Button(UIComponent):
    """
    Defines a UI button.
    """
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
        mx = xo_input.mouse_x
        my = xo_input.mouse_y

        # Check if the mouse is hovering over us
        bAlignedX = (mx >= self.rect.left) and (mx <= self.rect.right)
        bAlignedY = (my >= self.rect.top) and (my <= self.rect.bottom)
        self.__isHovering = bAlignedX and bAlignedY

        # Check if the mouse is down on us
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
            pygame.draw.rect(self.container.get_window(), (0, 255, 0), self.rect, 0)
