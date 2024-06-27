import random
from optimization_problem import ThreePartitionProblem


def hill_climbing(problem):
    current_solution = problem.generate_random_solution()
    current_objective_value = problem.objective_function(current_solution)
    convergence_curve = [current_objective_value]

    while True:
        neighbors = problem.get_neighborhood(current_solution)
        best_neighbor = min(neighbors, key=problem.objective_function)
        best_neighbor_value = problem.objective_function(best_neighbor)
        if best_neighbor_value < current_objective_value:
            current_solution = best_neighbor
            current_objective_value = best_neighbor_value
            convergence_curve.append(current_objective_value)
            # print("Skok")
        else:
            break

    return current_solution, current_objective_value, convergence_curve


if __name__ == "__main__":
        numbers = [random.randint(1, 100) for _ in range(15)]
        problem = ThreePartitionProblem(numbers)
        best_solution, best_objective_value, convergence_curve = hill_climbing(problem)
        print("Best Solution:", best_solution)
        print("Best Objective Value:", best_objective_value)

