# genetic-algorithm-TSP

This project implements a genetic algorithm to find an approximate solution to the Traveling Salesman Problem (TSP).

## Overview

The Traveling Salesman Problem involves finding the shortest possible route that visits a set of cities exactly once and returns to the origin city. This NP-hard problem is tackled using a genetic algorithm that evolves potential solutions over multiple generations.

## File Structure


```
data_generation.py        # Handles random city generation and distance matrix calculation  
tsp.py                    # Core implementation of the genetic algorithm  
plotting.py               # Visualization functions for results  
demo.py                   # Main execution script to demonstrate the algorithm

```

## Algorithm Details

### Genetic Algorithm Parameters

- **Population Size**: Number of individuals (solution candidates) in each generation
- **Mutation Probability**: Chance for random mutations in chromosomes
- **Elitism Rate**: Percentage of best individuals preserved in each generation
- **Reproduction Rate**: Percentage of individuals that participate in producing offspring
- **Max Generations**: Maximum number of generations for algorithm termination

### Implementation Components

#### Individual Class
Represents a single solution candidate with:
- Chromosome: A permutation of cities representing a possible route
- Fitness: The total distance of the route (lower is better)

#### Genetic Operators
- **Ordered Crossover**: Creates offspring by combining segments from parent routes
- **Mutation**: Swaps random cities to introduce variation
- **Selection**: Selects fitter individuals for reproduction

## Example Output

The algorithm provides:
1. The best route found (optimal or near-optimal city visitation order)
2. The fitness value (total distance)
3. Visualization of fitness improvement over generations
4. Visual representation of the optimal route
