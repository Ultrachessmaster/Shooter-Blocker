from Engine.Entity import Entity
from Engine.Timer import Timer
from Engine import Constants


class Enemy(Entity):
    def __init__(self, image, pos):
        Entity.__init__(self, image, pos)
    def update(self):
        if self.rect.y > Constants.ScreenSize()[1]:
            self.kill()