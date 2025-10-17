import numpy as np
import matplotlib.pyplot as plt

def euler(y0=100, r=0.2, h=0.1, t_max=10.0):
    n = int(t_max / h)
    t = np.linspace(0, t_max, n+1)
    y = np.zeros_like(t); y[0] = y0
    for k in range(n):
        y[k+1] = y[k] + h*r*y[k]
    return t, y

if __name__ == "__main__":
    t, y = euler()
    plt.plot(t, y)
    plt.xlabel("t"); plt.ylabel("y(t)"); plt.title("Euler sur y' = r y")
    plt.show()
