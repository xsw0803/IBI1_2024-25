import numpy as np
import matplotlib.pyplot as plt

vaccination_percentages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def simulate_sir_vaccination(vaccination_percent):
    N = 10000
    vaccinated = int(N * vaccination_percent / 100)
    S = N - vaccinated - 1 
    I = 1
    R = vaccinated  

    beta = 0.3
    gamma = 0.05

    S_list = [S]
    I_list = [I]
    R_list = [R]

    time_steps = 1000

    for i in range(time_steps):
            infection_p = beta * (I / N)
            if S <= 0:
                new_I = 0
            else:
                new_I = np.random.choice([0, 1], S, p=[1-infection_p, infection_p]).sum()
                new_I = min(new_I, S)  
    
            S -= new_I

            if I <= 0:
                new_R = 0
            else:
                new_R = np.random.choice([0, 1], I, p=[1-gamma, gamma]).sum()
                new_R = min(new_R, I)  
    
            I += new_I - new_R
            I = max(I, 0)  
            R += new_R
    
    
            S_list.append(S)
            I_list.append(I)
            R_list.append(R)
    
    return I_list

plt.figure(figsize=(6, 4), dpi=150)

for vp in vaccination_percentages:
    infected = simulate_sir_vaccination(vp)
    plt.plot(infected, label=f"{vp}%")

plt.xlabel("Time")
plt.ylabel("Number of Infected")
plt.title("Effect of Vaccination on Infection Spread")
plt.legend()
plt.grid(True)
plt.savefig("SIR_vaccination_plot.png", format="png")
plt.show()