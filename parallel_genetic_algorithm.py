import random

import numpy as np

from optimization_problem import ThreePartitionProblem
from multiprocessing import Pool
from genetic_algorithm import one_point_crossover, two_point_crossover,swap_mutation, interchange_mutation


def evaluate_population(problem, population):
    with Pool() as pool:
        fitness = pool.map(problem.objective_function, population)
    return fitness


def genetic_algorithm_parallel(problem, population_size, generations, crossover_rate, mutation_rate, elite_size,
                               crossover_method, mutation_method, termination_method):
    population = [problem.generate_random_solution() for _ in range(population_size)]
    fitness = evaluate_population(problem, population)
    best_solution = population[np.argmin(fitness)]
    best_value = min(fitness)
    no_improvement = 0

    for generation in range(generations):
        new_population = []

        #elita
        elities = [population[i] for i in np.argsort(fitness)[:elite_size]]
        new_population.extend(elities)

        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population, k=2)

            #krzyzowy
            if random.random() < crossover_rate:
                if crossover_method == "one_point":
                    child1, child2 = one_point_crossover(parent1, parent2)
                else:
                    child1, child2 = two_point_crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2

            #mutacja
            if random.random() < mutation_rate:
                if mutation_method == "swap":
                    child1 = swap_mutation(child1)
                else:
                    child1 = interchange_mutation(child1)
            if random.random() < mutation_rate:
                if mutation_method == "swap":
                    child2 = swap_mutation(child2)
                else:
                    child2 = interchange_mutation(child2)

            new_population.extend([child1, child2])

        population = new_population[:population_size]
        fitness = evaluate_population(problem, population)

        current_best_value = min(fitness)
        current_best = population[np.argmin(fitness)]

        if current_best_value < best_value:
            best_solution = current_best
            best_value = current_best_value
            no_improvement = 0
        else:
            no_improvement += 1

        if (termination_method == "no_improvement" and no_improvement >= 100) or \
                (termination_method == "generations" and generation >= generations - 1):
            break

    return best_solution, best_value


def main():
    numbers = [random.randint(1, 100) for _ in range(9)]
    problem = ThreePartitionProblem(numbers)
    best_solution, best_value = genetic_algorithm_parallel(problem, population_size=50, generations=1000,
                                                           crossover_rate=0.7, mutation_rate=0.1, elite_size=5,
                                                           crossover_method="one_point", mutation_method="swap",
                                                           termination_method="generations")
    print("Best Solutions:", best_solution)
    print("Best Objective Value:", best_value)

if __name__ == "__main__":
    main()