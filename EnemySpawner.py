import pygame as pg
from CircleShooter import CircleShooter
from Engine import Constants
from Engine.Presets import TimerPreset, EntitySpawnerPreset
from Engine.Timer import Timer
from SpiralShooter import SpiralShooter


class EnemySpawner(TimerPreset, EntitySpawnerPreset):
    def __init__(self):
        TimerPreset.__init__(self)
        EntitySpawnerPreset.__init__(self)
        offset = 100
        self.spawnpos = [(offset, -32), (Constants.ScreenSize()[0] / 2, -32), (Constants.ScreenSize()[0] - offset, -32)]
        self.timers.append(Timer(5, self.SpawnEnemies))
        self.iteration = -1

    def SpawnEnemies(self):
        self.iteration += 1
        #if self.iteration == 0:
        self.FirstIteration()
        self.timers.append(Timer(15, self.SpawnEnemies))

    def FirstIteration(self):
        self.entities.append(SpiralShooter(self.spawnpos[0]))
        #self.entities.append(CircleShooter(self.spawnpos[1]))
        self.entities.append(SpiralShooter(self.spawnpos[2]))