import pygame as pg
from pygame.locals import *

from CircleShooter import CircleShooter
from EnemySpawner import EnemySpawner
from Engine.EntManager import EntManager
from SpiralEnemy import SpiralEnemy
from Engine import Constants
import Player
import Blocker

class Game():
    def __init__(self):
        pg.init()
        Constants.LoadConstants()

        self.screen = pg.display.set_mode(Constants.ScreenSize())
        self.clock = pg.time.Clock()
        spiral = SpiralEnemy((0, 0))
        player = Player.Player((0, 0))
        blocker = Blocker.Blocker((0, 0), player)
        enemyspawner = EnemySpawner()
        circleshooter = CircleShooter((400, 0))
        self.entmanager = EntManager()
        self.entmanager.AddEntities(spiral, circleshooter, player, blocker)
        self.entmanager.AddEntityHolder(enemyspawner)
        self.running = True
        self.timers = []
        self.MainLoop()

    def Update(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False

        self.entmanager.Update()
        self.entmanager.PhysicsUpdate()

    def PostUpdate(self):
        self.entmanager.PostUpdate()

    def TimerUpdate(self, deltasecs):
        #search through timers, check if done and update, then remove any timers that are done
        #keep track of which timers are done in a separate list because removing a timer while in a for loop...
        #...messes up indexing
        timersdone = []
        for timer in self.timers:
            isdone = timer.UpdateAndIsDone(deltasecs)
            if isdone:
                timersdone.append(timer)
        for timer in timersdone:
            self.timers.remove(timer)

    def GetTimers(self):
        self.timers.extend(self.entmanager.GetTimers())

    def Draw(self):
        self.screen.fill((255, 255, 255))
        self.entmanager.Draw(self.screen)
        pg.display.flip()

    def MainLoop(self):
        while self.running:
            millisecs = self.clock.tick(60)

            self.Update()
            self.PostUpdate()
            self.TimerUpdate(float(millisecs) / float(1000))
            self.GetTimers()
            self.Draw()
g = Game()
#Kenton is a nigger