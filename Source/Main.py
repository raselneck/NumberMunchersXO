import pygame, sys
from Expressions import *
from gamestatemanager import *
from Input import xo_input
from pygame.locals import *

from Gamestates.mainscreen import MainScreen
from Gamestates.gamescreen import GameScreen

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
    print("{0} == {1}".format(frac, frac.get_equal_fraction()))

# Add GameStates here
# Format for game states is any class with a
# Start, Update, Draw, and Final function
# These are automatically called
stateManager = GameStateManager()
stateManager.addGameState("MainScreen", MainScreen(stateManager))
stateManager.addGameState("GameScreen", GameScreen(stateManager))

print stateManager

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
	
	# Check if we changed states
	# Trigger start function
	if stateManager.switchTriggered is True:
		stateManager.switchTriggered = False;
		stateManager.currentGameState = stateManager.stateToSwitchTo
		stateManager.currentGameState.start()
		stateManager.stateToSwitchTo = None
		
    # Game logic
	xo_input.update()
	stateManager.getCurrentGameState().update()
	
    # Draw game
	window.fill(clear_color)
	stateManager.getCurrentGameState().draw()
	
	# Check if state was changed
	# Trigger final function
	if stateManager.switchTriggered is True:
		stateManager.currentGameState.final()
	
    pygame.display.update()

exit_game(1)
