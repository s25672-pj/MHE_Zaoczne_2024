import random
import numpy as np
from optimization_problem import ThreePartitionProblem
from genetic_algorithm import one_point_crossover, two_point_crossover, swap_mutation, interchange_mutation


def evaluate_population(problem, population):
    return [problem.objective_function(individual) for individual in population]


def genetic_algorithm(problem, population_size, generations, crossover_rate, mutation_rate, elite_size,
                      crossover_method, mutation_method, termination_method):
    population = [problem.generate_random_solution() for _ in range(population_size)]
    fitness = evaluate_population(problem, population)
    best_solution = population[np.argmin(fitness)]
    best_value = min(fitness)
    no_improvement = 0

    convergence_curve = [best_value]

    for generation in range(generations):
        new_population = []

        # Elitism
        elites = [population[i] for i in np.argsort(fitness)[:elite_size]]
        new_population.extend(elites)

        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population, k=2)

            # Crossover
            if random.random() < crossover_rate:
                if crossover_method == "one_point":
                    child1, child2 = one_point_crossover(parent1, parent2)
                else:
                    child1, child2 = two_point_crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2

            # Mutation
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

        convergence_curve.append(best_value)

        if termination_method == "no_improvement" and no_improvement >= 100:
            break

    return population, fitness, convergence_curve


def island_genetic_algorithm(problem, population_size, generations, crossover_rate, mutation_rate, elite_size,
                             crossover_method, mutation_method, termination_method, num_islands, migration_interval,
                             migration_rate):
    island_size = population_size // num_islands
    islands = [
        genetic_algorithm(problem, island_size, generations // num_islands, crossover_rate, mutation_rate, elite_size,
                          crossover_method, mutation_method, termination_method) for _ in range(num_islands)]

    for generation in range(0, generations, migration_interval):
        migrants = []
        for island in islands:
            island_population, island_fitness, island_convergence = island
            best_indices = np.argsort(island_fitness)[:migration_rate]
            migrants.append([island_population[i] for i in best_indices])

        for i in range(num_islands):
            target_island_population, target_island_fitness, target_island_convergence = islands[i]
            source_island_population, source_island_fitness, source_island_convergence = islands[(i + 1) % num_islands]
            for j in range(min(migration_rate, len(source_island_population))):
                target_index = random.randint(0, len(target_island_population) - 1)
                target_island_population[target_index] = source_island_population[j]

        islands = [
            genetic_algorithm(problem, island_size, migration_interval, crossover_rate, mutation_rate, elite_size,
                              crossover_method, mutation_method, termination_method) for _ in range(num_islands)]


    best_solutions = []
    convergence_curve = []

    for island in islands:
        island_population, island_fitness, island_convergence = island
        best_index = np.argmin(island_fitness)
        best_solutions.append(island_population[best_index])
        convergence_curve.extend(island_convergence)

    best_solution = min(best_solutions, key=problem.objective_function)
    best_value = problem.objective_function(best_solution)

    return best_solution, best_value, convergence_curve



if __name__ == "__main__":
    numbers = [random.randint(1, 100) for _ in range(9)]
    problem = ThreePartitionProblem(numbers)
    best_solution, best_value, convergence_curve = island_genetic_algorithm(problem, population_size=100,
                                                                            generations=1000, crossover_rate=0.7,
                                                                            mutation_rate=0.1, elite_size=5,
                                                                            crossover_method="one_point",
                                                                            mutation_method="swap",
                                                                            termination_method="generations",
                                                                            num_islands=5, migration_interval=10,
                                                                            migration_rate=2)
    print("Best Solution:", best_solution)
    print("Best Objective Value:", best_value)
    print("Convergence Curve:", convergence_curve)
