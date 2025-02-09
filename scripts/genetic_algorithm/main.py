# Created on Feb 7th, 2025
# Author: Uriel Garcilazo Cruz

# Information domain and data characterization

'''
Problem description:
    Genetic algorithms are heuristic approaches to multidimensional complexity problems.
    They are inspired by the process of natural selection. This program provides an example 
    for the optimization of a simple mathematical function using a simple genetic algorithm.
    
    Goals:
    - Given an optimality criterion O_c, and a population of N units $u$:
        - mutate and impose selective pressure on each $u \in U_{i=1}^N$ the population to maximize the average fitness of 
        the population.
        
    - Inputs:
        - MUTATION_STRENGTH: float, << 1
        - N: int
        - OPTIMALITY_CRITERION: int
        - UNIT: class object with parameters:
            - x: float
            - y: float
            - fitness: float
        - GENERATION: class object with parameters:
            - POPULATION: [UNIT, ..., n=N]
            - AVG_UNIT_FT: float
        - GENERATIONS: [GENERATION, ...]
        - EPSILON: float << 1
        - SAMPLE_FITNESS_SIZE: int
        - GENERATION_SEED: [UNIT, ..., n=SAMPLE_FITNESS_SIZE]
    - Outputs:
        - BEST_AVERAGE_UNIT_PARAMETERS: (float, float)
        
    
    - Instance models (functions):
        optimality_function(): 
            - Uses an optimality criterion function and OPTIMALITY_CRITERION parameter to calculate UNIT.fitness
    
'''

# DATA DEFINITIONS


from random import random 
from random import choice


# DD. MUTATION_STRENGTH
# MUTATION_STRENGTH = float
# interp. CONSTANT. magnitude of mutation applied to UNIT.attributes in a new GENERATION.POPULATION
MUTATION_STRENGTH = 0.001

# DD. SAMPLE_FITNESS_SIZE
# SAMPLE_FITNESS_SIZE = int
# interp. CONSTANT. the number of units in the seed used to create a new generation
SAMPLE_FITNESS_SIZE = 1

# DD. EPSILON
# EPSILON = float
# interp. CONSTANT. theshold value used in the stopping condition of the genetic algorithm
EPSILON = 0.000001

# DD. OPTIMALITY_CRITERION
# OPTIMALITY_CRITERION = int
# interp. the target value for the optimality function
OPTIMALITY_CRITERION = 4


# DD. N
# N = int
# interp. CONSTANT: the number of UNIT in a GENERATION.POPULATION
N = 500

# FD. optimality_function()
# Signature: UNIT.x, UNIT.y -> UNIT.fitness
# Purpose: Calculate the fitness of a UNIT given the OPTIMALITY_CRITERION
def optimality_function(x, y):
    _fn = x**4 + y**4
    fitness = - abs(OPTIMALITY_CRITERION - _fn)
    return fitness

# DD. GENERATIONS_PASSED
# genpass = int
# interp. keep track of how many GENERATIONs have passed
genpass = 0

# DD. UNIT
# unit = Unit(x, y, fitness)
# interp. fundamental unit subject to selective pressure
class Unit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fitness = 0


# DD. GENERATED_SEED
# generated_seed = [UNIT, ..., n=SAMPLE_FITNESS_SIZE]
# interp. a list of units with random x and y values
_founder_population = []    # generated seed at time t=0
for _ in range(SAMPLE_FITNESS_SIZE):
    _founder_population.append(Unit(random(), random()))


# DD. GENERATION
# generation = Generation()
# interp. a generation of units with a population and average fitness
class Generation:
    def __init__(self, generated_seed):
        self.population = self.generate_population(generated_seed)        
        self.avg_unit_ft = self.calculate_population_fitness()
        
    
    # FD. calculate_population_fitness()
    # Signature: POPULATION -> float
    # purp. calculate the average fitness value for self.POPULATION
    def calculate_population_fitness(self):
        return sum([unit.fitness for unit in self.population])/len(self.population)
    
    # FD. generate_population()
    # Signature: GENERATION_SEED -> GENERATION.POPULATION
    # Purpose: Generate a new population for a given GENERATION
    def generate_population(self, generation_seed):
        _population = []
        # Do N times
        for n in range(N):
            # Sample an element from the generation seed
            _sample = choice(generation_seed)
            # mutate the sample's attributes
            if n == 0:  #keep the first individual with same parameters to avoid doing worse due to mutation
                _x = _sample.x
                _y = _sample.y
            else:
                _x = _sample.x + (random() * MUTATION_STRENGTH * choice([1,-1]))
                _y = _sample.y + (random() * MUTATION_STRENGTH * choice([1,-1]))
            # Generate a new unit
            new_unit = Unit(_x,_y)
            # Calculate the fitness of the new unit
            new_unit.fitness = optimality_function(_x, _y)
            # Add the unit to the population
            _population.append(new_unit)
        return _population
    
    # FD. calculate_average_fitness()
    # Signature: GENERATION.POPULATION -> (float, ..., n=parameters in UNIT)
    # Purpose: Calculate the average value of the parameters in the population
    def calculate_average_fitness(self):
        average_x = sum([unit.x for unit in self.population])/len(self.population)
        average_y = sum([unit.y for unit in self.population])/len(self.population)
        return (average_x, average_y)


# DD. DELTA_GENERATION
# delta_gen = float | None
# purp. difference between the average fitness of the population at t-1 and t
delta_gen = None



# ALgorithm and implementation
'''
1. Initialize the GENERATION_SEED by generating UNIT for n=SAMPLE_FITNESS_SIZE, where each UNIT has random x and y values.
2. While DELTA_GENERATION is greater than EPSILON:
    - Sort POPULATION by UNIT.fitness
    - Set GENERATION_SEED to POPULATION[0:SAMPLE_FITNESS_SIZE]
    - Generate a new GENERATION:
        - POPULATION = generate_population(GENERATION_SEED)
    - Calculate DELTA_GENERATION between OPTIMALITY_CRITERION and GENERATION at time t
3. Return the BEST_AVERAGE_UNIT
'''

def genetic_algorithm(generation_0):
    delta_gen = None
    generation_t = generation_0
    while (delta_gen is None) or abs(delta_gen) >= EPSILON:
        # gen_t_avg_fitness = generation_t.avg_unit_ft
        generation_t.population.sort(key=lambda x: x.fitness,reverse=True)
        # print([unit.fitness for unit in generation_t.population[0:4]])
        generated_seed = generation_t.population[0:SAMPLE_FITNESS_SIZE]
        generation_t = Generation(generated_seed)
        # delta_gen = generation_t1.avg_unit_ft - generation_t.avg_unit_ft
        # delta_gen = OPTIMALITY_CRITERION - generation_t.population[0].fitness
        delta_gen = abs(generation_t.population[0].fitness)
    best_average_unit_parameters = generation_t.calculate_average_fitness()
    [print(unit.fitness) for unit in generation_t.population]
    # best_average_unit_parameters = (generation_tp1.population[0].x, generation_tp1.population[0].y)
    return (best_average_unit_parameters)


if __name__ == "__main__":
    generation_0 = Generation(_founder_population)
    print(genetic_algorithm(generation_0))