from pygame import *

class Input:
    """
    Defines an easy wrapper for PyGame to get input from the XO.
    """

    def __init__(self):
        self.dpad_up = False
        self.dpad_down = False
        self.dpad_left = False
        self.dpad_right = False
        self.btn_circle = False
        self.btn_cross = False
        self.btn_square = False
        self.btn_check = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_left_down = False
        self.mouse_left_up = False
        self.mouse_left_pressed = False
        self.mouse_right_down = False
        self.mouse_right_up = False
        self.mouse_right_pressed = False
        self.escape = False
        self.__old_dpad_up = False
        self.__old_dpad_down = False
        self.__old_dpad_left = False
        self.__old_dpad_right = False
        self.__old_btn_circle = False
        self.__old_btn_cross = False
        self.__old_btn_square = False
        self.__old_btn_check = False
        self.__old_escape = False

    def update(self):
        """
        Updates all input values.
        """

        # Update buttons
        pressed = key.get_pressed()
        self.dpad_up            = not pressed[K_KP8] and self.__old_dpad_up
        self.dpad_down          = not pressed[K_KP2] and self.__old_dpad_down
        self.dpad_left          = not pressed[K_KP4] and self.__old_dpad_left
        self.dpad_right         = not pressed[K_KP6] and self.__old_dpad_right
        self.btn_circle         = not pressed[K_KP9] and self.__old_btn_circle
        self.btn_cross          = not pressed[K_KP3] and self.__old_btn_cross
        self.btn_square         = not pressed[K_KP7] and self.__old_btn_square
        self.btn_check          = not pressed[K_KP1] and self.__old_btn_check
        self.escape             = not pressed[K_ESCAPE] and self.__old_escape
        self.__old_dpad_up      = pressed[K_KP8]
        self.__old_dpad_down    = pressed[K_KP2]
        self.__old_dpad_left    = pressed[K_KP4]
        self.__old_dpad_right   = pressed[K_KP6]
        self.__old_btn_circle   = pressed[K_KP9]
        self.__old_btn_cross    = pressed[K_KP3]
        self.__old_btn_square   = pressed[K_KP7]
        self.__old_btn_check    = pressed[K_KP1]
        self.__old_escape       = pressed[K_ESCAPE]

        # Update mouse position
        position = mouse.get_pos()
        self.mouse_x = position[0]
        self.mouse_y = position[1]

        # Update mouse buttons
        pressed = mouse.get_pressed()
        self.mouse_left_pressed  = not pressed[0] and self.mouse_left_down
        self.mouse_left_down     = pressed[0]
        self.mouse_left_up       = not pressed[0]
        self.mouse_right_pressed = not pressed[2] and self.mouse_right_down
        self.mouse_right_down    = pressed[2]
        self.mouse_right_up      = not pressed[2]

# The global XO input value
xo_input = Input()
