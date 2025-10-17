import numpy as np
import matplotlib.pyplot as plt

def temperature(t, T0=80, Text=20, k=0.1):
    return Text + (T0-Text)*np.exp(-k*t)

if __name__ == "__main__":
    t = np.linspace(0, 60, 601)
    T = temperature(t)
    plt.plot(t, T)
    plt.xlabel("t (min)"); plt.ylabel("T(t) (°C)"); plt.title("Refroidissement de Newton")
    plt.show()
