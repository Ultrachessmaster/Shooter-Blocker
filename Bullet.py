from Engine.Entity import Entity


class Bullet(Entity):
    def __init__(self, image, pos):
        Entity.__init__(self, image, pos)