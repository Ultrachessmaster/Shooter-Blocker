import pygame as pg
from Engine.Presets import TimerPreset, EntitySpawnerPreset
from SpiralEnemy import SpiralEnemy


class EnemySpawner(TimerPreset, EntitySpawnerPreset):
    def __init__(self):
        TimerPreset.__init__(self)
        EntitySpawnerPreset.__init__(self)
        self.spawnpos = [(-32, 0), (-32, 160), (-32, 320)]

    def update(self):
        for pos in self.spawnpos:
            self.entities.append(SpiralEnemy(pos))