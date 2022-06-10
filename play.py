import pygame
from game import Game
import neat
import os
import pickle
import time

class Play:
    def __init__(self):
        self.game = Game()
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball

    def play_ai(self, genome, config):

        net = neat.nn.FeedForwardNetwork.create(genome, config)

        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.game.move_paddle(left=False, up=True)

            if keys[pygame.K_DOWN]:
                self.game.move_paddle(left=False, up=False)

            output = net.activate((self.right_paddle.y, self.ball.y, abs(self.right_paddle.x - self.ball.x)))
            decision = output.index(max(output))

            if decision == 0:
                pass
            elif decision == 1:
                self.game.move_paddle(left=True, up=True)
            else:
                self.game.move_paddle(left=True, up=False)


            game_info = self.game.loop()
            self.game.render(draw_score=True, draw_hits=False)
            pygame.display.update()

        pygame.quit()

def play_ai(config):
    with open("ai/best.pickle", "rb") as f:
        winner = pickle.load(f)

    game = Play()
    game.play_ai(winner, config)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                        neat.DefaultSpeciesSet, neat.DefaultStagnation,
                        config_path)

    play_ai(config)