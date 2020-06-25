import pygame as pg
import numpy as np
import constants as const

class Map:
    def __init__(self, sheet, gmap, window_size):
        self._sheet = sheet
        #print(self._sheet)
        self.map = gmap
        # print(self.map)
        # print(self.map[0][3])
        self.view = window_size
        self.viewfoc = (0, 0)

    def drawSurroundings(self, pos):
        if(pos[0] >= self.map.shape[0] - (const.CONST_VIEWPORT_SIZE[0]/2 - 1)):
            pos = self.map.shape[0] - (const.CONST_VIEWPORT_SIZE[0]/2 - 1), pos[1]
        elif(pos[0] <= (const.CONST_VIEWPORT_SIZE[0]/2 - 1)):
            pos = (const.CONST_VIEWPORT_SIZE[0]/2 - 1), pos[1]

        if(pos[1] >= self.map.shape[1] - (const.CONST_VIEWPORT_SIZE[1]/2 - 1)):
            pos = pos[0], self.map.shape[1] - (const.CONST_VIEWPORT_SIZE[1]/2 - 1)
        elif(pos[1] <= (const.CONST_VIEWPORT_SIZE[1]/2 - 1)):
            pos = pos[0], (const.CONST_VIEWPORT_SIZE[1]/2 - 1)

        # pos = int((pos[0] - ((self.view[0]/2)%32))/32), int((pos[1] - ((self.view[1]/2)%32))/32)
        pos = int(pos[0] - const.CONST_VIEWPORT_SIZE[0]/2 + 1), int(pos[1] - const.CONST_VIEWPORT_SIZE[1]/2 + 1)

        self.viewfoc = pos

        cell1 = pg.Surface((32, 32), pg.SRCALPHA)
        cell2 = pg.Surface((32, 32), pg.SRCALPHA) # defining 2 empty surfaces
        cell1.blit(self._sheet, (0, 0), pg.Rect((0, 0), const.CONST_SPRITE_SIZE))
        cell2.blit(self._sheet, (0, 0), pg.Rect((5*32, 0), const.CONST_SPRITE_SIZE))
        # drawing the map cell from the spritesheet for the map to the 2 empty
        # surfaces

        # drawing or "blitting" the cell surfaces onto the main viewport surface
        viewport = pg.Surface(self.view)
        for i in range(0, int(self.view[0]/32)):
            for j in range(0, int(self.view[1]/32)):
                if(self.map[int(pos[0]+i)%200][int(pos[1]+j)%200] == 0):
                    viewport.blit(cell1, (i*32, j*32))
                else:
                    viewport.blit(cell2, (i*32, j*32))

        return viewport

    def drawEntities(self, viewport, entlist):
        for i in entlist:
            (x, y) = (i.pos.x - self.viewfoc[0], i.pos.y - self.viewfoc[1])
            # print(x, y)
            # print(i.pos.x, i.pos.y)
            if(x < const.CONST_VIEWPORT_SIZE[0] and y < const.CONST_VIEWPORT_SIZE[1] and x >= 0 and y >= 0):
                viewport.blit(i.sprite, ((i.pos.x - self.viewfoc[0])*32, (i.pos.y - self.viewfoc[1])*32))

        return viewport

    