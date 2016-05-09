import pygame, sys
from input import xo_input
from UI.uicontainer import UIContainer
from fraction import *
from copy import deepcopy
from Gamestates.winscreen import *
from enemy import Enemy

class GameScreen:
    def __init__(self, manager, highScoreManager, screen):
        self.stateManager = manager
        self.window = screen
        self.highScoreManager = highScoreManager

        self.uiContainer = UIContainer(self.window)
        self.uiContainer.horizontalStride = 5

        self.titleFont = pygame.font.SysFont("monospace", 45, bold=True)
        self.scoreFont = pygame.font.SysFont("monospace", 30)
        self.textColour = (128, 128, 128)

        self.screenInfo = pygame.display.Info()

        self.addScore = 20
        self.scoreLoss = 5
        self.wrongAnswers = 0
        self.rightAnswers = 0
        self.totalRightAnswers = 0
        self.score = 0
        pass

    def start(self):
        #if not self.initializedUI:
        # Button sizes
        padding = 10
        side_margin = 50
        top_margin = 150
        width = (self.screenInfo.current_w - (padding * 5) - (side_margin * 2)) / 5
        height = (self.screenInfo.current_h - (padding * 5) - (top_margin)) / 5
        self.enemy = Enemy(self.window, width, height)
        self.fractionAnswers = []
        self.equalFractions = []
        self.answer = frac_random()

        for x in range(1, 30):
            self.fractionAnswers.append(frac_random())
            self.equalFractions.append(self.fractionAnswers[x - 1].get_equal_fraction())
            self.right_fracs, self.wrong_fracs = create_goal(self.answer)

        self.totalRightAnswers = len(self.right_fracs)
        print "Looking for {0} fractions...".format(self.totalRightAnswers)

        temp_frac = frac_random()
        temp_right_fracs = deepcopy(self.right_fracs)
        temp_wrong_fracs = deepcopy(self.wrong_fracs)

        for i in range(0, 5):
            for j in range(0, 5):
                if(len(temp_right_fracs) > 0 and len(temp_wrong_fracs) > 0):
                    if(self.array_random(1,2) == 1):
                        rand = self.array_random(0,len(temp_right_fracs)-1)
                        temp_frac = temp_right_fracs[rand]
                        temp_right_fracs.remove(temp_right_fracs[rand])
                    else:
                        rand = self.array_random(0, len(temp_wrong_fracs) - 1)
                        temp_frac = temp_wrong_fracs[rand]
                        temp_wrong_fracs.remove(temp_wrong_fracs[rand])
                elif(len(temp_right_fracs) > 0):
                    rand = self.array_random(0, len(temp_right_fracs) - 1)
                    temp_frac = temp_right_fracs[rand]
                    temp_right_fracs.remove(temp_right_fracs[rand])
                else:
                    rand = self.array_random(0, len(temp_wrong_fracs) - 1)
                    temp_frac = temp_wrong_fracs[rand]
                    temp_wrong_fracs.remove(temp_wrong_fracs[rand])

                button = self.uiContainer.add_button(str(temp_frac), (padding * i) + (width * i) + side_margin, (padding * j) + (height * j) + top_margin, width, height)
                button.font = pygame.font.SysFont("monospace", 30)
                button.baseColour = (0, 0, 0)
                button.hoverColour = (255, 255, 255)
                button.clickColour = (128, 128, 128)
                button.hoverFill = 1
        
    def update(self):
        if xo_input.escape:
            self.resetLevel()
            self.score = 0
            self.wrongAnswers = 0
            self.stateManager.switchGameState("MainScreen")
            return

        endLoop = False
        for button in self.uiContainer.components:
            if button.text != "" and button.was_pressed():
                btnFrac = frac_parse(button.text)
                if btnFrac == self.answer:
                    self.score += self.addScore
                    self.rightAnswers += 1
                    button.text = ""
                else:
                    self.score -= self.scoreLoss
                    self.wrongAnswers += 1
                    button.text = ""
                print "Got {0} / {1} fractions!".format(self.rightAnswers, self.totalRightAnswers)
        if self.rightAnswers == self.totalRightAnswers:
            self.resetLevel()
            self.stateManager.switchGameState("GameScreen")
        if(self.wrongAnswers == 3):
            setScore(self.score)
            self.wrongAnswers = 0
            self.resetLevel()
            self.score = 0
            self.stateManager.switchGameState("WinScreen")

        self.uiContainer.update()
    
    def draw(self):
        x = (-self.screenInfo.current_w / 2) + 90
        y = (-self.screenInfo.current_h / 2) + 110
        self.drawText("Score: " + str(self.score), self.scoreFont, x, y)
        self.drawText("Lives: " + str(3 - self.wrongAnswers), self.scoreFont, x + 500, y)
        self.drawText("Find these multiples: " + str(self.answer), self.titleFont, 0, (-self.screenInfo.current_h/2) + 70)
        # UI needs to be drawn LAST
        self.uiContainer.draw()
        #returns true if colliding with enemy
        if self.enemy.update(self.uiContainer.selectedIndex):
            self.score -= self.scoreLoss
            self.wrongAnswers += 1

    def final(self):
        pass

    def drawText(self, text, font, offsetX, offsetY):
        label = font.render(text, 1, self.textColour)
        text_width, text_height = font.size(text)
        x = (self.screenInfo.current_w/2) - (text_width/2) + offsetX
        y = (self.screenInfo.current_h/2) - (text_height/2) + offsetY
        self.window.blit(label, (x, y))

    def array_random(self, start, end):
        if(start == end):
            return start
        return randint(start, end)

    def resetLevel(self):
        self.uiContainer.components = []
        self.rightAnswers = 0
        self.totalRightAnswers = 0
