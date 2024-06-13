import random
from optimization_problem import ThreePartitionProblem


def tabu_search(problem, tabu_size, max_iterations):
    current_solution = problem.generate_random_solution()
    current_objective_value = problem.objective_function(current_solution)

    best_solution = current_solution
    best_objective_value = current_objective_value

    tabu_list = []

    for _ in range(max_iterations):
        neighbors = problem.get_neighborhood(current_solution)
        neighbors = [(neighbor, problem.objective_function(neighbor)) for neighbor in neighbors]
        neighbors.sort(key=lambda x: x[1])

        for neighbor, objective_value in neighbors:
            if neighbor not in tabu_list:
                current_solution = neighbor
                current_objective_value = objective_value
                if current_objective_value < best_objective_value:
                    best_solution = current_solution
                    best_objective_value = current_objective_value
                break

        tabu_list.append(current_solution)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    return best_solution, best_objective_value


if __name__ == "__main__":
    numbers = [random.randint(1, 100) for _ in range(9)]
    problem = ThreePartitionProblem(numbers)
    best_solution, best_objective_value = tabu_search(problem, tabu_size=10, max_iterations=100)
    print("Best Solution:", best_solution)
    print("Best Objective Value:", best_objective_value)
