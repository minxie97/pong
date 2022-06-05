import constants as c
import pygame

class Paddle:

    COLOR = c.WHITE
    VELO = c.PADDLE_VELO

    def __init__(self, x, y, width, height):
        self.x = self.starting_x = x
        self.y = self.starting_y = y
        self.width = width
        self.height = height

    def render_paddle(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VELO
        else:
            self.y += self.VELO

    def reset(self):
        self.x = self.starting_x
        self.y = self.starting_y