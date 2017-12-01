import pygame as pg

class EntManager:
    def __init__(self):
        self._entities = pg.sprite.RenderPlain()

    def PostUpdate(self):
        for ent in self._entities:
            ent.postupdate()

    def Draw(self, screen):
        self._entities.draw(screen)

    def AddEntities(self, *entities):
        self._entities.add(entities)

    def Update(self):
        ents = []
        for ent in self._entities:
            ents.extend(ent.get_entities())
            ent.reset_entities()
        self._entities.add(ents)
        self._entities.update()

    def GetEntity(self, name):
        for ent in self._entities:
            if ent.__name__ == name:
                return ent
    def GetTimers(self):
        timers = []
        for ent in self._entities:
            timers.extend(ent.get_timers())
            ent.reset_timers()
        return timers