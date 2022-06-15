# PONG

A playable version of the classic PONG game complete with an AI opponent trained using the NEAT (Neural Evolution of Augmenting Topologies) genetic algorithm. 

## How to Play
1. First clone the repository
2. Check that you have Python 3
3. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` on your terminal or command prompt
4. Run the file with `python3 play.py`
5. Try and beat the AI!

## How it Works
The Pong AI is created using a algorithm that takes a population of 50 neural networks with different "genomes" and puts them into the Pong game to play against each other. Each genome is rated for their fitness, which is calculated through how many hits the genome achieves, how long a match lasts, and amount of movement. The best performing genomes from the generation are taken and bred to create a population for the next generation. This generational cycle repeats until a genome meets the determined fitness threshold, and that genome is saved as the opponent AI. 

The opponent AI controls the right paddle while the user plays with the right paddle. Control the user paddle using `w` for up and `s` for down.



## Acknowledgements
* [PyGames](https://www.pygame.org/news)
* [NEAT-Python](https://neat-python.readthedocs.io/en/latest/neat_overview.html)
* [Efficient Evolution of Neural Network Topologies by Kenneth O. Stanley and Risto Miikkulainen](http://nn.cs.utexas.edu/downloads/papers/stanley.cec02.pdf)
* [NEAT Wikipedia](https://en.wikipedia.org/wiki/Neuroevolution_of_augmenting_topologies)
* [NEAT: An Awesome Approach to NeuroEvolution by Hunter Heidenreich](https://towardsdatascience.com/neat-an-awesome-approach-to-neuroevolution-3eca5cc7930f)
* Special thanks to the awesome YouTubers [Tech With Tim](https://www.youtube.com/c/TechWithTim) and [Finn Eggers](https://www.youtube.com/channel/UCaKAU8vQzS-_e5xt7NSK3Xw)
