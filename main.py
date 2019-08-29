import GeneticAlgorithm as ga
import numpy as np

def main():
    L = 12
    popsize = 10
    gene = np.zeros(L, dtype=np.int)
    gene[gene.size-1] = 1

    for i in range(popsize):
        gene = np.roll(gene,-1)
        print(gene)

if __name__ == "__main__":
    main()