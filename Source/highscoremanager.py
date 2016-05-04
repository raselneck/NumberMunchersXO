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
    
    def getCurrentHighScores(self):
        '''
        Returns a Dict of all the current high scores with keys 'first' through 'tenth'
        '''
        return self.high_scores
    
    def compareHighScores(self, new_score):
        '''
        Returns true if the given score would be in the high score list
        
        :param new_score: The score to test
        '''
        foundNewScore = False
        
        for d in self.high_scores:
            if self.high_scores[d]["score"] < new_score:
                foundNewScore = True
                
        return foundNewScore
        
    def addHighScore(self, new_score, name):
        '''
        Adds given score and name to high score list if it would fit
        
        :param new_score: Score to add to new entry
        :param name: Name to add to new entry
        '''
        #Find lowest value, then shift down up to new value
        newKey = ""
        
        if self.high_scores["tenth"]["score"] < new_score:
            newKey = "tenth"
        if self.high_scores["ninth"]["score"] < new_score:
            self.high_scores["tenth"]["score"] = self.high_scores["ninth"]["score"]
            self.high_scores["tenth"]["name"] = self.high_scores["ninth"]["name"]
            newKey = "ninth"
        if self.high_scores["eighth"]["score"] < new_score:
            self.high_scores["ninth"]["score"] = self.high_scores["eighth"]["score"]
            self.high_scores["ninth"]["name"] = self.high_scores["eighth"]["name"]
            newKey = "eighth"
        if self.high_scores["seventh"]["score"] < new_score:
            self.high_scores["eighth"]["score"] = self.high_scores["seventh"]["score"]
            self.high_scores["eighth"]["name"] = self.high_scores["seventh"]["name"]
            newKey = "seventh"
        if self.high_scores["sixth"]["score"] < new_score:
            self.high_scores["seventh"]["score"] = self.high_scores["sixth"]["score"]
            self.high_scores["seventh"]["name"] = self.high_scores["sixth"]["name"]
            newKey = "sixth"
        if self.high_scores["fifth"]["score"] < new_score:
            self.high_scores["sixth"]["score"] = self.high_scores["fifth"]["score"]
            self.high_scores["sixth"]["name"] = self.high_scores["fifth"]["name"]
            newKey = "fifth"
        if self.high_scores["fourth"]["score"] < new_score:
            self.high_scores["fifth"]["score"] = self.high_scores["fourth"]["score"]
            self.high_scores["fifth"]["name"] = self.high_scores["fourth"]["name"]
            newKey = "fourth"
        if self.high_scores["third"]["score"] < new_score:
            self.high_scores["fourth"]["score"] = self.high_scores["third"]["score"]
            self.high_scores["fourth"]["name"] = self.high_scores["third"]["name"]
            newKey = "third"
        if self.high_scores["second"]["score"] < new_score:
            self.high_scores["third"]["score"] = self.high_scores["second"]["score"]
            self.high_scores["third"]["name"] = self.high_scores["second"]["name"]
            newKey = "second"
        if self.high_scores["first"]["score"] < new_score:
            self.high_scores["second"]["score"] = self.high_scores["first"]["score"]
            self.high_scores["second"]["name"] = self.high_scores["first"]["name"]
            newKey = "first"
        
        # Replace score if new score is in the criteria
        if newKey != "":
            self.high_scores[newKey]["score"] = new_score
            self.high_scores[newKey]["name"] = name

        pass
        
    def saveHighScores(self):
        '''
        Saves current high scores to a json file name '.highscores'
        '''
        with open("../.highscores", "w") as f:
            json.dump({ "highscores" : self.high_scores, "default_highscores" : self.default_high_scores }, f)
        pass
        
    def resetHighScores(self):
        '''
        Resets current high scores to the values in 'default_highscores'
        '''
        for key in self.high_scores:
            self.high_scores[key] = self.default_high_scores[key]
        pass
    
    def __str__(self):
        return json.dumps(self.data, sort_keys=True, indent=4, separators=(",", ": "))