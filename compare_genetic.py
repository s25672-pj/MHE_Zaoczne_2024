import time
import tracemalloc
import random
import matplotlib.pyplot as plt
from genetic_algorithm import genetic_algorithm
from optimization_problem import ThreePartitionProblem


def run_experiment(method, problem, *args):
    tracemalloc.start()
    start_time = time.time()


    solution, value, convergence_curve = genetic_algorithm(problem, *args)

    end_time = time.time()
    memory_used = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    elapsed_time = end_time - start_time
    return solution, value, elapsed_time, memory_used, convergence_curve


def compare_genetic():
    numbers = [random.randint(1, 100) for _ in range(18)]
    problem = ThreePartitionProblem(numbers)

    methods = {
        "ga_one_point_swap_no_improvement": (50, 1000, 0.7, 0.1, 5, "one_point", "swap", "no_improvement"),
        "ga_one_point_interchange_no_improvement": (50, 1000, 0.7, 0.1, 5, "one_point", "interchange", "no_improvement"),
        "ga_one_point_swap_generations": (50, 1000, 0.7, 0.1, 5, "one_point", "swap", "generations"),
        "ga_one_point_interchange_generations": (50, 1000, 0.7, 0.1, 5, "one_point", "interchange", "generations"),
        "ga_two_point_swap_no_improvement": (50, 1000, 0.7, 0.1, 5, "two_point", "swap", "no_improvement"),
        "ga_two_point_interchange_no_improvement": (50, 1000, 0.7, 0.1, 5, "two_point", "interchange", "no_improvement"),
        "ga_two_point_swap_generations": (50, 1000, 0.7, 0.1, 5, "two_point", "swap", "generations"),
        "ga_two_point_interchange_generations": (50, 1000, 0.7, 0.1, 5, "two_point", "interchange", "generations")
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

    plt.figure(figsize=(12, 8))

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
    plt.xlabel('Generation/Iteration')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    compare_genetic()