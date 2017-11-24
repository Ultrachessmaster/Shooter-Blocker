import math

import pygame as pg

from Engine.Entity import Entity


class SexyImp(Entity):
    def __init__(self, image, pos):
        Entity.__init__(self, image, pos)

        self.circlespeed = 0.01
        self.offsetspeed = 0.3
        self.dir = 0, 1
    def update(self):
        #spin in cirle while moving in a direction
        time = self.circlespeed * pg.time.get_ticks()
        xvel = math.sin(time)
        yvel = math.cos(time)
        xdir, ydir = self.dir
        xvel += self.offsetspeed * xdir
        yvel += self.offsetspeed * ydir
        self.vel = (xvel, yvel)