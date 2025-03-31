import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

'''
Generally speaking, I split this process into four steps.

First, to find the susceptible(0) neighbors of each infected person, and to randomly choose
those will be infected at beta rate.
Second, randomly choose recovered ones at gamma rate in infected population.
Fourth, infect those who selected to be infected(1).

Then, the for loop will run in time course to simulate the whole process.

However, to make sure the recently-infected person won't recover immediately, in the for loop,
the order of each step will change a little bit.
First, the infected ones should be found at first.
In each time step, the selected recover population will firstly recover and change to 2.
Then, the susceptible neighbor(0) will be found and select some of them waiting for infection.
Then, the selected ones will be infected(1).

After the for loop, I select four time steps like 0, 10, 50 and 100 to draw the plot
and let them show at the same time, to see the trendency of infection and recovery.
'''

# Define basic rates and values for SIR model.
# Make a point for pandemic outbreak to infect others.
size = 100
beta = 0.3
gamma = 0.05
time_step  = 100
population = np.zeros((size,size))
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1

# Define the function "neighrbour".
# In this function, I will find the susceptible neighbour for infected ones
# and append them into new_infection list to be infected.
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

# Define the "recover" function.                       
# In this function, I will recover infected ones in rate of gamma
# and make them into 2.
def recover(population, infected_list):
    for x, y in infected_list:
        recovery_list = np.random.choice([0,1], 1, p = [1-gamma, gamma])
        if recovery_list == 1:
            population[x, y] = 2

# Define the "infect" function.
# In this function, the susceptible ones in new_infection list will be infected as 1.
def infect(x, y):
    population[x, y] = 1

# Start for loop in time course to do whole simulation.
for i in range(time_step +1):
    # Find infected ones.
    infected_ones = np.where(population == 1)
    infected_list = list(zip(infected_ones[0],infected_ones[1]))
    # Recover some infected ones using recover function.
    recover(population, infected_list)
    # Create an empty list to store outputs of functions.
    new_infection =[]
    # Use for loop to find neighbours and new infections. Then infect them.
    for x, y in infected_list:
        neighbor(x, y, new_infection)
    for x, y in new_infection:
        infect(x, y)
    
    # Create a list of time steps.
    print_times = [0, 10, 50, 100]
    # Draw four pictures when the time step is in the list and create a subplot to show them all.
    if i in print_times:
        plt.subplot(2, 2, print_times.index(i) + 1)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Plot for time step as {i}")
        
# Adjust the illustration automatically.
plt.tight_layout()
plt.show()