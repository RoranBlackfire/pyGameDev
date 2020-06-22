import pygame as pg
import numpy as np
import random
import map
import constants as const

#init pygame

pg.init()

screen = pg.display.set_mode(const.CONST_WINDOW_SIZE)
mapsheet = pg.image.load("res/Map/maptileset.png").convert_alpha()
gmap = np.ndarray((200, 200), dtype=int)
gmap.fill(0)

for i in range(0, 50):
    gmap[random.randint(0, 199)][random.randint(0, 199)] = 1

m = map.Map(mapsheet, gmap, const.CONST_WINDOW_SIZE)
pos = (50, 50)

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

    screen.fill((0, 0, 0))
    screen.blit(m.drawSurroundings(pos), (0, 0))
    pg.display.flip()
