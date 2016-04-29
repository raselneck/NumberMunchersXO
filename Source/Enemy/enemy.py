import pygame, sys
import time
import random

random.seed(calendar.timegm(time.gmtime()))
MOVEAMOUNT = 50

class Enemy:
    infoObject = pygame.display.Info()
	posx: infoObject.current_w / 2
    posy: infoObject.current_h / 2
    direction: "up"
	visible: true
	start = 0;
	currtime = 0;
	
    def __init__ (self):
        start = time.time();
    def spawn(self){
		dirRand = random.randint(0, 3)
		slotRand = random.randint(0, 4)
	    if dirRand == 0:
            direction = "up"
			posy = infoObject.current_h * .2
			posx = infoObject.current_w * (slotRand/4);
		if dirRand == 1:
            direction = "right"
			posx = infoObject.current_w * .2
			posy = infoObject.current_h * (slotRand/4);
	    if dirRand == 2:
            direction = "left"
			posx = infoObject.current_w * .8
			posy = infoObject.current_h * (slotRand/4);
		if dirRand == 3:
            direction = "down"
			posy = infoObject.current_h * .8
			posx = infoObject.current_w * (slotRand/4);
	}
	def update(self){
		currtime = time.time();
		if currtime - starttime > 10:
		     start = time.time();
			 move();
	}
	def draw(self):
         pygame.draw.circle(self.container.get_window(), (posx, posy), (255, 0, 0), 0)
    def move(self):
        if direction == "up":
		    posy += MOVEAMOUNT
        if direction == "right":
		    posx += MOVEAMOUNT
		if direction == "left":
		    posx -= MOVEAMOUNT
		if direction == "down":
		    posy -= MOVEAMOUNT