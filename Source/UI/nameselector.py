import pygame
from uicomponent import UIComponent
from input import xo_input

class NameSelector(UIComponent):
    """
    Defines a name selector UI component.
    """

    __MAX_NAME_LENGTH = 12
    __CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '!', '?', ' ']

    def __init__(self, container):
        """
        Creates a new button.

        :param container: The parent UI container.
        """
        UIComponent.__init__(self, container)
        self.__name = "".ljust(NameSelector.__MAX_NAME_LENGTH, ' ')
        self.__namePosition = 0
        self.__charPosition = 0
        self.__font = pygame.font.SysFont("monospace", 20)
        self.__char_w, self.__char_h = self.__font.size("M")

    def getName(self):
        """
        Gets the entered name.
        """
        return self.__name

    def setName(self, name):
        """
        Sets the new name.
        :param name: The new name.
        :return:
        """
        self.__name = ""
        length = min(len(name), NameSelector.__MAX_NAME_LENGTH)
        if length == 0:
            return
        elif length == 1:
            self.__name[0] = name[0]
        else:
            for i in range(0, length):
                self.__name += name[i]
        self.__name = self.__name.ljust(NameSelector.__MAX_NAME_LENGTH, ' ')
        self.__charPosition = NameSelector.__CHARACTERS.index(self.__name[0])

    def __setNameCharAtIndex(self, index, char):
        newName = ""
        for i in range(0, len(self.__name)):
            if i == index:
                newName += char
            else:
                newName += self.__name[i]
        self.__name = newName.ljust(NameSelector.__MAX_NAME_LENGTH, ' ')

    def update(self):
        # If they pressed X, set the current character and move to the next
        if xo_input.btn_cross:
            self.__name[self.__namePosition] = NameSelector.__CHARACTERS[self.__charPosition]
            if self.__namePosition < NameSelector.__MAX_NAME_LENGTH:
                self.__namePosition += 1
        # If they press left, go to the previous character
        if xo_input.dpad_left and self.__namePosition > 0:
            self.__namePosition -= 1
            self.__charPosition = NameSelector.__CHARACTERS.index(self.__name[self.__namePosition])
        # If they press left, go to the previous character
        if xo_input.dpad_right and self.__namePosition < NameSelector.__MAX_NAME_LENGTH - 1:
            self.__namePosition += 1
            self.__charPosition = NameSelector.__CHARACTERS.index(self.__name[self.__namePosition])
        # If they press up, go to the previous character
        if xo_input.dpad_up:
            self.__charPosition -= 1
            if self.__charPosition < 0:
                self.__charPosition = len(NameSelector.__CHARACTERS) - 1
            self.__setNameCharAtIndex(self.__namePosition, NameSelector.__CHARACTERS[self.__charPosition])
        # If they press down, go to the next character
        if xo_input.dpad_down:
            self.__charPosition += 1
            if self.__charPosition >= len(NameSelector.__CHARACTERS):
                self.__charPosition = 0
            self.__setNameCharAtIndex(self.__namePosition, NameSelector.__CHARACTERS[self.__charPosition])

    def draw(self):
        surface = self.container.get_window()
        x = self.rect.left + 50
        y = self.rect.top + 50
        for i in range(0, len(self.__name)):
            color = (255, 255, 255)
            if i == self.__namePosition:
                color = (255, 0, 0)
                underline = pygame.Rect(x, y + self.__char_h + 2, self.__char_w, 3)
                pygame.draw.rect(surface, color, underline)
            label = self.__font.render(self.__name[i], True, color)
            surface.blit(label, (x, y))
            x += self.__char_w
