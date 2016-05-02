import pygame, sys
import json

class HighScoreManager:
    
    def __init__(self):
        # Read in the file
        with open("../.highscores", "r") as f:
            self.data = json.load(f)
        
        # The default section is just used to reset scores if the user chooses
        self.high_scores = self.data["highscores"]
        self.default_high_scores = self.data["default_highscores"]
        
        pass
        
    def addHighScore(self, new_score):
        pass
        
    def saveHighScores(self)
        pass
        
    def resetHighScores(self)
        pass
    
    def __str__(self):
        return json.dumps(self.high_scores, sort_keys=True, indent=4, separators=(",", ": "))