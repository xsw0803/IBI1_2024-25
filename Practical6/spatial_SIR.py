import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

size = 100
beta = 0.3
gamma = 0.05
time_step  = 100
population = np.zeros((size,size))
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1

def neighbor(x, y, new_infection):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:                
            if dx == 0 and dy == 0:
                continue
            nx = x + dx
            ny = y + dy
            if 0 <= nx < size and 0 <= ny < size:
                if population[nx, ny] == 0:
                    infection_list = np.random.choice([0,1], 1, p = [1-beta, beta])
                    if infection_list == 1:
                        new_infection.append((nx, ny))

def recover(population):
    infected_ones = np.where(population == 1)
    infected_list = list(zip(infected_ones[0],infected_ones[1]))
    for x, y in infected_list:
        recovery_list = np.random.choice([0,1], 1, p = [1-gamma, gamma])
        if recovery_list == 1:
            population[x, y] = 2

def infect(x, y):
    population[x, y] = 1

for i in range(time_step +1):
    recover(population)
    infected_ones = np.where(population == 1)
    infected_list = list(zip(infected_ones[0],infected_ones[1]))
    new_infection =[]
    for x, y in infected_list:
        neighbor(x, y)
    for x, y in new_infection:
        infect(x, y)
    
    print_times = [0, 10, 50, 100]
    if i in print_times:
        plt.subplot(2, 2, print_times.index(i) + 1)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Plot for time step as {i}")

plt.tight_layout()
plt.show()