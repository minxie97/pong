import pygame
import constants as c
import random

class Ball:
    VELO = c.BALL_VELO
    COLOR = c.WHITE

    def __init__(self, x, y, radius):
        self.x = self.starting_x = x
        self.y = self.starting_y = y
        self.radius = radius
        self.x_velo = self.VELO
        self.y_velo = 0

    def render_ball(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_velo
        self.y += self.y_velo

    def reset(self):
        self.x = self.starting_x
        self.y = self.starting_y
        self.x_velo *= -1
        self.y_velo = random.randint(-2, 2)