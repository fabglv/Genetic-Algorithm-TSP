import random

# Individuals

class Individual:
    """A candidate solution with a tour and fitness score."""

    distance_matrix = None
    mutation_rate = None
    
    def __init__(self, chromosome):
        """Initialize with a chromosome and compute fitness."""
        self.chromosome = chromosome
        self.fitness = self.evaluate_fitness()
    
    def evaluate_fitness(self):
        """Compute total distance of the tour."""
        fitness = sum(
            Individual.distance_matrix[self.chromosome[i], self.chromosome[i + 1]]
            for i in range(len(self.chromosome) - 1)
        )
        fitness += Individual.distance_matrix[self.chromosome[-1], self.chromosome[0]]
        return fitness
    
    def __str__(self):
        """Return the tour as a string, starting from city 0."""
        chars = [str(gene) for gene in self.chromosome]
        for i in range(len(chars)):
            if chars[i] == '0':
                break
        chars = chars[i :] + chars[: i]
        return(','.join(chars))
    
    @classmethod
    def ordered_crossover(cls, parent1, parent2):
        """Create a child using ordered crossover."""
        chrom1 = parent1.chromosome
        chrom2 = parent2.chromosome
        start, end = sorted(random.sample(range(len(chrom1)), 2))
        slice_1 = chrom1[start:end + 1]
        remainder = [gene for gene in chrom2 if gene not in slice_1]
        child_chromosome = remainder[:start] + slice_1 + remainder[start:]
        child = cls(Individual.mutate(child_chromosome))
        return child

    @staticmethod
    def mutate(chromosome):
        """Randomly swap genes in the chromosome."""
        for i in range(len(chromosome)):
            if random.random() <= Individual.mutation_rate:
                j = random.randint(0, len(chromosome) - 1)
                chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
        return chromosome
    
# Auxiliary Functions

def random_population(population_size, N):
    """Create a random initial population of size `population_size`."""
    population = []
    for _ in range(population_size):
        chromosome = random.sample(range(N), N)
        population.append(Individual(chromosome))
    return population

def new_generation(parents, population_size):
    """Make a new gen using crossover from selected parents and mutations."""
    offspring = []
    for _ in range(population_size):
        parent_1, parent_2 = random.sample(parents, 2)
        child = Individual.ordered_crossover(parent_1, parent_2)
        offspring.append(child)
    return offspring

def nice_print(gen, individual):
    """Print gen info and best individual."""
    txt = "Gen: {} --- Chr: {} --- Fitness: {}".format(gen, individual, round(individual.fitness, 3)) 
    print(txt)

# Main Algorithm

def GA(population_size, mutation_rate, elitism, reproduction, max_gen, distance_matrix, N, verbose):
    """Run the genetic algorithm and return the log of best individuals per gen."""

    Individual.distance_matrix = distance_matrix
    Individual.mutation_rate = mutation_rate
    
    population = random_population(population_size, N)
    population = sorted(population, key = lambda x:x.fitness)

    gen = 1
    log = [(gen, population[0])]

    if verbose: 
        print('\nEVOLUTION:\n')
        nice_print(gen, population[0])

    while (gen < max_gen):

        gen += 1

        # Elitism: keeps top performers
        elite_size = int(elitism * population_size)
        elite = population[: elite_size]

        # Selection and offspring generation
        parents = population[:int(population_size * reproduction)]
        offspring_size = population_size - elite_size
        offspring = new_generation(parents, offspring_size)

        # New population
        population = elite + offspring
        population = sorted(population, key = lambda x:x.fitness)

        # Logging and optional output
        log.append((gen, population[0]))
        if verbose and gen % 10 == 0: nice_print(gen, population[0])

    return(log)