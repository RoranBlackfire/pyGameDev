import pygame as pg
from pygame.locals import *
import numpy as np
import random
import map
import constants as const
import entity as ent

#init pygame

pg.init()


# this is a temporary class just to get a player sprite
# to appear
# class Player:
#     def __init__(self, pos, sprite):
#         self.pos = pos
#         self.sprite = sprite


screen = pg.display.set_mode(const.CONST_WINDOW_SIZE)
pg.display.set_caption("Prototyping")
playersheet = pg.image.load("res/Male/Male 01-1.png").convert_alpha()
selec = pg.image.load("res/misc/selector.png")
selecsurf = pg.Surface(const.CONST_SPRITE_SIZE).convert_alpha()
selecsurf.blit(selec, (0, 0))
selecsurf.convert_alpha()
mapsheet = pg.image.load("res/Map/maptileset.png").convert_alpha()
gmap = np.ndarray(const.CONST_MAP_SIZE, dtype=int)
gmap.fill(0)

for i in range(0, 150):
    gmap[random.randint(0, 199)][random.randint(0, 199)] = 1

m = map.Map(mapsheet, gmap, const.CONST_WINDOW_SIZE)
pos = (50, 50)
selector = ent.Entity(ent.Coord(pos), selecsurf)

sprlist = [selector]

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if (event.type == pg.KEYDOWN and event.key == pg.K_RIGHT):
            pos = pos[0]+1, pos[1]
        if (event.type == pg.KEYDOWN and event.key == pg.K_LEFT):
            pos = pos[0] -1, pos[1]
        if (event.type == pg.KEYDOWN and event.key == pg.K_UP):
            pos = pos[0], pos[1]-1
        if (event.type == pg.KEYDOWN and event.key == pg.K_DOWN):
            pos = pos[0], pos[1]+1

    if(pos[0] <= 0):
        pos = 0, pos[1]
    if(pos[0] >= 200):
        pos = 199, pos[1]
    if(pos[1] <= 0):
        pos = pos[0], 0
    if(pos[1] >= 200):
        pos = pos[0], 199

    sprlist[0].pos = ent.Coord(pos)

    viewport = m.drawSurroundings(pos)

    screen.fill((0, 0, 0))
    screen.blit(m.drawEntities(viewport, sprlist), (0, 0))
    pg.display.flip()
