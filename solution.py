import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def render(win):
    win.fill(BLACK)
    pygame.display.update()

def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)
        render(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
    
    pygame.quit()

if __name__ == '__main__':
    main()