import numpy as np
import matplotlib.pyplot as plt
import random

POPULATION_SIZE = 30
NUM_GENERATIONS = 14
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.3
QUANTITY_OF_ITERATIONS = 40
WEIGHT = 15


def get_items():
    items_matrix = np.zeros((10, 2))
    items_matrix[:, 0] = np.random.randint(0, 11, size=10) #ценность
    items_matrix[:, 1] = np.random.randint(1, 11, size=10) #вес
    
    print(items_matrix)
    return items_matrix


def generate_chromosome():
    return [random.randint(0, 1) for _ in range(10)]


def generate_population():
    return [generate_chromosome() for _ in range(POPULATION_SIZE)]


def fitness_function(chromosome, items):
    total_value = 0
    total_weight = 0
    
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_value += items[i, 0]
            total_weight += items[i, 1]
    
    if total_weight > WEIGHT:
        total_value = total_value - 10 * (total_weight - WEIGHT)
    
    return total_value
   
       
def crossover(parant_1, parant_2):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, len(parant_1)-1)
        child_1 = parant_1[:crossover_point] + parant_2[crossover_point:]
        child_2 = parant_2[:crossover_point] + parant_1[crossover_point:]
        
        return child_1, child_2
    
    else:
        return parant_1, parant_2
    

def mutate(chromosome):
    size = len(chromosome)
    if random.random() < MUTATION_RATE:
        mutate_point = random.randint(0, size)
        for i in range(size):
            if i == mutate_point:
                if chromosome[i] == 0:
                    chromosome[i] = 1
                else:
                    chromosome[i] = 0
            
    return chromosome
    
       
def tournament_selection(population, items):
    num_pretendents = 5
    pretendents = [random.choice(population) for _ in range(num_pretendents)]
    values_pretendents = [fitness_function(chromosome, items) for chromosome in pretendents]
        
    best_value = values_pretendents.index(max(values_pretendents))
    
    return pretendents[best_value]


def show_best_chromosome(population, items):
    fitness_values = [fitness_function(chromosome, items) for chromosome in population]
    
    best_value = fitness_values.index(max(fitness_values))
    print(f'\nЛучшая комбинация: {population[best_value]}')
    print(f'Ценность: {fitness_values[best_value]}')
    
    
      
def main():
    items = get_items()
    population = generate_population()
    
    best_fitness_progress = []
    
    i = 0
    while i < QUANTITY_OF_ITERATIONS:
        parant_1 = tournament_selection(population, items)
        parant_2 = tournament_selection(population, items)
        
        child_1, child_2 = crossover(parant_1, parant_2)
        
        child_1 = mutate(child_1)
        child_2 = mutate(child_2)
        
        
        population.extend([child_1, child_2])
        population.sort(key=lambda chromosome: fitness_function(chromosome, items))
        population = population[-POPULATION_SIZE:]
        
        best_fitness_progress.append(max([fitness_function(chromosome, items) for chromosome in population]))
        
        
        i+=1    
        
    
       
    show_best_chromosome(population, items) 
    
    plt.plot(best_fitness_progress)
    plt.title('Прогресс лучшего значения за поколения')
    plt.xlabel('Итерация')
    plt.ylabel('Лучшее значение')
    plt.show()   

main()