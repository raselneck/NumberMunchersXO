import pygame, sys

class GameScreen:

	def __init__(self, manager):
		self.stateManager = manager
		pass

	def start(self):
		print "Start GameScreen"
		
	def update(self):
		self.stateManager.switchGameState("MainScreen")
		print "update"
	
	def draw(self):
		print "draw"
	
	def final(self):
		print "final"