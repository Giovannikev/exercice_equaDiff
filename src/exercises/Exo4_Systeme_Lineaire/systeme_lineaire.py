import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

A = np.array([[3, -4],[1, 1]], float)

def f(t, X):
    return A @ X

if __name__ == "__main__":
    sol = solve_ivp(f, [0, 5], y0=[1,0], t_eval=np.linspace(0,5,400))
    x, y = sol.y
    plt.plot(x, y)
    plt.xlabel("x"); plt.ylabel("y"); plt.title("Portrait de phase (système linéaire)"); plt.axis("equal")
    plt.show()
