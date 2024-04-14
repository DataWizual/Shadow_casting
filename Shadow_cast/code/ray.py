import pygame
import numpy as np
from settings import *


class Ray:
    def __init__(self, pos, angle):
        self.angle = angle
        self.start_pos = pos
        self.finish_pos = pygame.Vector2()
        self.dir = pygame.Vector2(np.cos(angle), np.sin(angle))

    def cast(self, wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y
        x3 = self.start_pos.x
        y3 = self.start_pos.y
        x4 = self.start_pos.x+self.dir.x
        y4 = self.start_pos.y+self.dir.y
        den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        if den == 0:
            return None
        t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/den
        u = - ((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/den
        if 0 <= t <= 1 and 0 <= u:
            self.finish_pos = pygame.Vector2()
            self.finish_pos.x = x1 + t * (x2 - x1)
            self.finish_pos.y = y1 + t * (y2 - y1)
            return self.finish_pos
        else:
            return None
