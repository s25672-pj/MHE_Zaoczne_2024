from itertools import permutations
from optimization_problem import ThreePartitionProblem
import random


def brute_force(problem):

    best_solution = None
    best_objective_value = float('inf')
    convergence_curve = []

    for perm in permutations(problem.numbers):
        solution = [list(perm[i:i + 3]) for i in range(0, len(perm), 3)]
        objective_value = problem.objective_function(solution)
        if objective_value < best_objective_value:
            best_solution = solution
            best_objective_value = objective_value

        convergence_curve.append(best_objective_value)

    return best_solution, best_objective_value, convergence_curve


if __name__ == "__main__":
    numbers = [random.randint(1, 100) for _ in range(9)]
    problem = ThreePartitionProblem(numbers)
    best_solution, best_objective_value, convergence_curve = brute_force(problem)
    print("Best Solution:", best_solution)
    print("Best Objective Value:", best_objective_value)
