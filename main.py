import GeneticAlgorithm as ga
import numpy as np
import random

def main():
    temp = ga.GA()
    temp.initPopulation()

    while temp.generation < temp.max_generations:
        temp.RWS(5)
        temp.printGA()
        temp.generation += 1

    print(f'bora {temp.list_prob}')
    temp.printGA()

if __name__ == "__main__":
    main()