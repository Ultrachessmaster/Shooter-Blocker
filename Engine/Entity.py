import pygame as pg
import math

class Entity(pg.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.pos = pos
        self.image = image
        self.rect = image.get_rect()
        self.vel = (0, 0)
        self.angle = 0
    def postupdate(self):
        #move entity on screen
        xvel, yvel = self.vel
        self.rect = self.rect.move([xvel * self.speed, yvel * self.speed])
    def set_angle(self, desiredangle):
        if desiredangle < 0:
            desiredangle = 360 + desiredangle
        self.image = pg.transform.rotate(self.image, math.fabs(self.angle - desiredangle))