import random
import math
from optimization_problem import ThreePartitionProblem


def simulated_annealing(problem, initial_temperature, cooling_rate, min_temperature, max_iterations):
    def temperature(t):
        return initial_temperature * (cooling_rate ** t)

    current_solution = problem.generate_random_solution()
    current_objective_value = problem.objective_function(current_solution)

    best_solution = current_solution
    best_objective_value = current_objective_value

    t = 0
    while temperature(t) > min_temperature and t < max_iterations:
        neighbor = problem.get_random_neighbor(current_solution)
        neighbor_objective_value = problem.objective_function(neighbor)

        delta = neighbor_objective_value - current_objective_value

        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / temperature(t)):
            current_solution = neighbor
            current_objective_value = neighbor_objective_value

            if current_objective_value < best_objective_value:
                best_solution = current_solution
                best_objective_value = current_objective_value

        t += 1

    return best_solution, best_objective_value


if __name__ == "__main__":
    numbers = [random.randint(1, 100) for _ in range(9)]
    problem = ThreePartitionProblem(numbers)
    best_solution, best_objective_value = simulated_annealing(problem, initial_temperature=100, cooling_rate=0.99, min_temperature=0.1, max_iterations=1000)
    print("Best Solution:", best_solution)
    print("Best Objective value:", best_objective_value)

