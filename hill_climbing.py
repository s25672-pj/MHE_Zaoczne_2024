import random
from optimization_problem import ThreePartitionProblem


def hill_climbing(problem):
    current_solution = problem.generate_random_solution()
    current_objective_value = problem.objective_function(current_solution)

    while True:
        neighbors = problem.get_neighborhood(current_solution)
        best_neighbor = min(neighbors, key=problem.objective_function)
        best_neighbor_value = problem.objective_function(best_neighbor)

        if best_neighbor_value < current_objective_value:
            current_solution = best_neighbor
            current_objective_value = best_neighbor_value
        else:
            break

        return current_solution, current_objective_value


if __name__ == "__main__":
        numbers = [random.randint(1, 100) for _ in  range(9)]
        problem = ThreePartitionProblem(numbers)
        best_solution, best_objective_value = hill_climbing(problem)
        print("Best Solution:", best_solution)
        print("Best Objective Value:", best_objective_value)

