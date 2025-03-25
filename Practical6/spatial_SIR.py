import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


size = 100
population = np.zeros((size, size))  # 0: Susceptible, 1: Infected, 2: Recovered

outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1

beta = 0.3
gamma = 0.05
time_steps = 100

plt.figure(figsize=(6,4), dpi=150)

for t in range(time_steps):
    
    infected_coords = np.where(population == 1)
    infected_list = list(zip(infected_coords[0], infected_coords[1]))
    
    new_infections = []
    for x, y in infected_list:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  
                nx, ny = x + dx, y + dy
                if 0 <= nx < size and 0 <= ny < size:
                    if population[nx, ny] == 0:  
                        if np.random.rand() < beta:
                            new_infections.append((nx, ny))
    
  
    recovery_mask = (population == 1) & (np.random.rand(size, size) < gamma)
    population[recovery_mask] = 2
    
    
    for x, y in new_infections:
        population[x, y] = 1
    
   
    if t in [0, 10, 50, 99]:
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Time Step {t}")

plt.tight_layout()
plt.savefig("spatial_SIR_plot.png", format="png")
plt.show()