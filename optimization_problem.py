import random

class ThreePartitionProblem:
    def __init__(self, numbers):
        self.numbers = numbers
        self.m = len(numbers) // 3
        self.target_sum = sum(numbers) // 3

    def objective_function(self, solution):
        group_sums = [sum(group) for group in solution]
        return sum((self.target_sum - group_sum) ** 2 for group_sum in group_sums)

    def generate_random_solution(self):
        shuffled_numbers = random.sample(self.numbers, len(self.numbers))
        return [shuffled_numbers[i:i + 3] for i in range(0, len(shuffled_numbers), 3)]

    def get_neighborhood(self, solution):
        neighbors = []
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                for k in range(3):
                    for l in range(3):
                        neighbor = [list(group) for group in solution]
                        neighbor[i][k], neighbor[j][l] = neighbor[j][l], neighbor[i][k]
                        neighbors.append(neighbor)
        return neighbors

    def get_random_neighbor(self, solution):
        neighbor = [list(group) for group in solution]
        group1, group2 = random.sample(range(len(solution)), 2)
        index1, index2 = random.randint(0, 2), random.randint(0, 2)
        neighbor[group1][index1], neighbor[group2][index2] = neighbor[group2][index2], neighbor[group1][index1]
        return neighbor


if __name__ == "__main__":
    numbers = [random.randint(1, 100) for _ in range(9)]
    problem = ThreePartitionProblem(numbers)
    initial_solution = problem.generate_random_solution()
    print("Initial Solution:", initial_solution)
    print("Initial Objective Value:", problem.objective_function(initial_solution))
    neighbors = problem.get_neighborhood(initial_solution)
    print("Number of Neighbors:", len(neighbors))