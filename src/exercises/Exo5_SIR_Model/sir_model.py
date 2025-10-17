import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

beta, gamma, N = 0.002, 0.5, 1000

def sir(t, y):
    S, I, R = y
    return [-beta*S*I, beta*S*I - gamma*I, gamma*I]

if __name__ == "__main__":
    y0 = [990, 10, 0]
    t = np.linspace(0, 30, 600)
    sol = solve_ivp(sir, [t[0], t[-1]], y0, t_eval=t)
    S, I, R = sol.y
    plt.plot(t, S, label="S")
    plt.plot(t, I, label="I")
    plt.plot(t, R, label="R")
    plt.legend(); plt.xlabel("t"); plt.ylabel("Population"); plt.title("SIR")
    plt.show()
