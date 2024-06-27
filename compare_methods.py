import time
import tracemalloc
import random
import matplotlib.pyplot as plt
from optimization_problem import ThreePartitionProblem
from brute_force import brute_force
from hill_climbing import hill_climbing
from hill_climbing_random import hill_climbing_random
from tabu_search import tabu_search
from simulated_annealing import simulated_annealing
from genetic_algorithm import genetic_algorithm
from parallel_genetic_algorithm import genetic_algorithm_parallel
from island_genetic_algorithm import island_genetic_algorithm


def run_experiment(method, problem, *args):
    tracemalloc.start()
    start_time = time.time()

    if method == "brute_force":
        solution, value, convergence_curve = brute_force(problem)
    elif method == "hill_climbing":
        solution, value, convergence_curve = hill_climbing(problem)
    elif method == "hill_climbing_random":
        solution, value, convergence_curve = hill_climbing_random(problem)
    elif method == "tabu_search":
        solution, value, convergence_curve = tabu_search(problem, *args)
    elif method == "simulated_annealing":
        solution, value, convergence_curve = simulated_annealing(problem, *args)
    elif method == "genetic_algorithm":
        solution, value, convergence_curve = genetic_algorithm(problem, *args)
    elif method == "parallel_genetic_algorithm":
        solution, value, convergence_curve = genetic_algorithm_parallel(problem, *args)
    elif method == "island_genetic_algorithm":
        solution, value, convergence_curve = island_genetic_algorithm(problem, *args)
    else:
        raise ValueError(f"Nieznana metoda: {method}")

    end_time = time.time()
    memory_used = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    elapsed_time = end_time - start_time
    return solution, value, elapsed_time, memory_used, convergence_curve


def compare_methods():
    numbers = [random.randint(1, 100) for _ in range(9)]
    problem = ThreePartitionProblem(numbers)

    methods = {
        "brute_force": (),
        "hill_climbing": (),
        #"hill_climbing_random": (),
        "tabu_search": (10, 100),
        "simulated_annealing": (100, 0.99, 0.1, 1000),
        "genetic_algorithm": (50, 1000, 0.7, 0.1, 5, "one_point", "swap", "generations"),
        #"parallel_genetic_algorithm": (50, 1000, 0.7, 0.1, 5, "one_point", "swap", "generations"),
        "island_genetic_algorithm": (100, 1000, 0.7, 0.1, 5, "one_point", "swap", "generations", 5, 10, 2)
    }

    results = []

    for method, args in methods.items():
        print(f"Metoda {method}")
        solution, value, elapsed_time, memory_used, convergence_curve = run_experiment(method, problem, *args)
        results.append((method, solution, value, elapsed_time, memory_used, convergence_curve))
        print(f"{method}: Value = {value}, Time = {elapsed_time:.2f}s, memory = {memory_used / 10**6:.2f}MB")

    plot_results(results)
    plot_convergence(results)
    return results


def plot_results(results):
    methods = [result[0] for result in results]
    values = [result[2] for result in results]
    time = [result[3] for result in results]
    memories = [result[4] for result in results]

    plt.figure(figsize=(12,8))

    plt.subplot(2, 2, 1)
    plt.bar(methods, values)
    plt.title('Value')
    plt.xticks(rotation=45, ha="right")

    plt.subplot(2, 2, 2)
    plt.bar(methods, time)
    plt.title('Time')
    plt.xticks(rotation=45, ha="right")

    plt.subplot(2, 2, 3)
    plt.bar(methods, memories)
    plt.title('Memory')
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()


def plot_convergence(results):
    plt.figure(figsize=(12, 8))
    for result in results:
        method, _, _, _, _, convergence_curve = result
        plt.plot(convergence_curve, label=method)

    plt.title('Convergence Curves')
    plt.xlabel('Iteration/Generation')
    plt.ylabel('Value')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    compare_methods()