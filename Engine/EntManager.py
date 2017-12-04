import pygame as pg

class EntManager:
    def __init__(self):
        self._entities = pg.sprite.RenderPlain()
        self._entholders = []

    def PostUpdate(self):
        for ent in self._entities:
            ent.postupdate()

    def Draw(self, screen):
        for ent in self._entities:
            if ent.visible:
                screen.blit(ent.image, ent.rect)

    def AddEntities(self, *entities):
        self._entities.add(entities)

    def AddEntityHolder(self, entholder):
        self._entholders.append(entholder)

    def Update(self):
        ents = []
        for ent in self._entities:
            ents.extend(ent.get_entities())
            ent.reset_entities()
        for eh in self._entholders:
            ents.extend(eh.get_entities())
            ent.reset_entities()
        self._entities.add(ents)
        self._entities.update()
        for eh in self._entholders:
            eh.update()

    def PhysicsUpdate(self):
        for ent in self._entities:
            if ent.get_collisions:
                collidingents = []
                for colent in self._entities:
                    if colent.rect.colliderect(ent.rect):
                        collidingents.append(colent)
                ent.collisions(collidingents)

    def GetEntity(self, name):
        for ent in self._entities:
            if ent.__name__ == name:
                return ent
    def GetTimers(self):
        timers = []
        for ent in self._entities:
            timers.extend(ent.get_timers())
            ent.reset_timers()
        for eh in self._entholders:
            timers.extend(eh.get_timers())
            eh.reset_timers()
        return timers