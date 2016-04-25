import pygame, sys
import Gamestates.mainscreen

class GameStateManager:
	
	def __init__(self):
		self.gameStatesIndex = {}
		self.totalGameStates = 0;
	
		self.currentGameState = None;
		
		self.switchTriggered = False;
		self.stateToSwitchTo = None;
		
	def getCurrentGameState(self):
		return self.currentGameState
		
	# Signals a switch for the next update cycle
	def switchGameState(self, string):
		self.stateToSwitchTo = self.gameStatesIndex[string]
		self.switchTriggered = True
	
	# Adds a reference to a state object
	def addGameState(self, string, obj):
		self.gameStatesIndex[string] = obj
		self.totalGameStates += 1
		
		# Set the first state added to current
		if self.stateToSwitchTo == None:
			self.switchTriggered = True
			self.stateToSwitchTo = obj
	
	def __str__(self):
		s = 'Game States:\n'
		
		for key, value in self.gameStatesIndex.iteritems():
			s += "%s %s\n" % (key, value)
			
		return s