import pygame
import constants as c

def handle_paddle_move(keys, left_paddle, right_paddle):
    #left
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VELO >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VELO + left_paddle.height <= c.HEIGHT:
        left_paddle.move(up=False)

    #right
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VELO >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VELO + right_paddle.height <= c.HEIGHT:
        right_paddle.move(up=False)