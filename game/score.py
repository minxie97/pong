import pygame
import constants as c

def render_score(win, left_score, right_score):
    left_score_text = c.FONT.render(f"{left_score}", 1, c.WHITE)
    right_score_text = c.FONT.render(f"{right_score}", 1, c.WHITE)
    win.blit(left_score_text, (c.WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (c.WIDTH * (3/4) - right_score_text.get_width()//2, 20))