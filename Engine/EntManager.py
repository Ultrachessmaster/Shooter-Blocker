import pygame as pg

class EntManager:
    def __init__(self):
        EntManager._entities = pg.sprite.RenderPlain()
        self._entholders = []

    def PostUpdate(self):
        for ent in EntManager._entities:
            ent.postupdate()

    def Draw(self, screen):
        for ent in EntManager._entities:
            if ent.visible:
                screen.blit(ent.image, ent.rect)
            for text in ent.textlist:
                text.Draw(screen)

    def AddEntities(*entities):
        EntManager._entities.add(entities)

    def AddEntityHolder(self, entholder):
        self._entholders.append(entholder)

    def Update(self):
        ents = []
        for ent in EntManager._entities:
            ents.extend(ent.get_entities())
            ent.reset_entities()
        for eh in self._entholders:
            ents.extend(eh.get_entities())
            ent.reset_entities()
        EntManager._entities.add(ents)
        EntManager._entities.update()
        for eh in self._entholders:
            eh.update()

    def PhysicsUpdate(self):
        for ent in EntManager._entities:
            if ent.get_collisions:
                collidingents = []
                for colent in EntManager._entities:
                    if colent.rect.colliderect(ent.rect):
                        collidingents.append(colent)
                ent.collisions(collidingents)

    def GetEntity(tag):
        for ent in EntManager._entities:
            if ent.tag == tag:
                return ent
        return None

    def GetTimers(self):
        timers = []
        for ent in EntManager._entities:
            timers.extend(ent.get_timers())
            ent.reset_timers()
        for eh in self._entholders:
            timers.extend(eh.get_timers())
            eh.reset_timers()
        return timers