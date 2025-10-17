import numpy as np
import matplotlib.pyplot as plt

def solution(t, r=0.2, N0=100):
    return N0*np.exp(r*t)

if __name__ == "__main__":
    t = np.linspace(0, 20, 400)
    y = solution(t)
    plt.plot(t, y)
    plt.xlabel("t"); plt.ylabel("N(t)"); plt.title("Croissance exponentielle")
    plt.show()
