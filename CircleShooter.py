from Bullet import Bullet
from Enemy import Enemy
from Engine import Constants
from Engine.Timer import Timer


class CircleShooter(Enemy):
    def __init__(self, pos):
        Enemy.__init__(self, Constants.PlayerImage(), pos)
        self.vel = (0, 1.5)
        self.bulletrate = 1
        self.bulletspeed = 3
        self.timers.append(Timer(self.bulletrate, self.shoot_bullet))

    def update(self):
        Enemy.update(self)

    def shoot_bullet(self):
        self.entities.append(Bullet((self.rect.x, self.rect.y), (self.bulletspeed, self.bulletspeed)))
        self.entities.append(Bullet((self.rect.x, self.rect.y), (self.bulletspeed, -self.bulletspeed)))
        self.entities.append(Bullet((self.rect.x, self.rect.y), (-self.bulletspeed, self.bulletspeed)))
        self.entities.append(Bullet((self.rect.x, self.rect.y), (-self.bulletspeed, -self.bulletspeed)))
        self.entities.append(Bullet((self.rect.x, self.rect.y), (-1.5 * self.bulletspeed, 0)))
        self.entities.append(Bullet((self.rect.x, self.rect.y), (0, -1.5 * self.bulletspeed)))
        self.entities.append(Bullet((self.rect.x, self.rect.y), (1.5 * self.bulletspeed, 0)))
        self.entities.append(Bullet((self.rect.x, self.rect.y), (0, 1.5 * self.bulletspeed)))

        self.timers.append(Timer(self.bulletrate, self.shoot_bullet))
