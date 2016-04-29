import pygame, sys
from fraction import Fraction
from gamestatemanager import *
from input import xo_input
from pygame.locals import *

from Gamestates.mainscreen import MainScreen
from Gamestates.gamescreen import GameScreen
from Gamestates.instructionsscreen import InstructionsScreen
from Gamestates.highscorescreen import HighScoreScreen
from Gamestates.aboutscreen import AboutScreen


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


# Test two fractions
fracA = Fraction(3, 9)
fracB = Fraction(1, 3)
assert fracA == fracB



# Initialize pygame
passed, failed = pygame.init()
if (failed > 0):
    print("One or more pygame submodules failed to initialize")
    exit_game(-1)

# Get desktop information
screen_info = pygame.display.Info()

# Make the game full screen
window_flags = FULLSCREEN | DOUBLEBUF | NOFRAME
window_size = (screen_info.current_w, screen_info.current_h)
window = create_window(window_size, window_flags, 32, "PyGame Test")
clear_color = (0, 0, 0)


# Add GameStates here
# Format for game states is any class with a
# Start, Update, Draw, and Final function
# These are automatically called
stateManager = GameStateManager()
stateManager.addGameState("MainScreen", MainScreen(stateManager, window))
stateManager.addGameState("GameScreen", GameScreen(stateManager, window))
stateManager.addGameState("AboutScreen", AboutScreen(stateManager, window))
stateManager.addGameState("InstructionsScreen", InstructionsScreen(stateManager, window))
stateManager.addGameState("HighScoreScreen", HighScoreScreen(stateManager, window))

# Prevent extra states being added after game starts
stateManager.gameRunning = True

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
        stateManager.switchTriggered = False
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
