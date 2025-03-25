import numpy as np
import matplotlib.pyplot as plt

'''
Make a list of vaccination_percentages as 0 to 100%.
Define a function as simulate_vaccination and inputs vaccination_percent.
'''
vaccination_percentages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def simulate_vaccination(vaccination_percent):
    
    '''
    For this function, total N is 10000, vaccinated population is N*vaccination_percent/100.
    Susceptible population is N - vaccnated population and infected population.
    Initial infected population is 1.
    '''
    N = 10000
    vaccinated = int(N * vaccination_percent / 100)
    S = N - vaccinated - 1 
    I = 1
    R = vaccinated  

    '''
    Beta is the probability of infection and gamma is probabilty of recovery.
    Create three separate lists for each population.
    '''
    beta = 0.3
    gamma = 0.05
    S_list = [S]
    I_list = [I]
    R_list = [R]

    '''
    The time steps is 1000, meaning we take the simulation for 1000 days.

    Use for loop in time steps and caluculate the propobility as infection_p.

    new_I is the new infected population. Achieve this by random.choice to assign 0/1 for infected and
    not infected person in all susceptible population, with a infection propability as infection_p.
    Then sum up all the values to get how many people are infected, because only 1 will be calculated
    and 0 doesn't make sense.

    Do the same foe new_R, meaning the new population of recovered people.
    '''

    time_steps = 1000

    for i in range(time_steps):
            infection_p = beta * (I / N)
            
            '''
            Specially, sometimes I or S will be negative numbers.
            To make this function works well, I add a step to determine the S or I as positive.

            If S <= 0, then all susceptible population has been infected before, new I is 0.
            Else, new_I must smaller than S.
            '''
            if S <= 0:
                new_I = 0
            else:
                new_I = np.random.choice([0, 1], S, p=[1-infection_p, infection_p]).sum()
                new_I = min(new_I, S)  
            
            '''
            Then, suspecible population is the previous population - new infected population.
            '''
            S -= new_I
            
            '''
            I is the same.
            If I <= 0, then all infected population has been recovered before, new R is 0.
            Else, new_R must smaller than infected population. 
            '''
            if I <= 0:
                new_R = 0
            else:
                new_R = np.random.choice([0, 1], I, p=[1-gamma, gamma]).sum()
                new_R = min(new_R, I)  
            
            '''
            Then infected population is previous infected population + new infected population
            and - new recovered population.

            Sepcially, to make sure I is positive numbers for next loop, I must be 0 or I(positive).
            '''
            I += new_I - new_R
            I = max(I, 0)

            '''
            Recovered population is previous recovered population + new recovered population.
            '''  
            R += new_R
    
            '''
            Append new numbers into their lists.
            '''
            S_list.append(S)
            I_list.append(I)
            R_list.append(R)
    
    '''
    The end of this defined function, and the outputs should be the I_list.
    '''
    return I_list

'''
Draw the figure.
'''
plt.figure(figsize=(6, 4), dpi=150)

'''
For every vp values in vaccination_percentages list:
    
    Infected values mean the output of each different vaccination_percentages will have a one-to-one
    correspond with one I_list.
    
    Then draw the plot of infected values as specific I_list and with the label to show corresponding
    vaccination percentage.
'''
for vp in vaccination_percentages:
    infected = simulate_vaccination(vp)
    plt.plot(infected, label=f"{vp}%")

'''
Other parameters for the plot, and then show the plot with all percentages at same time.
'''
plt.xlabel("Time")
plt.ylabel("Number of Infected")
plt.title("Effect of Vaccination on Infection Spread")
plt.legend()
plt.grid(True)
plt.show()