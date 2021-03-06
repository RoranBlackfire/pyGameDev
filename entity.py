import pygame as pg

# entity management system for the game

class Coord:
    def __init__(self, x, y, elev=0):
        self.x = x
        self.y = y
        self.elev = elev

    def __init__(self, pos, elev=0):
        self.x = pos[0]
        self.y = pos[1]
        self.elev = elev

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y, self.elev + other.elev)

    def __add__(self, other):
        return Coord(self.x + other[0], self.y + other[1], elev=self.elev)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y, self.elev - other.elev)

    def __sub__(self, other):
        return Coord(self.x - other[0], self.y - other[1], elev=self.elev)


class  Stat:
    def __init__(self, hlt, nrg):
        self.hlt = 100  # default health
        self.nrg = 100  # defualt energy
    
    #def rip(self, hlt):
     #   if(self.hlt < 0)
      #  {
       #     return death()
        #}


class Entity:
    def __init__(self, pos, sprite):
        self.pos = pos
        self.sprite = sprite

    def move(self, key):
        if (key == pg.K_LEFT):
            self.pos -= (1, 0)
        elif (key == pg.K_RIGHT):
            self.pos += (1, 0)
        elif (key == pg.K_UP):
            self.pos -= (1, 0)
        elif (key == pg.K_DOWN):
            self.pos -= (1, 0)

# class Player(Entity):


    