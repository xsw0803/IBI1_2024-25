import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

'''
Create a size of 10*10 and all assign these points as zero.
'''
size = 100
population = np.zeros((size, size))  

'''
To make a pandemic outbreak as random.choice from the set of size and select 2.
population[] is a two-demension expression to define the point with x and y ticks.
This means the point(0,1) is Infected as 1.
0: Susceptible, 1: Infected, 2: Recovered'
'''
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1

'''
The beta parameter is the infectious rate and gamma is the recovery rate.
Time steps is 100, meaning we can have a picture everyday.
'''
beta = 0.3
gamma = 0.05
time_steps = 100

'''
Draw a figure as dpi is 150.
'''
plt.figure(figsize=(6,4), dpi=150)

'''
Create a for loop to list all the time steps:
    
    infected_location is where the stimulation started and infected_list is a list which
    can include all x and y as points, not one-dimension numbers.
'''
for t in range(time_steps + 1):
    infected_location = np.where(population == 1)
    infected_list = list(zip(infected_location[0], infected_location[1]))
    
    ''''
    Create a new list for new_infections.
    
    For the point in the infected_list, x can go further or not go or go back with one point,
    this means x can infect one person.
    
    After that,
    For the point in the infected_list, y can go up or not go or go down with one point,
    this means y can infect one person.
    
    If x and y both not go, means noone is infected, then continue the loop until there's an infection.
    If x and y do change, then plus the change as nx and ny.
    '''
    new_infections = []
    for x, y in infected_list:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  
                nx, ny = x + dx, y + dy

                '''
                To determine the infection size is in the size.
                If nx is smaller than x size and y is smaller than y size:
                    In this situation, if the point represneted nx and ny is susceptible,
                     In this situation, if the random np points here is smaller than beta rate,
                        then the point (nx,ny) is infected.
                '''
                if 0 <= nx < size and 0 <= ny < size:
                    if population[nx, ny] == 0:  
                        if np.random.rand() < beta:
                            new_infections.append((nx, ny))
    
    '''
    recovery_mask is a boolean value and only when they are all true,
    which means the person is 1 as infected and random value is smaller than gamma,
    the change the point of recovery_mask into recoveried point.
    '''
    recovery_mask = (population == 1) & (np.random.rand(size, size) < gamma)
    population[recovery_mask] = 2
    
    '''
    For point in new_infections,
    Turn the point as infected person.
    '''
    for x, y in new_infections:
        population[x, y] = 1

    '''
    Draw and show the plot as population points and add the title.
    '''
    if t == time_steps:
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Spatial SIR for time step {t}", fontsize = 12)

plt.show()