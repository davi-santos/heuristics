import numpy as np

class Cromossomo:
    def __init__(self, L=12):
        self.gene = np.zeros(L, dtype=np.int)
        self.fitness = 0

    def printInfo(self):
        print(f'gene: {self.gene}')
        print(f'fitness: {self.fitness}')

class GA:
    def __init__(self, popsize=10, max_generations=10):
        self.popsize = popsize
        self.max_generations = max_generations
        self.population = []

    def initPopulation (self):
        gene = np.zeros()
        