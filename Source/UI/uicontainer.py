import pygame
from button import Button

class UIContainer(object):
    """
    Defines a container for all UI components.
    """
    __components = []
    __selectedComponent = None
    __window = None

    def __init__(self, window):
        """
        Creates a new UI container.
        """
        self.__window = window

    def add_button(self):
        """
        Adds a button to this container.

        :return: The button.
        """
        button = Button(self)
        self.__components.append(button)
        return button

    def get_window(self):
        """
        Gets this container's window.

        :return: The window.
        """
        return self.__window

    def update(self):
        """
        Updates all of the UI components in this container.
        """
        for component in self.__components:
            component.update()

    def draw(self):
        """
        Draws all of the UI components in this container.
        """
        for component in self.__components:
            component.draw()
