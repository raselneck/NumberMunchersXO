import pygame, sys
from fraction import *
from gamestatemanager import *
from input import xo_input
from pygame.locals import *
from exit import exit_game
import os

from Gamestates.mainscreen import MainScreen
from Gamestates.gamescreen import GameScreen
from Gamestates.instructionsscreen import InstructionsScreen
from Gamestates.highscorescreen import HighScoreScreen
from Gamestates.aboutscreen import AboutScreen
from Gamestates.winscreen import WinScreen

from highscoremanager import *

if sys.platform != "win32":
    from gi.repository import Gtk

class Game:
    """
    Defines the overall game.
    """

    def __init__(self):
        self.paused = False

        # Get desktop information
        self.screen_info = pygame.display.Info()

        # Make the game full screen
        window_flags = FULLSCREEN | DOUBLEBUF | NOFRAME
        window_size = (self.screen_info.current_w, self.screen_info.current_h)
        if sys.platform == "win32":
            window_size = (1200, 900)
            window_flags = DOUBLEBUF | NOFRAME
        self.window = self.create_window(window_size, window_flags, 32, "PyGame Test")
        self.clear_color = (0, 0, 0)

        # Add GameStates here
        # Format for game states is any class with a
        # Start, Update, Draw, and Final function
        # These are automatically called
        self.stateManager = GameStateManager()
        self.stateManager.addGameState("MainScreen", MainScreen(self.stateManager, self.window))
        self.stateManager.addGameState("GameScreen", GameScreen(self.stateManager, highScoreManager, self.window))
        self.stateManager.addGameState("AboutScreen", AboutScreen(self.stateManager, self.window))
        self.stateManager.addGameState("InstructionsScreen", InstructionsScreen(self.stateManager, self.window))
        self.stateManager.addGameState("HighScoreScreen", HighScoreScreen(self.stateManager, highScoreManager, self.window))
        self.stateManager.addGameState("WinScreen", WinScreen(self.stateManager, self.window, highScoreManager))

        # Prevent extra states being added after game starts
        self.stateManager.gameRunning = True

        # Setup a clock for managing the frame rate
        self.clock = pygame.time.Clock()

    def set_paused(self, paused):
        self.paused = paused

    def create_window(self, resolution = (100, 100), flags = 0, depth = 32, title = "Hello, world!"):
        """
        Creates the pygame window

        :param resolution: The window resolution.
        :param flags: The window flags.
        :param depth: The window depth-bit count.
        :param title: The window title.
        :return: The window.
        """
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        window = pygame.display.set_mode(resolution, flags, depth)
        pygame.display.set_caption(title)
        return window

    def run(self):
        # Run the game loop
        while self.stateManager.gameRunning:
            # Run the GTK message pump
            if sys.platform != "win32":
                while gtk.events_pending():
                    gtk.main_iteration()

            # Run the message pump
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.stateManager.gameRunning = False
                #if event.type == KEYDOWN:
                #    if event.key == K_ESCAPE:
                #        stateManager.gameRunning = False

            if not self.paused:
                # Check if we changed states
                # Trigger start function
                if self.stateManager.switchTriggered is True:
                    self.stateManager.switchTriggered = False
                    self.stateManager.currentGameState = self.stateManager.stateToSwitchTo
                    self.stateManager.currentGameState.start()
                    self.stateManager.stateToSwitchTo = None

                # Game logic
                xo_input.update()
                self.stateManager.getCurrentGameState().update()

            # Draw game
            self.window.fill(self.clear_color)
            self.stateManager.getCurrentGameState().draw()

            # Check if state was changed
            # Trigger final function
            if self.stateManager.switchTriggered is True:
                self.stateManager.currentGameState.final()

            pygame.display.update()
            self.clock.tick(30)

        exit_game(1)

# This function is called when the game is run directly from the command line
def main():
    # Initialize pygame
    passed, failed = pygame.init()
    if (failed > 0):
        print("One or more pygame submodules failed to initialize")
        exit_game(-1, None)

    # Run the game
    game = Game()
    game.run()

if __name__ == '__main__':
    main()
