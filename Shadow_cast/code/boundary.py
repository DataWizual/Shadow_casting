import pygame
from settings import *


class Boundary:
    def __init__(self, x1, y1, x2, y2):
        self.a = pygame.Vector2(x1, y1)
        self.b = pygame.Vector2(x2, y2)

    def draw(self, screen):
        pygame.draw.aaline(screen, P_BLUE, self.a, self.b)
