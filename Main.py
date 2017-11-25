import pygame as pg
from pygame.locals import *
import SexyImp

class Game():
    def __init__(self):
        pg.init()

        self.size = 1000, 600
        self.screen = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()
        self.playerimage = pg.image.load("player.png")
        self.imp = SexyImp.SexyImp(self.playerimage, (0, 0))
        self.spritelist = pg.sprite.RenderPlain()
        self.spritelist.add(self.imp)
        self.running = True
        self.MainLoop()

    def Update(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False

        self.spritelist.update()

    def Draw(self):
        self.screen.fill((0, 0, 0))
        self.spritelist.draw(self.screen)
        pg.display.flip()

    def PostUpdate(self):
        for sprite in self.spritelist:
            sprite.postupdate()

    def MainLoop(self):
        while self.running:
            self.clock.tick(60)

            self.Update()
            self.PostUpdate()
            self.Draw()
g = Game()
#Kenton is a nigger