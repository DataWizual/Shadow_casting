import pygame
import numpy as np
from ray import Ray
from settings import *


class Particle:
    def __init__(self, screen, walls):
        self.pos = pygame.Vector2(
            screen.get_width() // 2, screen.get_height() // 2)
        self.walls = walls
        self.rays = []

    def update(self, x, y):
        self.pos.update(x, y)

    def twopointangle(self):
        start = []
        for wall in self.walls:
            ray_a, ray_delta_a, ray_delta_a_n = self.angle_calc(
                wall.a.x, wall.a.y, 0.00001)
            ray_b, ray_delta_b, ray_delta_b_n = self.angle_calc(
                wall.b.x, wall.b.y, 0.00001)
            start.extend((ray_delta_a_n, ray_a, ray_delta_a,
                         ray_delta_b_n, ray_b, ray_delta_b))
        return start

    def angle_calc(self, x, y, delta_rad):
        angle_x = x - self.pos.x
        angle_y = y - self.pos.y
        angle = np.arctan2(angle_y, angle_x)
        ray = Ray(self.pos, angle)
        ray_delta = Ray(self.pos, angle+delta_rad)
        ray_delta_n = Ray(self.pos, angle-delta_rad)
        return ray, ray_delta, ray_delta_n

    def look(self):
        self.rays = self.twopointangle()
        for ray in self.rays:
            ray.finish_pos = self.ray_calc(ray)
        self.rays.sort(key=lambda x: x.angle, reverse=True)

    def ray_calc(self, ray):
        closest = None
        record = float('inf')
        for wall in self.walls:
            pt = ray.cast(wall)
            if pt:
                d = self.pos.distance_squared_to(pt)
                if d < record:
                    record = d
                    closest = pt
        return closest

    def draw(self, screen):
        pygame.mouse.set_visible(False)
        new_surface = pygame.Surface((width, height))
        new_surface.fill((0, 0, 0))
        image = pygame.image.load(
            "polygon/light.png").convert_alpha()
        pygame.draw.circle(screen, ORANGE, self.pos, 4)
        for ray in range(len(self.rays)):
            if self.rays[ray].finish_pos and self.rays[
                    (1 + ray) % len(self.rays)].finish_pos:
                pygame.draw.polygon(
                    new_surface, GREEN, (
                        self.pos, self.rays[ray].finish_pos,
                        self.rays[(1 + ray) % len(self.rays)].finish_pos))
        new_surface.set_colorkey(GREEN)
        screen.blit(image, (self.pos.x - 300, self.pos.y - 300))
        screen.blit(new_surface, (0, 0))
