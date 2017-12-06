import pygame as pg
import Player
from Engine import Constants
from Engine.EntManager import EntManager
from Engine.Entity import Entity
import math

class Blocker(Entity):
    def __init__(self, pos, player):
        Entity.__init__(self, Constants.BlockerImage(), pos)
        self.rect.x, self.rect.y = 500,270
        self.player = player
        self.get_collisions = True
        self.points = 0
        self.maxpoints = 12

    def update(self):
        self.Move()
        self._UpdateHealth()

    def Move(self):
        player = EntManager.GetEntity("Player")
        pos = pg.mouse.get_pos()
        pos = (pos[0] - player.rect.x, pos[1] - player.rect.y)
        length = math.sqrt(pos[0]**2 + pos[1]**2)
        size = 32
        normalvector = (pos[0] / length, pos[1] / length)
        pos = (pos[0] * size / length, pos[1] * size / length)
        angle = math.acos(normalvector[0])
        if normalvector[1] < 0:
            angle = -angle
        self.set_angle(-angle)
        self.rect.x = pos[0] + player.rect.x
        self.rect.y = pos[1] + player.rect.y

    def _UpdateHealth(self):
        if self.points >= self.maxpoints:
            self.points = 0
            player = EntManager.GetEntity("Player")
            player.health = min(player.health + 1, player.maxhealth)

    def collisions(self, colls):
        bullets = [b for b in colls if b.tag is "Bullet"]
        for b in bullets:
            b.kill()
            self.points += 1

