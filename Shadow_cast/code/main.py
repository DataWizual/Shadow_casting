import pygame
from pygame.locals import *
from particle import Particle
from settings import *
from obstacles import *


def main():
    pygame.init()
    sc = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    walls = obstacle_w()
    particle = Particle(sc, walls)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        sc.fill(BLACK)
        particle.draw(sc)
        particle.look()
        for wall in walls:
            wall.draw(sc)
        draw_polygon(sc)
        mx, my = pygame.mouse.get_pos()
        particle.update(mx, my)
        pygame.display.flip()
        clock.tick()


if __name__ == '__main__':
    main()
