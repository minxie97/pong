import pygame
from .constants import *
import random

class Boom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = random.randrange(1, 6)
        self.height = self.width
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect()
        self.kill_timer = 60
        self.velocity_x = random.randrange(-16,16)
        self.velocity_y = random.randrange(-16,16)

    def update(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        if self.kill_timer == 0:
            self.kill()
        else:
            self.kill_timer -= 1