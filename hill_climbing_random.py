import random
from optimization_problem import ThreePartitionProblem


def hill_climbing_random(problem):
    current_solution = problem.generate_random_solution()
    current_objective_value = problem.objective_function(current_solution)

    while True:
        neighbors = problem.get_neighborhood(current_solution)
        random_neighbor = random.choice(neighbors)
        random_neighbor_value = problem.objective_function(random_neighbor)

        if random_neighbor_value < current_objective_value:
            current_solution = random_neighbor
            current_objective_value = random_neighbor_value
        else:
            break

    return current_solution, current_objective_value


if __name__ == "__main__":
    numbers = [random.randint(1, 100) for _ in range(9)]
    problem = ThreePartitionProblem(numbers)
    best_solution, best_objective_value = hill_climbing_random(problem)
    print("Best Solution:", best_solution)
    print("Best Objective Value:", best_objective_value)