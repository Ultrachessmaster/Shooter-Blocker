import pygame as pg

pg.init()

size = 800, 300
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
spritelist = pg.sprite.RenderPlain()

while True:
    clock.tick(60)
    spritelist.update()