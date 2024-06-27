import random
from optimization_problem import ThreePartitionProblem


def one_point_crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 2)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


def two_point_crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(1, len(parent1)), 2))
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2


def swap_mutation(solution):
    new_solution = [list(group) for group in solution]
    group = random.choice(new_solution)
    i, j = random.sample(range(len(group)), 2)
    group[i], group[j] = group[j], group[i]
    return new_solution


def interchange_mutation(solution):
    new_solution = [list(group) for group in solution]
    group1, group2 = random.sample(new_solution, 2)
    i, j = random.randint(0, 2), random.randint(0, 2)
    group1[i], group2[j] = group2[j], group1[i]
    return new_solution


def genetic_algorithm(problem, population_size, generations, crossover_rate, mutation_rate, elite_size, crossover_method, mutation_method, termination_method):
    population = [problem.generate_random_solution() for _ in range(population_size)]
    best_solution = min(population, key=problem.objective_function)
    best_value = problem.objective_function(best_solution)
    no_improvement = 0

    convergence_curve = [best_value]

    for generation in range(generations):
        new_population = []

        #elita
        elities = sorted(population, key=problem.objective_function)[:elite_size]
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

        current_best = min(population, key=problem.objective_function)
        current_best_value = problem.objective_function(current_best)

        if current_best_value < best_value:
            best_solution = current_best
            best_value = current_best_value
            no_improvement = 0
        else:
            no_improvement += 1

        convergence_curve.append(best_value)

        if (termination_method == "no_improvement" and no_improvement >= 100) or \
                (termination_method == "generations" and generation >= generations -1):
            break

    return best_solution, best_value, convergence_curve


if __name__ == "__main__":
    numbers = [random.randint(1, 100) for _ in range(15)]
    problem = ThreePartitionProblem(numbers)
    best_solution, best_value, convergence_curve = genetic_algorithm(problem, population_size=50, generations=1000,
                                                                     crossover_rate=0.7, mutation_rate=0.1, elite_size=5,
                                                                     crossover_method="one_point", mutation_method="swap",
                                                                     termination_method="generations")
    print("Best Solutions:", best_solution)
    print("Best Objective Value:", best_value)






