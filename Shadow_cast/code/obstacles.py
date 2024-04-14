import pygame
from settings import *
from boundary import *


def draw_polygon(screen):
    polygons = [
        [(100, 100), (300, 50), (200, 250)],
        [(400, 100), (550, 50), (500, 300)],
        [(50, 450), (250, 300), (250, 500), (150, 550)],
        [(450, 350), (350, 300), (350, 450), (550, 550)],
        [(50, 250), (100, 250), (50, 350)],
        [(300, 200), (350, 200), (350, 250), (300, 250)]
    ]

    colors = [P_BLUE, P_BLUE, P_BLUE, P_RED, P_RED, P_RED, P_RED]

    for polygon, color in zip(polygons, colors):
        pygame.draw.polygon(screen, color, polygon, 0)


def obstacle_w():
    walls = []
    point = [[0, 0, width, 0], [width, 0, width, height],
             [width, height, 0, height], [0, height, 0, 0],
             [100, 100, 300, 50], [100, 100, 200, 250],
             [300, 50, 200, 250], [400, 100, 550, 50],
             [400, 100, 500, 300], [550, 50, 500, 300],
             [50, 450, 250, 300], [50, 450, 150, 550],
             [250, 300, 250, 500], [150, 550, 250, 500],
             [450, 350, 350, 300], [350, 300, 350, 450],
             [450, 350, 550, 550], [350, 450, 550, 550],
             [50, 250, 100, 250], [50, 250, 50, 350],
             [100, 250, 50, 350], [300, 200, 350, 200],
             [300, 200, 300, 250], [350, 200, 350, 250],
             [300, 250, 350, 250]]
    for sublist in point:
        for i in range(0, len(sublist), 2):
            x1, y1, x2, y2 = sublist[i], sublist[i+1], sublist[(
                i+2) % len(sublist)], sublist[(i+3) % len(sublist)]
            walls.append(Boundary(x1, y1, x2, y2))
    return walls
