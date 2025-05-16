import numpy as np

from data_generation import data_generation
from TSP import GA
from plotting import generate_plots

np.random.seed(50)

def main():
    """Run a demo of the TSP genetic algorithm and plot the result."""

    N = 20 # number of cities

    x, y, city_dict, distance_matrix = data_generation(N)

    params = {
        "population_size": 100,
        "mutation_rate": 0.1,
        "elitism": 0.05,
        "reproduction": 0.3,
        "max_gen": 1000
    }

    log = GA(**params, distance_matrix=distance_matrix, N=N, verbose=True)

    _, solution = log[-1]

    print('\nBEST SOLUTION FOUND:\n{}\n\nFITNESS:\n{:.3f}'.format(solution, solution.fitness))

    generate_plots(log, city_dict, N, x, y)

if __name__ == "__main__":
    main()