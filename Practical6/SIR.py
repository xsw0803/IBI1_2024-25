import numpy as np
import matplotlib.pyplot as plt

'''
The total population is 10000.
The susceptible population is total number - infected number.
Innitial infected number is 1.
Initial recovered number is 1.

beta is the probability of infection and gamma is probabilty of recovery.
Create three separate lists for each population.
'''
N = 10000
S = N - 1
I = 1
R = 0

beta = 0.3
gamma = 0.05
S_list = [S]
I_list = [I]
R_list = [R]

'''
The time steps is 1000, meaning we take the stimulation for 1000 days.

Use for loop in tiem steps and caluculate the propobility as infection_p.

new_I is the new infected population. Achieve this by random.choice to assign 0/1 for infected and
not infected person in all susceptible population, with a infection propability as infection_p.
Then sum up all the values to get how many people are infected, because only 1 will be calculated
and 0 doesn't make sense.

Do the same for new_R, meaning the new population of recovered people.
'''

time_steps = 1000

for i in range(time_steps):
    infection_p = beta*I/N
    new_I = np.random.choice([0, 1], S, p=[1-infection_p, infection_p]).sum()
    new_R = np.random.choice([0, 1], I, p=[1-gamma, gamma]).sum()
    
    '''
    Suspecible population - new infected population each time and append into the lists of S.
    Infected population + new infected population and - nwe recovered population and append into I.
    Rcovered population + new recovered population and append into the list of R.
    '''
    S -= new_I
    I += new_I - new_R
    R += new_R
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

'''
We have already got lists of different population.
Then we draw the figure of these three population to see the changes during time course.
plt.grid(True) means this plot will show gridlines.
'''

plt.figure(dpi=150)
plt.plot(S_list, label="Susceptible")
plt.plot(I_list, label="Infected")
plt.plot(R_list, label="Recovered")
plt.xlabel("Time")
plt.ylabel("Number of People")
plt.title("SIR Model Simulation")
plt.legend()
plt.grid(True)
plt.show()