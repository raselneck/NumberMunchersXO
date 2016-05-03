import pygame
from button import Button
from input import xo_input

class UIContainer(object):
    """
    Defines a container for all UI components.
    """
    def __init__(self, window):
        """
        Creates a new UI container.
        """
        self.window = window
        self.components = []
        self.selectedComponent = None
        self.selectedIndex = 0
        self.horizontalStride = 1
        self.verticalStride = 1

    def __check_for_first_component(self):
        """
        Checks to see if the first component has been added
        """
        if len(self.components) == 1:
            self.selectedIndex = 0
            self.selectedComponent = self.components[0]
            self.selectedComponent.selected = True

    def add_button(self, title = "DefaultText", x = 0, y = 0, width = 0, height = 0):
        """
        Adds a button to this container.

        :return: The button.
        """
        button = Button(self)
        button.text = title
        button.rect = pygame.Rect(x, y, width, height)
        self.components.append(button)
        self.__check_for_first_component()
        return button

    def get_window(self):
        """
        Gets this container's window.

        :return: The window.
        """
        return self.window

    def update(self):
        """
        Updates all of the UI components in this container.
        """
        if len(self.components) > 0:
            changedSelection = False

            # Modify the selected index based on which DPad key was pressed
            if xo_input.dpad_left:
                self.selectedIndex -= self.horizontalStride
                changedSelection = True
            if xo_input.dpad_right:
                self.selectedIndex += self.horizontalStride
                changedSelection = True
            if xo_input.dpad_up:
                self.selectedIndex -= self.verticalStride
                changedSelection = True
            if xo_input.dpad_down:
                self.selectedIndex += self.verticalStride
                changedSelection = True

            if changedSelection:
                # "Unselect" the last component
                if self.selectedComponent is not None:
                    self.selectedComponent.selected = False

                # Make sure the selected index fits within the bounds of components
                while self.selectedIndex < len(self.components):
                    self.selectedIndex += len(self.components)
                while self.selectedIndex >= len(self.components):
                    self.selectedIndex -= len(self.components)

                # Set the selected component based on the selected index
                self.selectedComponent = self.components[self.selectedIndex]
                self.selectedComponent.selected = True
            else:
                # Here we can check to see if we should simulate the button being pressed
                if xo_input.btn_check and isinstance(self.selectedComponent, Button):
                    self.selectedComponent.simulate_press()

        # Update all of the components
        for component in self.components:
            component.update()

    def draw(self):
        """
        Draws all of the UI components in this container.
        """
        for component in self.components:
            component.draw()
