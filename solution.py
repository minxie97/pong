import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

class Paddle:

    COLOR = WHITE
    VELO = 4

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


def render_game(win, paddles):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.render_paddle(win)

    for i in range(10, HEIGHT, HEIGHT//24):
        if i % 2 == 1:
            continue
        else:
            pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//24))

    pygame.display.update()

def handle_paddle_move(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VELO >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VELO + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VELO >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VELO + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


def main():
    running = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    while running:
        clock.tick(FPS)
        render_game(WINDOW, [left_paddle, right_paddle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_move(keys, left_paddle, right_paddle)

    
    pygame.quit()

if __name__ == '__main__':
    main()