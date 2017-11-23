from Engine.Entity import Entity
import math
import pygame as pg

class SexyImp(Entity):
    def __init__(self, image, pos):
        Entity.__init__(self, image, pos)
        self.xvel = 0
        self.yvel = 0
        self.speed = 5
        self.circleradius = 0.01
    def update(self):
        time = self.circleradius * pg.time.get_ticks()
        self.xvel = math.sin(time)
        self.yvel = math.cos(time)
    def postupdate(self):
        self.rect = self.rect.move([self.xvel * self.speed, self.yvel * self.speed])