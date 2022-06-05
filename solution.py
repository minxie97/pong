import pygame
import constants as c

pygame.init()

WINDOW = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("PONG")

class Paddle:

    COLOR = c.WHITE
    VELO = c.PADDLE_VELO

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render_paddle(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VELO
        else:
            self.y += self.VELO

class Ball:
    MAX_VELO = c.BALL_VELO
    COLOR = c.WHITE

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_velo = self.MAX_VELO
        self.y_velo = 0

    def render_ball(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_velo
        self.y += self.y_velo

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
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_velo *= -1

def render_game(win, paddles, ball):
    win.fill(c.BLACK)

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

    while running:
        clock.tick(c.FPS)
        render_game(WINDOW, [left_paddle, right_paddle], ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_move(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

    pygame.quit()

if __name__ == '__main__':
    main()