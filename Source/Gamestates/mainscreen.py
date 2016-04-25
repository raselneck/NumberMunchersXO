import pygame, sys

class MainScreen:

	def __init__(self, manager):
		self.stateManager = manager
		pass

	def start(self):
		print "Start MainScreen"
		
	def update(self):
		self.stateManager.switchGameState("GameScreen")
		print "update"
	
	def draw(self):
		print "draw"
	
	def final(self):
		print "final"