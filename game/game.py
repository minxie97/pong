import pygame
from paddles import Paddle
from ball import Ball
from paddle_movement import handle_paddle_move
from collision import handle_collision
from score import render_score
import constants as c

pygame.init()

WINDOW = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("PONG")

def render_game(win, paddles, ball, left_score, right_score):
    win.fill(c.BLACK)

    render_score(win, left_score, right_score)

    for paddle in paddles:
        paddle.render_paddle(win)

    for i in range(10, c.HEIGHT, c.HEIGHT//24):
        if i % 2 == 1:
            continue
        else:
            pygame.draw.rect(win, c.WHITE, (c.WIDTH//2 - 5, i, 10, c.HEIGHT//24))

    ball.render_ball(win)

    pygame.display.update()

def main():
    running = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, c.HEIGHT//2 - c.PADDLE_HEIGHT//2, c.PADDLE_WIDTH, c.PADDLE_HEIGHT)
    right_paddle = Paddle(c.WIDTH - 10 - c.PADDLE_WIDTH, c.HEIGHT//2 - c.PADDLE_HEIGHT//2, c.PADDLE_WIDTH, c.PADDLE_HEIGHT)

    ball = Ball(c.WIDTH//2, c.HEIGHT//2, c.BALL_RADIUS)

    left_score = 0
    right_score = 0

    while running:
        clock.tick(c.FPS)
        render_game(WINDOW, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_move(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > c.WIDTH:
            left_score += 1
            ball.reset()

        game_over = False

        if left_score >= c.WIN:
            game_over = True
            win_text = "Left won!"
        elif right_score >= c.WIN:
            game_over = True
            win_text = "Right won!"

        if game_over:
            text = c.FONT.render(win_text, 1, c.WHITE)
            WINDOW.fill(c.BLACK)
            WINDOW.blit(text, (c.WIDTH//2 - text.get_width()//2, c.HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

    pygame.quit()

if __name__ == '__main__':
    main()