import pygame as pg
import Player
from Engine import Constants
from Engine.Entity import Entity

class Blocker(Entity):
    def __init__(self, pos, player):
        Entity.__init__(self, Constants.BlockerImage(), pos)
        self.rect.x, self.rect.y = 500,270
        self.player = player
        self.get_collisions = True

    def update(self):
        playerRect = self.player.getRect()
        playerRectX = playerRect[0]
        playerRectY = playerRect[1]
        pressed = pg.key.get_pressed()
        self.vel = (self.player.getVel())
        offsetX, offsetY = 30, 25

        if pressed[pg.K_RIGHT]:
            self.set_angle(360)
            self.rect.x = playerRectX + offsetX
            self.rect.y = playerRectY

        if pressed[pg.K_LEFT]:
            self.set_angle(180)
            self.rect.x = playerRectX - offsetX
            self.rect.y = playerRectY

        if pressed[pg.K_UP]:
            self.set_angle(90)
            self.rect.x = playerRectX
            self.rect.y = playerRectY - offsetY

        if pressed[pg.K_DOWN]:
            self.set_angle(270)
            self.rect.x = playerRectX
            self.rect.y = playerRectY + offsetY

    def collisions(self, colls):
        delete = []
        for coll in colls:
            if coll.tag == "Bullet":
                delete.append(coll)
        for coll in delete:
            coll.kill()
