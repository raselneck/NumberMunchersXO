import pygame

class UIComponent:
    """
    The base class for all UI components.
    """
    rect = pygame.Rect(0, 0, 0, 0)
    selectable = False
    container = None

    def __init__(self, container):
        """
        Creates a new UI component.

        :param container: The parent UI container
        """
        self.container = container

    def update(self):
        """
        Updates this component.
        """

    def draw(self):
        """
        Draws this component.
        """
