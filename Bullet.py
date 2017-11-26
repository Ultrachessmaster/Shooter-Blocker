from Engine import Constants
from Engine.Timer import Timer
from Engine.Entity import Entity

class Bullet(Entity):
    def __init__(self, pos, vel):
        Entity.__init__(self, Constants.BulletImage(), pos)
        self.vel = vel
        self.timers.append(Timer(10, self.kill))