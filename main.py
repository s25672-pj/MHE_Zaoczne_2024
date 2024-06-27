# import sys
import argparse
import random
from optimization_problem import ThreePartitionProblem
from brute_force import brute_force
from hill_climbing import hill_climbing
from hill_climbing_random import hill_climbing_random
from tabu_search import tabu_search
from simulated_annealing import simulated_annealing
from genetic_algorithm import genetic_algorithm
from parallel_genetic_algorithm import genetic_algorithm_parallel
from island_genetic_algorithm import island_genetic_algorithm


def parse_args():
    parser = argparse.ArgumentParser(description="Rozwiązanie problemu")
    parser.add_argument('algorithm', choices=['brute_force', 'hill_climbing', 'hil_climbing_random', 'tabu_search',
                                              'simulated_annealing', 'genetic_algorithm', 'parallel_genetic_algorithm',
                                              'island_genetic_algorithm'],
                        help='Algorytmy do rozwiazania problemu')
    parser.add_argument('--file', type=str, help="Sciezka do pliku zawierajacy liczby")
    parser.add_argument('--seed', type=int, default=None, help="Losowe ziarno")
    parser.add_argument('--tabu_size', type=int, default=10, help="Rozmiar listy tabu")
    parser.add_argument('--max_iterations', type=int, default=100, help="Liczba iteracji")
    parser.add_argument('--initial_temperature', type=float, default=100, help="Temperatura inicjująca")
    parser.add_argument('--cooling_rate', type=float, default=0.99, help="Stopien chlodzenia")
    parser.add_argument('--min_temperature', type=float, default=0.1, help="Minimalna temperatura")
    parser.add_argument('--population_size', type=int, default=50, help="Rozmiar populacji")
    parser.add_argument('--generations', type=int, default=1000, help="Liczba generacji")
    parser.add_argument('--crossover_rate', type=float, default=0.7, help="Stopien krzyzowania")
    parser.add_argument('--mutation_rate', type=float, default=0.1, help="Stopien mutacji")
    parser.add_argument('--elite_size', type=int, default=5, help="Rozmiar elity")
    parser.add_argument('--crossover_method', choices=['one_point', 'two_point'], default='one_point', help="Metoda krzyzowania")
    parser.add_argument('--mutation_method', choices=['swap', 'interchange'], default='swap', help="metoda mutacji")
    parser.add_argument('--termination_method', choices=['generations', 'no_improvement'], default='generations', help="metoda terminacji")
    parser.add_argument('--num_islands', type=int, default=5, help="liczba wysp")
    parser.add_argument('--migration_interval', type=int, default=10, help="licznik migracji")
    parser.add_argument('--migration_rate', type=int, default=2, help="wspolczynik migracji")
    return parser.parse_args()


def load_numbers(file_path):
    with open(file_path, 'r') as f:
        line = f.readline().strip()
        numbers = [int(num) for num in line.split(',')]
    return numbers


def main():
    args = parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    if args.file:
        numbers = load_numbers(args.file)
    else:
        numbers = [random.randint(1, 100) for _ in range(9)]

    problem = ThreePartitionProblem(numbers)

    if args.algorithm == 'brute_force':
        solution, value, convergence_curve = brute_force(problem)
    elif args.algorithm == 'hill_climbing':
        solution, value, convergence_curve = hill_climbing(problem)
    elif args.algorithm == 'hill_climbing_random':
        solution, value, convergence_curve = hill_climbing_random(problem)
    elif args.algorithm == 'tabu_search':
        solution, value, convergence_curve = tabu_search(problem, args.tabu_sice, args.max_iterations)
    elif args.algorithm == 'simulated_annealing':
        solution, value, convergence_curve = simulated_annealing(problem, args.initial_temperature, args.cooling_rate, args.min_temperature, args.max_iterations)
    elif args.algorithm == 'genetic_algorithm':
        solution, value, convergence_curve = genetic_algorithm(problem, args.population_size, args.generations, args.crossover_rate,
                                            args.mutation_rate, args.elite_size, args.crossover_method,
                                            args.mutation_method, args.termination_method)
    elif args.algorithm == 'parallel_genetic_algorithm':
        solution, value, convergence_curve = genetic_algorithm_parallel(problem, args.population_size, args.generations,
                                                      args.crossover_rate, args.mutation_rate, args.elite_size,
                                                      args.crossover_method, args.mutation_method,
                                                      args.termination_method)
    elif args.algorithm == 'island_genetic_algorithm':
        solution, value, convergence_curve = island_genetic_algorithm(problem, args.population_size, args.generations,
                                                   args.crossover_rate, args.mutation_rate, args.elite_size,
                                                   args.crossover_method, args.mutation_method,
                                                   args.termination_method, args.num_islands, args.migration_interval,
                                                   args.migration_rate)
    else:
        print("Nieznany algorytm")
        return

    print("Najlepsze rozwiązanie: ", solution)
    print("Najlepsza wartosc: ", value)


if __name__ == "__main__":
    main()