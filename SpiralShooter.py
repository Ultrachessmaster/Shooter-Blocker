import math
import pygame as pg

from Bullet import Bullet
from Enemy import Enemy
from Engine import Constants
from Engine.Entity import Entity
from Engine.Timer import Timer

class SpiralShooter(Enemy):
    def __init__(self, pos):
        Enemy.__init__(self, Constants.PlayerImage(), pos)
        self.circlespeed = 0.01
        self.offsetspeed = 0.3
        self.dir = 0, 1
        self.speed = 5
        self.bulletrate = 0.1

        timer = Timer(self.bulletrate, self.shoot_bullet)
        self.timers.append(timer)

    def update(self):
        Enemy.update(self)
        #spin in cirle while moving in a direction
        time = self.circlespeed * pg.time.get_ticks()
        xvel = math.sin(time)
        yvel = math.cos(time)
        xdir, ydir = self.dir
        xvel += self.offsetspeed * xdir
        yvel += self.offsetspeed * ydir
        xvel *= self.speed
        yvel *= self.speed
        self.vel = (xvel, yvel)

    def shoot_bullet(self):
        bullet = Bullet((self.rect.x, self.rect.y), self.vel)
        self.entities.append(bullet)

        timer = Timer(self.bulletrate, self.shoot_bullet)
        self.timers.append(timer)
        return
