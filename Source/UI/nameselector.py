import pygame
from uicomponent import UIComponent
from input import xo_input

class NameSelector(UIComponent):
    """
    Defines a name selector UI component.
    """

    __MAX_NAME_LENGTH = 8
    __CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, container):
        """
        Creates a new button.

        :param container: The parent UI container.
        """
        UIComponent.__init__(self, container)
        self.__name = "".rjust(NameSelector.__MAX_NAME_LENGTH, ' ')
        self.__namePosition = 0
        self.__charPosition = 0
        self.__font = pygame.font.SysFont("monospace", 20)

    def getName(self):
        """
        Gets the entered name.
        """
        return self.__name

    def update(self):
        # If they pressed X, set the current character and move to the next
        if xo_input.btn_cross:
            self.__name[self.__namePosition] = NameSelector.__CHARACTERS[self.__charPosition]
            if self.__namePosition < NameSelector.__MAX_NAME_LENGTH:
                self.__namePosition += 1
        # If they press left, go to the previous character
        if xo_input.dpad_left and self.__namePosition > 0:
            self.__namePosition -= 1
        # If they press left, go to the previous character
        if xo_input.dpad_right and self.__namePosition < NameSelector.__MAX_NAME_LENGTH - 1:
            self.__namePosition -= 1
        # If they press up, go to the previous character
        if xo_input.dpad_up:
            self.__charPosition -= 1
            if self.__charPosition < 0:
                self.__charPosition = len(NameSelector.__CHARACTERS) - 1
        # If they press down, go to the next character
        if xo_input.dpad_down:
            self.__charPosition += 1
            if self.__charPosition >= len(NameSelector.__CHARACTERS):
                self.__charPosition = 0

    def draw(self):
        pass
