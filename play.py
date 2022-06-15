from game import Game
import pygame
import neat
import os
import time
import pickle

class Pong:
    def __init__(self):
        self.game = Game()
        self.ball = self.game.ball
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle

    def play_ai(self, net):
        clock = pygame.time.Clock()

        run = True

        while run:
            clock.tick(90)
            self.game.loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            output = net.activate((self.right_paddle.y, abs(self.right_paddle.x - self.ball.x), self.ball.y))
            decision = output.index(max(output))

            if decision == 1:
                self.game.move_paddle(left=False, up=True)
            elif decision == 2:
                self.game.move_paddle(left=False, up=False)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_paddle(left=True, up=True)
            elif keys[pygame.K_s]:
                self.game.move_paddle(left=True, up=False)

            self.game.render(draw_score=True, draw_hits=False)
            pygame.display.update()

    def train_ai(self, genome1, genome2, config, draw=False):
        run = True
        start_time = time.time()

        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)
        self.genome1 = genome1
        self.genome2 = genome2

        max_hits = 50

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True

            game_info = self.game.loop()

            self.move_ai_paddles(net1, net2)

            if draw:
                self.game.render(draw_score=False, draw_hits=True)

            pygame.display.update()

            duration = time.time() - start_time
            if game_info.left_score == 1 or game_info.right_score == 1 or game_info.left_hits >= max_hits:
                self.calculate_fitness(game_info, duration)
                break

        return False

    def move_ai_paddles(self, net1, net2):

        players = [(self.genome1, net1, self.right_paddle, False), (self.genome2, net2, self.left_paddle, True)]
        for (genome, net, paddle, left) in players:
            output = net.activate((paddle.y, abs(paddle.x - self.ball.x), self.ball.y))
            decision = output.index(max(output))

            valid = True
            if decision == 0:
                genome.fitness -= 0.01
            elif decision == 1:
                valid = self.game.move_paddle(left=left, up=True)
            else:
                valid = self.game.move_paddle(left=left, up=False)

            if not valid:
                genome.fitness -= 1

    def calculate_fitness(self, game_info, duration):
        self.genome1.fitness += game_info.left_hits + duration
        self.genome2.fitness += game_info.right_hits + duration

def eval_genomes(genomes, config):
    for i, (genome_id1, genome1) in enumerate(genomes):
        print(round(i/len(genomes) * 100), end=" ")
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[min(i+1, len(genomes) - 1):]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            pong = Pong()

            force_quit = pong.train_ai(genome1, genome2, config, draw=True)
            if force_quit:
                quit()

def run_neat(config):
    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-49')
    #p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes)
    with open("evil.pickle", "wb") as f:
        pickle.dump(winner, f)

def play_evil_network(config):
    with open("evil.pickle", "rb") as f:
        winner = pickle.load(f)
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    pong = Pong()
    pong.play_ai(winner_net)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                        neat.DefaultSpeciesSet, neat.DefaultStagnation,
                        config_path)

    #run_neat(config)
    play_evil_network(config)