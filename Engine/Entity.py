import pygame as pg
import math

from Engine.Presets import TimerPreset, EntitySpawnerPreset


class Entity(TimerPreset, EntitySpawnerPreset, pg.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        TimerPreset.__init__(self)
        EntitySpawnerPreset.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.visible = True
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel = (0, 0)
        self.angle = 0
        self.tag = ""
        self.get_collisions = False
    def postupdate(self):
        #move entity on screen
        xvel, yvel = self.vel
        self.rect = self.rect.move([xvel, yvel])
    def set_angle(self, desiredangle):
        if desiredangle < 0:
            desiredangle = 360 + desiredangle
        self.image = pg.transform.rotate(self.image, (desiredangle - self.angle))
        self.angle = desiredangle
    def collisions(self, colls):
        return