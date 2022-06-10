import pygame
from .paddles import Paddle
from .ball import Ball
from .score import render_score
from .constants import *

pygame.init()

class GameInfo:
    def __init__(self, left_hits, right_hits, left_score, right_score):
        self.left_hits = left_hits
        self.right_hits = right_hits
        self.left_score = left_score
        self.right_score = right_score

class Game:
    def __init__(self):
        self.win_width = WIDTH
        self.win_height = HEIGHT
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        
        self.left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)

        self.left_score = 0
        self.right_score = 0

        self.left_hits = 0
        self.right_hits = 0

    def render_hits(self):
        hits_text = FONT.render(f"{self.left_hits + self.right_hits}", 1, GOLD)
        self.win.blit(hits_text, (self.win_width/2 - hits_text.get_width()//2, 10))

    def render_divider(self):
        for i in range(10, HEIGHT, HEIGHT//24):
            if i % 2 == 1:
                continue
            else:
                pygame.draw.rect(self.win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//24))

    def handle_collision(self):
        ball = self.ball
        left_paddle = self.left_paddle
        right_paddle = self.right_paddle

        if ball.y + ball.radius >= self.win_height:
            ball.y_velo *= -1
        elif ball.y - ball.radius <= 0:
            ball.y_velo *= -1

        if ball.x_velo < 0:
            if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
                if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                    ball.x_velo *= -1

                    middle_y = left_paddle.y + left_paddle.height / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (left_paddle.height / 2) / BALL_VELO
                    y_velo = difference_in_y / reduction_factor
                    ball.y_velo = -1 * y_velo
                    self.left_hits += 1

        else:
            if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
                if ball.x + ball.radius >= right_paddle.x:
                    ball.x_velo *= -1

                    middle_y = right_paddle.y + right_paddle.height / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (right_paddle.height / 2) / BALL_VELO
                    y_velo = difference_in_y / reduction_factor
                    ball.y_velo = -1 * y_velo
                    self.right_hits += 1

    def move_paddle(self, left=True, up=True):
        if left:
            if up and self.left_paddle.y - PADDLE_VELO < 0:
                return False
            if not up and self.left_paddle.y + PADDLE_HEIGHT > self.win_height:
                return False
            self.left_paddle.move(up)
        else:
            if up and self.right_paddle.y - PADDLE_VELO < 0:
                return False
            if not up and self.right_paddle.y + PADDLE_HEIGHT > self.win_height:
                return False
            self.right_paddle.move(up)

        return True

    def render(self, draw_score=True, draw_hits=False):
        self.win.fill(BLACK)

        self.render_divider()

        if draw_score:
            render_score(self.win, self.left_score, self.right_score)

        if draw_hits:
            self.render_hits()

        for paddle in [self.left_paddle, self.right_paddle]:
            paddle.render_paddle(self.win)

        self.ball.render_ball(self.win)

    def loop(self):

        self.ball.move()
        self.handle_collision()

        if self.ball.x < 0:
            self.ball.reset()
            self.right_score += 1
        elif self.ball.x > self.win_width:
            self.ball.reset()
            self.left_score += 1

        game_info = GameInfo(self.left_hits, self.right_hits, self.left_score, self.right_score)

        return game_info
    
    def reset(self):
        self.ball.reset()
        self.left_paddle.reset()
        self.right_paddle.reset()
        self.left_score = 0
        self.right_score = 0
        self.left_hits = 0
        self.right_hits = 0