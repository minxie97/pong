import pygame
import os, sys

pygame.init()

#screen
WIDTH, HEIGHT = 800, 600

#frames per second
FPS = 60

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)

#paddles
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
PADDLE_VELO = 5

#ball
BALL_RADIUS = 7
BALL_VELO = 5

#score
WIN_SCORE = 11

#font
FONT = pygame.font.Font("assets/ARCADECLASSIC.TTF", 50)