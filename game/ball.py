import pygame
from .constants import *
import math
import random

class Ball:

    def __init__(self, x, y, radius):
        self.x = self.starting_x = x
        self.y = self.starting_y = y
        self.radius = radius
        angle = self.get_random_angle(-30, 30, [0])
        pos = 1 if random.random() < 0.5 else -1

        self.x_velo = pos * abs(math.cos(angle) * BALL_VELO)
        self.y_velo = math.sin(angle) * BALL_VELO

    def get_random_angle(self, min_angle, max_angle, excluded):
        angle = 0
        while angle in excluded:
            angle = math.radians(random.randrange(min_angle, max_angle))

        return angle

    def render_ball(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_velo
        self.y += self.y_velo

    def reset(self):
        self.x = self.starting_x
        self.y = self.starting_y

        angle = self.get_random_angle(-30, 30, [0])
        x_velo = abs(math.cos(angle) * BALL_VELO)
        y_velo = math.sin(angle) * BALL_VELO

        self.x_velo *= -1
        self.y_velo = y_velo