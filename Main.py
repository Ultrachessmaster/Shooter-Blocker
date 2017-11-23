import pygame as pg
from pygame.locals import *

pg.init()

size = 1000, 600
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
ballimage = pg.image.load("player.png")
sprite = pg.sprite.Sprite()
sprite.image = ballimage
sprite.rect = ballimage.get_rect()
spritelist = pg.sprite.RenderPlain()
spritelist.add(sprite)
running = True

while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == QUIT:
            running = False

    spritelist.update()
    sprite.rect = sprite.rect.move([1,1])
    screen.fill((0,0,0))
    spritelist.draw(screen)
    pg.display.flip()