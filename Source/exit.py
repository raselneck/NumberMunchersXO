import sys, pygame
from highscoremanager import *

def exit_game(code):
    """
    Exits the game with the given status code.

    :param code: The exit code.
    """
    highScoreManager.saveHighScores()
    pygame.quit()
    sys.exit(code)
