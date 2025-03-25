import numpy as np
import matplotlib.pyplot as plt


N = 10000
S = N - 1
I = 1
R = 0

beta = 0.3
gamma = 0.05

S_list = [S]
I_list = [I]
R_list = [R]

time_steps = 1000

for _ in range(time_steps):
    infection_p = beta*I/N
    new_I = np.random.choice([0, 1], S, p=[1-infection_p, infection_p]).sum()
    new_R = np.random.choice([0, 1], I, p=[1-gamma, gamma]).sum()
    S -= new_I
    I += new_I - new_R
    R += new_R
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

plt.figure(dpi=150)
plt.plot(S_list, label="Susceptible")
plt.plot(I_list, label="Infected")
plt.plot(R_list, label="Recovered")
plt.xlabel("Time")
plt.ylabel("Number of People")
plt.title("SIR Model Simulation")
plt.legend()
plt.grid(True)
plt.savefig("SIR_plot.png", format="png")
plt.show()