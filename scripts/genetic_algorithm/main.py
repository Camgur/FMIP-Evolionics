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
        - EPSILON: float
        - SAMPLE_FITNESS_SIZE: int
        - GENERATION_SEED: [UNIT, ..., n=SAMPLE_FITNESS_SIZE]
    - Outputs:
        - BEST_AVERAGE_UNIT: UNIT
        
    
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
MUTATION_STRENGTH = 0.1

# DD. SAMPLE_FITNESS_SIZE
# SAMPLE_FITNESS_SIZE = int
# interp. CONSTANT. the number of units in the seed used to create a new generation
SAMPLE_FITNESS_SIZE = 10

# DD. EPSILON
# EPSILON = float
# interp. CONSTANT. theshold value used in the stopping condition of the genetic algorithm
EPSILON = 0.001

# DD. OPTIMALITY_CRITERION
# OPTIMALITY_CRITERION = int
# interp. the target value for the optimality function
OPTIMALITY_CRITERION = 4


# DD. N
# N = int
# interp. CONSTANT: the number of UNIT in a GENERATION.POPULATION
N = 100

# FD. optimality_function()
# Signature: UNIT.x, UNIT.y -> UNIT.fitness
# Purpose: Calculate the fitness of a UNIT given the OPTIMALITY_CRITERION
def optimality_function(x, y):
    _fn = x**4 + y**4
    fitness = abs(OPTIMALITY_CRITERION - _fn)
    return fitness

# # FD. generate_population()
# # Signature: GENERATION_SEED -> GENERATION.POPULATION
# # Purpose: Generate a new population of UNIT for next generation
# def generate_population(generation_seed):
    
#     return generation_seed



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
        self.population = self.generate_population(_founder_population)        
        self.avg_unit_ft = 0
        
    
    # FD. generate_population()
    # Signature: GENERATION_SEED -> GENERATION.POPULATION
    # Purpose: Generate a new population for a given GENERATION
    def generate_population(self, generation_seed):
        _population = []
        # Do N times
        for _ in range(N):
            # Sample an element from the generation seed
            _sample = choice(generation_seed)
            # mutate the sample's attributes 
            _x = _sample.x + (random() * MUTATION_STRENGTH * choice([1,-1]))
            _y = _sample.y + (random() * MUTATION_STRENGTH * choice([1,-1]))
            # Generate a new unit
            new_unit = Unit(_x,_y)
            # Calculate the fitness of the new unit
            new_unit.fitness = optimality_function(_x, _y)
            # Add the unit to the population
            _population.append(new_unit)
        return _population

generation_0 = Generation(_founder_population)


# ALgorithm and implementation
'''
1. Initialize the GENERATION_SEED by generating UNIT for n=SAMPLE_FITNESS_SIZE, where each UNIT has random x and y values.
2. While difference between the average fitness of the population at t-1 and t is greater than EPSILON:
    - Generate a new GENERATION:
        - POPULATION = generate_population(GENERATION_SEED)
    For each UNIT in GENERATION.POPULATION:
        - UNIT.fitness = optimality_function(UNIT,OPTIMALITY_CRITERION)
    - GENERATION.AVG_UNIT_FT = calculate the average UNIT.fitness for each UNIT in POPULATION
    - Sort POPULATION by UNIT.fitness
    - Set GENERATION_SEED to POPULATION[0:SAMPLE_FITNESS_SIZE]
'''
