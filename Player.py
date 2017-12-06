import pygame as pg
from Engine import Constants
from Engine.Entity import Entity
from Engine.Text import Text
from Engine.Timer import Timer


class Player(Entity):
    def __init__(self, pos):
        Entity.__init__(self, Constants.PlayerImage(), pos)
        self.speed = 4
        self.xLeft = 0
        self.xRight = 1000
        self.yDown = 600
        self.yUp = 0
        self.rect.x, self.rect.y = 500,300
        self.xVel = 0
        self.yVel = 0
        self.tag = "Player"
        self.get_collisions = True
        self.health = 5
        self.maxhealth = 15
        self.invincible = False
        self.textlist.append(None)

    def update(self):
        self._MoveAndCollide()
        self.CreateText()
        if self.health <= 0:
            self.kill()

    def CreateText(self):
        text = Text("Health: {0}".format(self.health), (0, 0))
        self.textlist[0] = text

    def _MoveAndCollide(self):
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

        self.vel = (xVel, yVel)
        self.xVel = xVel
        self.yVel = yVel

    def getVel(self):
        val = [self.xVel, self.yVel]
        return val

    def getRect(self):
        val = [self.rect.x, self.rect.y]
        return val

    def collisions(self, colls):
        if self.invincible: return

        bullets = [b for b in colls if b.tag is "Bullet"]
        for b in bullets:
            b.kill()
            self.health -= 1
        if len(bullets) > 0:
            self.timers.append(Timer(0.1, self.flip_invisibility))
            def make_notinvincible(): self.invincible = False
            self.timers.append(Timer(2, make_notinvincible))
            self.invincible = True
    def flip_invisibility(self):
        self.visible = not self.visible
        if self.invincible:
            self.timers.append(Timer(0.1, self.flip_invisibility))
        else:
            self.visible = True

