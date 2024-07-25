import random
import math

class Point:
    def __init__(self) -> None:
        self.x = random.randint(-100, 100)
        self.y = random.randint(-100, 100)

def dist(p1, p2):
    return float(math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2))

def fitness(route):
    total_distance = 0
    for i in range(1, len(route)):
        total_distance += dist(route[i - 1], route[i])
    return total_distance

def generate_individual(points):
    individual = points.copy()
    random.shuffle(individual)
    return individual

def crossover(parent1, parent2):
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(start + 1, len(parent1))

    child = [-1] * len(parent1)
    for i in range(start, end):
        child[i] = parent1[i]

    remaining_points = [p for p in parent2 if p not in child]
    j = 0
    for i in range(len(child)):
        if child[i] == -1:
            child[i] = remaining_points[j]
            j += 1

    return child

def mutate(route):
    idx1, idx2 = random.sample(range(len(route)), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

def solve(points, population_size=50, generations=100):
    population = [generate_individual(points) for _ in range(population_size)]

    for _ in range(generations):
        population.sort(key=lambda x: fitness(x))

        elite_size = int(0.2 * population_size)
        next_generation = population[:elite_size]

        while len(next_generation) < population_size:
            parent1 = random.choice(population[:elite_size])
            parent2 = random.choice(population[:elite_size])

            child = crossover(parent1, parent2)

            if random.random() < 0.2:
                child = mutate(child)

            next_generation.append(child)

        population = next_generation

    best_route = min(population, key=lambda x: fitness(x))
    return best_route

