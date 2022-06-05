import pygame
import constants as c
import random

pygame.init()

WINDOW = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("PONG")

FONT = pygame.font.Font("assets/ARCADECLASSIC.TTF", 50)

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

def handle_collision(ball, left_paddle, right_paddle):
    #ceiling and floor collision
    if ball.y + ball.radius >= c.HEIGHT:
        ball.y_velo *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_velo *= -1

    #paddle collision
    if ball.x_velo < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_velo *= -1

                middle_y = left_paddle.y + left_paddle.height//2
                diff_y = middle_y - ball.y
                reduction_factor = (left_paddle.height//2) / ball.VELO
                
                ball.y_velo = (diff_y / reduction_factor) * -1
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_velo *= -1

                middle_y = right_paddle.y + right_paddle.height//2
                diff_y = middle_y - ball.y
                reduction_factor = (right_paddle.height//2) / ball.VELO
                
                ball.y_velo = (diff_y / reduction_factor) * -1

def render_game(win, paddles, ball, left_score, right_score):
    win.fill(c.BLACK)

    left_score_text = FONT.render(f"{left_score}", 1, c.WHITE)
    right_score_text = FONT.render(f"{right_score}", 1, c.WHITE)
    win.blit(left_score_text, (c.WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (c.WIDTH * (3/4) - right_score_text.get_width()//2, 20))

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
            text = FONT.render(win_text, 1, c.WHITE)
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