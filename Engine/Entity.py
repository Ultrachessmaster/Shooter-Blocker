import pygame as pg
import math

class Entity(pg.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel = (0, 0)
        self.angle = 0
        self.timers = []
        self.entities = []
    def postupdate(self):
        #move entity on screen
        xvel, yvel = self.vel
        self.rect = self.rect.move([xvel, yvel])
    def get_entities(self):
        return self.entities
    def reset_entities(self):
        self.entities = []
    def get_timers(self):
        return self.timers
    def reset_timers(self):
        self.timers = []
    def set_angle(self, desiredangle):
        if desiredangle < 0:
            desiredangle = 360 + desiredangle
        self.image = pg.transform.rotate(self.image, (desiredangle - self.angle))
        self.angle = desiredangle