import pygame as pg

class Constants:
    None

def LoadConstants():
        Constants._PlayerImage = pg.image.load("player.png")
        Constants._BulletImage = pg.image.load("bullet.png")
        Constants._Size = 1000, 600

def PlayerImage():
    return Constants._PlayerImage
def BulletImage():
    return Constants._BulletImage
def ScreenSize():
    return Constants._Size