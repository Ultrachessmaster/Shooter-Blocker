import pygame as pg
from Engine import Constants
from Engine.Entity import Entity

class Player(Entity):
    def __init__(self, pos):
        Entity.__init__(self, Constants.PlayerImage(), pos)
        self.speed = 6
        self.xLeft = 0
        self.xRight = 1000
        self.yDown = 600
        self.yUp = 0
        self.rect.x, self.rect.y = 500,300
        self.xVel = 0
        self.yVel = 0
        self.tag = "Player"

    def update(self):
        pressed = pg.key.get_pressed()
        # Movement and Collision
        xVel = 0
        yVel = 0
        if pressed[pg.K_w]:
            if self.rect.top > self.yUp:
                if (self.rect.top - self.speed) < self.yUp:
                    difference = self.yUp + self.rect.top
                    yVel -= difference
                else:
                    yVel -= self.speed
        if pressed[pg.K_s]:
            if self.rect.bottom < self.yDown:
                if (self.rect.bottom + self.speed) > self.yDown:
                    difference = self.yDown - self.rect.bottom
                    yVel += difference
                else:
                    yVel += self.speed
        if pressed[pg.K_d]:
            if self.rect.right < self.xRight:
                if (self.rect.right + self.speed) > self.xRight:
                    difference = self.xRight - self.rect.right
                    xVel += difference
                else:
                    xVel += self.speed
        if pressed[pg.K_a]:
            if self.rect.left > self.xLeft:
                if (self.rect.left - self.speed) < self.xLeft:
                    difference = self.xLeft + self.rect.left
                    xVel -= difference
                else:
                    xVel -= self.speed

        self.vel = (xVel,yVel)

        self.xVel = xVel
        self.yVel = yVel

    def getVel(self):
        val = [self.xVel, self.yVel]
        return val

    def getRect(self):
        val = [self.rect.x, self.rect.y]
        return val

    #def collision(self):




