import numpy as np
import math
import random

class Cromossomo:
    def __init__(self, gene):
        self.gene = np.array(gene, dtype = np.int)
        self.fitness = 0
    
    def setFitness(self):
        x_sup = 2
        x_inf = -1
        
        #getting the indices of gene where values equals 1
        aux = np.where(self.gene == 1)
        
        #sum of 2**i elements
        aux = np.sum([2**i for i in aux])
        x = (aux)/(2**len(self.gene))*(x_sup-x_inf)+x_inf
        self.fitness = x*math.sin(10*math.pi*x) + 2

    def printInfo(self):
        print(f'gene: {self.gene}')
        print(f'fitness: {self.fitness}')

class GA:
    def __init__(self, popsize=10, max_generations=2):
        self.popsize = popsize
        self.generation = 0
        self.max_generations = max_generations
        self.list_prob = []
        self.population = []
        self.mating_pool = []
        self.pc = 0.8
        self.pm = 0.01

    def initPopulation (self):
        #create 1 gene
        L = 12
        gene = np.zeros(L, dtype=np.int)
        gene[gene.size-1] = 1; gene[gene.size-3] = 1

        for i in range(self.popsize):
            cromossomo = Cromossomo(gene)
            cromossomo.setFitness()
            self.population.append(cromossomo)
            gene = np.roll(gene,-1)

        #sort individuals by fitness
        self.population = sorted(self.population, key = lambda cromo: cromo.fitness, reverse=True)
    
    def getProbabilityList(self):
        fitness_list = np.array([_.fitness for _ in self.population])
        total_fit = float(sum(fitness_list))
        self.list_prob = [f/total_fit for f in fitness_list]

    #roulette wheel selection
    def RWS(self, number):
        self.getProbabilityList()

        chosen = []
        for n in range(number):
            r = random.random()
            for (i, individual) in enumerate(self.population):
                if r <= self.list_prob[i]:
                    chosen.append(individual)
                    self.population.pop(i)
                    break
        return chosen

    def crossover(self):
        pass

    def printGA(self):
        print(f'Popsize: {self.popsize}')
        print(f'max generations: {self.max_generations}')
        print(f'Population:')
        for individual in self.population:
            individual.printInfo()