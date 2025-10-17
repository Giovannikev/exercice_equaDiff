import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

class SystemeDynamique:
    def __init__(self, f: Callable[[float, float], float], y0: float, t_max: float, h: float):
        self.f, self.y0, self.t_max, self.h = f, y0, t_max, h

    def euler(self):
        n = int(self.t_max/self.h)
        t = np.linspace(0, self.t_max, n+1)
        y = np.zeros_like(t); y[0] = self.y0
        for k in range(n):
            y[k+1] = y[k] + self.h*self.f(t[k], y[k])
        return t, y

if __name__ == "__main__":
    f = lambda t, y: -0.1*y + 2
    sys = SystemeDynamique(f, y0=0.0, t_max=50.0, h=0.1)
    t, y = sys.euler()
    plt.plot(t, y)
    plt.xlabel("t"); plt.ylabel("y(t)"); plt.title("y' = -0.1y + 2 (Euler)")
    plt.show()
