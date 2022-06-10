from .constants import *
import pygame

class Paddle:

    def __init__(self, x, y, width, height):
        self.x = self.starting_x = x
        self.y = self.starting_y = y
        self.width = width
        self.height = height

    def render_paddle(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= PADDLE_VELO
        else:
            self.y += PADDLE_VELO

    def reset(self):
        self.x = self.starting_x
        self.y = self.starting_y