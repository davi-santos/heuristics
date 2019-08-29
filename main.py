import GeneticAlgorithm as ga
import numpy as np

def main():
    arr = np.zeros(12, dtype=np.int)
    arr[0] += 1

    for i in range(arr.size):
        print(arr)
        arr.roll(x, 1)
    print(arr)
        

if __name__ == "__main__":
    main()