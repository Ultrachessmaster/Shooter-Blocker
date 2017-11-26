import pygame as pg
from pygame.locals import *

from CircleShooter import CircleShooter
from SpiralEnemy import SpiralEnemy
from Engine import Constants

class Game():
    def __init__(self):
        pg.init()
        Constants.LoadConstants()

        self.screen = pg.display.set_mode(Constants.ScreenSize())
        self.clock = pg.time.Clock()
        spiral = SpiralEnemy((0, 0))
        circleshooter = CircleShooter((400, 0))
        self.spritelist = pg.sprite.RenderPlain()
        self.spritelist.add(spiral, circleshooter)
        self.running = True
        self.timers = []
        self.MainLoop()

    def Update(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False

        self.spritelist.update()

    def PostUpdate(self):
        for sprite in self.spritelist:
            sprite.postupdate()

    def GetEntities(self):
        for entity in self.spritelist:
            self.spritelist.add(entity.get_entities())
            entity.reset_entities()

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
        for sprite in self.spritelist:
            self.timers.extend(sprite.get_timers())
            sprite.reset_timers()

    def Draw(self):
        self.screen.fill((255, 255, 255))
        self.spritelist.draw(self.screen)
        pg.display.flip()



    def MainLoop(self):
        while self.running:
            millisecs = self.clock.tick(60)

            self.Update()
            self.PostUpdate()
            self.TimerUpdate(float(millisecs) / float(1000))
            self.GetEntities()
            self.GetTimers()
            self.Draw()
g = Game()
#Kenton is a nigger