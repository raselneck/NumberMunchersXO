import pygame
import sys
import time
import random


class Enemy:

    def __init__(self, screen, width, height):
        self.window = screen
        self.start = time.time()
        self.w = width
        self.h = height
        self.infoObject = pygame.display.Info()
        self.posx = 200.0
        self.posy = 200.0
        self.direction = "up"
        self.visible = False
        self.currtime = 0.0
        self.index = 0

    def spawn(self):
        self.dirRand = random.randint(0, 3)
        self.slotRand = random.randint(0, 4)
        if self.dirRand == 0:
            self.direction = "down"
            self.posy = 150
            self.posx = self.slotRand * self.w + 50 + 10 * self.slotRand
            self.index = self.slotRand * 5
        if self.dirRand == 1:
            self.direction = "up"
            self.posy = 150 + self.h * 4 + 40
            self.posx = self.slotRand * self.w + 50 + 10 * self.slotRand
            self.index = self.slotRand * 5 + 4
        if self.dirRand == 2:
            self.direction = "right"
            self.posy = self.slotRand * self.h + 150 + 10 * self.slotRand
            self.posx = 50
            self.index = self.slotRand
        if self.dirRand == 3:
            self.direction = "left"
            self.posy = self.slotRand * self.h + 150 + 10 * self.slotRand
            self.posx = 50 + self.w * 4 + 40
            self.index = self.slotRand + 20


    def update(self, index):
        self.playerI = index
        
        self.currtime = time.time()
        if self.index == self.playerI and self.visible:
            self.visible = False
            return True
        if self.currtime >= self.start  + 2 and self.visible:
            self.start = time.time()
            self.move()

        if self.visible == False and self.currtime >= self.start + 5:
            self.start = time.time()
            self.spawn()
            self.visible = True

        if self.visible == True:
            self.draw()


    def draw(self):
        pygame.draw.rect(self.window, (255, 0, 0), (self.posx, self.posy, self.w, self.h), 0)

    def move(self):
        if self.direction == "up":
            self.posy -= self.h + 10
            self.index -= 1
        if self.direction == "right":
            self.posx += self.w + 10
            self.index += 5
        if self.direction == "left":
            self.posx -= self.w + 10
            self.index -= 5
        if self.direction == "down":
            self.posy += self.h + 10
            self.index += 1
        if self.posy < 150 or self.posx < 50 or self.posy > self.h * 6 or self.posx > self.w * 5:
            self.visible = False;
            self.start = time.time()