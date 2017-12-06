import pygame as pg
class Text:
    def __init__(self, text, pos):
        font = pg.font.SysFont("Ariel", 30)
        self._textsurface = font.render(text, False, (0, 0, 0))
        self._pos = pos
    def Draw(self, screen):
        screen.blit(self._textsurface, self._pos)