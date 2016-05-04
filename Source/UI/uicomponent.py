import pygame

class UIComponent:
    """
    The base class for all UI components.
    """

    def __init__(self, container):
        """
        Creates a new UI component.

        :param container: The parent UI container
        """
        self.container = container
        self.selectable = False
        self.selected = False
        self.__enabled = True
        self.rect = pygame.Rect(0, 0, 0, 0)

    def enabled(self):
        return self.__enabled

    def enable(self):
        """
        Enables this component.
        """
        self.__enabled = True

    def disable(self):
        """
        Enables this component.
        """
        self.__enabled = False

    def update(self):
        """
        Updates this component.
        """
        pass

    def draw(self):
        """
        Draws this component.
        """
        pass
