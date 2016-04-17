import pygame, sys
from Expressions import *
from pygame.locals import *

def exit_game(code):
    """
    Exits the game with the given status code.

    :param code: The exit code.
    """
    pygame.quit()
    sys.exit(code)

def create_window(resolution = (100, 100), flags = 0, depth = 32, title = "Hello, world!"):
    """
    Creates the pygame window

    :param resolution: The window resolution.
    :param flags: The window flags.
    :param depth: The window depth-bit count.
    :param title: The window title.
    :return: The window.
    """
    window = pygame.display.set_mode(resolution, flags, depth)
    pygame.display.set_caption(title)
    return window

# Initialize pygame
passed, failed = pygame.init()
if (failed > 0):
    print("One or more pygame submodules failed to initialize")
    exit_game(-1)

# Create the pygame window
window_size = (1280, 768)
window = create_window(window_size, 0, 32, "PyGame Test")
clear_color = (100, 149, 247)

for x in range(1, 30):
    frac = frac_random()
    print("{0} ({1}) == {2}".format(frac, frac.can_be_reduced(), frac.get_equal_fraction()))

# Run the game loop
is_running = True
while (is_running):
    # Run the message pump
    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                is_running = False
    window.fill(clear_color)
    ### TODO - Update game logic
    ### TODO - Draw game
    pygame.display.update()

exit_game(1)
